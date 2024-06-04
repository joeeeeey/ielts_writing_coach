from find_diff import find_diff
from get_description import generate_diff_description, generate_markdown_revision, generate_revision_explanation, generate_task_analysis_md, save_md_file, compose_part1_input_json, markdown_to_pdf
# from tmp.origin import content as original_dict
# from tmp.revised import content as revised_dict
import sys
import json

# step1: get the input of part1
# step2: ask chatGPT of part1 to get the output
# step3: use part1 output to generate the diff_description
# step4: use diff_description to generate part2 input
# step5: ask chatGPT of part2 to get the output
# step6: use output of part2 to generate markdown
def _generate_diff_description(essay_id):
    # read original_dict from tmp/essays/{essay_id}/part1_input.json
    # read revised_dict from tmp/essays/{essay_id}/part1_output.json
    original_dict = {}
    revised_dict = {}
    with open(f"tmp/essays/{essay_id}/part1_input.json", 'r') as f:
        original_dict = json.load(f)
    with open(f"tmp/essays/{essay_id}/part1_output.json", 'r') as f:
        revised_dict = json.load(f)

    origin_content_dict = original_dict["origin_content_dict"]
    revised_content_dict = revised_dict["revised_content_dict"]

    index_of_revision_list = 0 # this should be incremented by 1 for each iteration
    diff_description_output = {}

    for paragraph_index, original in origin_content_dict.items():
        # ========= part 1 =========
        revised = revised_content_dict[paragraph_index]["content"]
        diffs_dict = find_diff(original, revised)
        # TODO, save diff dict into tmp/essays/{essay_id}/diffs_dict.json
        diff_descriptions = generate_diff_description(original, revised, diffs_dict)

        # - add index before each diff_description
        # - increase the variable index_of_revision_list
        for i in range(len(diff_descriptions)):
            index_of_revision_list += 1
            diff_descriptions[i] = f"{str(index_of_revision_list)}. {diff_descriptions[i]}"
            # add diff_descriptions into diff_description_output
            if paragraph_index not in diff_description_output:
                diff_description_output[paragraph_index] = []
            diff_description_output[paragraph_index].append(diff_descriptions[i])

    diff_description_output = json.dumps(diff_description_output, indent=4, ensure_ascii=False) # This is the input of chatGPT
    with open(f"tmp/essays/{essay_id}/diff_description.json", "w") as f:
        f.write(diff_description_output)
        print("diff_description.json is saved.")

def _generate_markdown(essay_id):
    def read_json_from_tmp_comments(id):
        with open(f'tmp/essays/{id}/comments.json', 'r') as f:
            return json.load(f)

    original_dict = {}
    revised_dict = {}
    revised_comments = read_json_from_tmp_comments(essay_id)
    with open(f"tmp/essays/{essay_id}/part1_input.json", 'r') as f:
        original_dict = json.load(f)
    with open(f"tmp/essays/{essay_id}/part1_output.json", 'r') as f:
        revised_dict = json.load(f)

    origin_content_dict = original_dict["origin_content_dict"]
    revised_content_dict = revised_dict["revised_content_dict"]

    paragraph_revision_output = {} # this is part of final output

    markdown_revision_output = {
        "task_analysis_output": generate_task_analysis_md(json.dumps(revised_dict['Task Analysis'])),
        "paragraph_revision_output": paragraph_revision_output,
        "score_output": {}
    }

    index_of_revision_list = 0
    for paragraph_index, original in origin_content_dict.items():
        # ========= part 1 =========
        revised = revised_content_dict[paragraph_index]['content']
        diffs_dict = find_diff(original, revised)
        generate_markdown_res = generate_markdown_revision(original, revised, diffs_dict, index_of_revision_list) # the revised markdown based on origin content
        diffs_dict = find_diff(original, revised)
        # diff_descriptions = generate_diff_description(original, revised, diffs_dict)
        for i in range(len(diffs_dict.items())):
            index_of_revision_list += 1
        # for i in range(len(diff_descriptions)):
        #     index_of_revision_list += 1
        # ========= part2 ===========
        revised_comment = revised_comments.get(str(paragraph_index))

        paragraph_revision_output[paragraph_index] = {
            "result_text": generate_markdown_res["result_text"],
            "table_explain": generate_revision_explanation(generate_markdown_res["changes_dict"], revised_comment) if revised_comment else {}
        }

    save_md_file(markdown_revision_output, essay_id) # save the markdown file


def review_arg(action, essay_id):
    if action == "compose_part1_input":
        print("Option compose_part1_input_ selected. Performing action 1...")
        compose_part1_input_json(essay_id)
        # Perform action 1
    elif action == "generate_diff_description":
        print("Option generate_diff_description selected. Performing generate_diff_description...")
        _generate_diff_description(essay_id)
        # Perform action 2
    elif action == "generate_markdown":
        print("Option generate_markdown selected. Performing action 3...")
        _generate_markdown(essay_id)
        markdown_to_pdf(essay_id)
        # Perform action 3
    else:
        print("Invalid option. Please choose from 'option1', 'option2', or 'option3'.")

# python script.py option1
if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <option>")
        sys.exit(1)

    # Get the argument passed to the script
    action, essay_id = sys.argv[1], sys.argv[2]

    # Review the argument and perform corresponding actions
    review_arg(action, essay_id)
