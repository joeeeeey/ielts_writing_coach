import json
'''
I need you to improve the python generate_diff_description function according to the input and output, currently the function can not use `` to surround the replacement word, insertion word and deletion word, which check it the the output.


input:
```
@origin: No doubt that children are not a distraction from more important work, they are the most important work.
@revised: There is no doubt that children are not just a diversion from more important work
@diffs_dict:  {1: {'type': 'Replacement', 'original': 'No', 'origin_index': 0, 'revised': 'There is no', 'revised_index': 0}, 2: {'type': 'Insertion', 'original': '', 'origin_index': 31, 'revised': 'just', 'revised_index': 40}, 3: {'type': 'Replacement', 'original': 'distraction', 'origin_index': 33, 'revised': 'diversion', 'revised_index': 47}, 4: {'type': 'Deletion', 'original': ',', 'origin_index': 69, 'revised': '', 'revised_index': 84}, 5: {'type': 'Replacement', 'original': 'important', 'origin_index': 89, 'revised': 'crucial', 'revised_index': 102}}

output:
```json
[
  "1. replacement: a `good` parent => a `beneficial` parent",
  "2. insertion: children many => children `have` many",
  "3. deletion: parents `need` to => parents to",
]
```
'''

# def generate_diff_description(original, revised, diffs_dict):
#     # Helper function to extract surrounding text
#     def get_surrounding_text(text, index, length, num_words=1):
#         words = text.split()
#         positions = [0] * (len(words) + 1)
        
#         # Calculate the start and end positions for each word
#         for i in range(1, len(words) + 1):
#             positions[i] = positions[i - 1] + len(words[i - 1]) + 1  # include space in length

#         # Find the position in the split words list
#         start_word_index = next((i for i, pos in enumerate(positions) if pos > index), -1) - 1
#         end_word_index = next((i for i, pos in enumerate(positions) if pos >= index + length), -1)
        
#         start = max(0, start_word_index - num_words)
#         end = min(len(words), end_word_index + num_words)
        
#         return " ".join(words[start:end])

#     results = []
    
#     for idx, diff in diffs_dict.items():
#         if diff['type'] == 'Replacement':
#             original_len = len(diff['original'])
#             revised_len = len(diff['revised'])
#             origin_surr = get_surrounding_text(original, diff['origin_index'], original_len)
#             origin_surr = origin_surr.replace(diff['original'], f"'{diff['original']}'")
#             revised_surr = get_surrounding_text(revised, diff['revised_index'], revised_len)
#             revised_surr = revised_surr.replace(diff['revised'], f"'{diff['revised']}'")
#             results.append(f"replacement: {origin_surr} => {revised_surr}")
        
#         elif diff['type'] == 'Insertion':
#             revised_len = len(diff['revised'])
#             revised_surr = get_surrounding_text(revised, diff['revised_index'], revised_len)
#             revised_surr = revised_surr.replace(diff['revised'], f"'{diff['revised']}'")
#             results.append(f"insertion: {revised_surr}")
        
#         elif diff['type'] == 'Deletion':
#             original_len = len(diff['original'])
#             origin_surr = get_surrounding_text(original, diff['origin_index'], original_len)
#             results.append(f"deletion: {origin_surr} => {origin_surr.replace(diff['original'], '').strip()}")

#     return results

def generate_diff_description(original, revised, diffs_dict):
    # Helper function to extract surrounding text
    def get_surrounding_text(text, index, length, num_words=1):
        words = text.split()
        positions = [0] * (len(words) + 1)
        
        # Calculate the start and end positions for each word
        for i in range(1, len(words) + 1):
            positions[i] = positions[i - 1] + len(words[i - 1]) + 1  # include space in length

        # Find the position in the split words list
        start_word_index = next((i for i, pos in enumerate(positions) if pos > index), -1) - 1
        end_word_index = next((i for i, pos in enumerate(positions) if pos >= index + length), -1)
        
        start = max(0, start_word_index - num_words)
        end = min(len(words), end_word_index + num_words)
        
        return " ".join(words[start:end])

    results = []
    
    for idx, diff in sorted(diffs_dict.items()):
        if diff['type'] == 'Replacement':
            original_text = f"`{diff['original']}`"
            revised_text = f"`{diff['revised']}`"
            original_len = len(diff['original'])
            revised_len = len(diff['revised'])
            origin_surr = get_surrounding_text(original, diff['origin_index'], original_len)
            revised_surr = get_surrounding_text(revised, diff['revised_index'], revised_len)
            results.append(f"replacement: {origin_surr.replace(diff['original'], original_text)} => {revised_surr.replace(diff['revised'], revised_text)}")
        
        elif diff['type'] == 'Insertion':
            revised_text = f"`{diff['revised']}`"
            revised_len = len(diff['revised'])
            revised_surr = get_surrounding_text(revised, diff['revised_index'], revised_len)
            results.append(f"insertion: {revised_surr.replace(diff['revised'], revised_text)}")
        
        elif diff['type'] == 'Deletion':
            original_text = f"`{diff['original']}`"
            original_len = len(diff['original'])
            origin_surr = get_surrounding_text(original, diff['origin_index'], original_len)
            results.append(f"deletion: {origin_surr.replace(diff['original'], original_text)} => {origin_surr.replace(diff['original'], '').strip()}")

    return results



"""
I need you to create the python function based on generate_diff_description function 
to generate a markdown revised text based on the input and output.

input:
```
@origin: No doubt that children are not a distraction from more important work, they are the most important work.
@revised: There is no doubt that children are not just a diversion from more important work
@diffs_dict:  {1: {'type': 'Replacement', 'original': 'No', 'origin_index': 0, 'revised': 'There is no', 'revised_index': 0}, 2: {'type': 'Insertion', 'original': '', 'origin_index': 31, 'revised': 'just', 'revised_index': 40}, 3: {'type': 'Replacement', 'original': 'distraction', 'origin_index': 33, 'revised': 'diversion', 'revised_index': 47}, 4: {'type': 'Deletion', 'original': ',', 'origin_index': 69, 'revised': '', 'revised_index': 84}, 5: {'type': 'Replacement', 'original': 'important', 'origin_index': 89, 'revised': 'crucial', 'revised_index': 102}}

Fro output:

rules:

- each time when revise happened, no matter its a replacement, insertion, deletion, always use a number {index_of_revision_list} before the start, e.g. 
    origin: `become a good parent`
    revised: `become a 1~~good~~<span style="color:red; font-weight:bold;">beneficial</span> parent`
- if do replacement, For every change you make to the original text:
    - Use Strikethroughs symbol `~~` for Original Text: Always use a strikethrough on the original text that is being replaced or modified.
    - Highlight Changes Clearly: Immediately after the strikethrough text, insert the replacement text formatted in bold and red. This should be encapsulated within special markers (<span style="color:red; font-weight:bold;"> and </span>).
    - Mandatory Display of Changes: It is crucial that both the original (stricken out) and the revised text are visible next to each other to clearly show the transformation from the original to the revised text.
  e.g. 
	origin: `become a good parent`
	revised: `become a 1~~good~~<span style="color:red; font-weight:bold;">beneficial</span> parent`
- if the revise is a deletion of words,phrases or sentences, just use strike through symbol `~~` and bold red style for the specific text, e.g.
	origin: `the way of parents`
	revise: `the way 3<span style="color:red; font-weight:bold;">~~of~~</span> parents`
- if the revise is a insertion, just use bold red font insert the specific position, e.g.
	origin: `different results. if`
	revised: `different results. 7<span style="color:red; font-weight:bold;">In my opinion,</span> if`

Ok, after output rules, there is the sample json output
json
{
  'md_content': '''{index_of_revision_list+index}~~No~~<span style="color:red; font-weight:bold;">There is no doubt</span> that '''
}
```

THen i will tell you the reference function, note that although index_of_revision_list is not used now, you should use it for the "true index" with the index_of_revision_list+index
```python
def generate_diff_description(original, revised, diffs_dict, index_of_revision_list=0):
    # Helper function to extract surrounding text
    def get_surrounding_text(text, index, length, num_words=1):
        words = text.split()
        positions = [0] * (len(words) + 1)
        
        # Calculate the start and end positions for each word
        for i in range(1, len(words) + 1):
            positions[i] = positions[i - 1] + len(words[i - 1]) + 1  # include space in length

        # Find the position in the split words list
        start_word_index = next((i for i, pos in enumerate(positions) if pos > index), -1) - 1
        end_word_index = next((i for i, pos in enumerate(positions) if pos >= index + length), -1)
        
        start = max(0, start_word_index - num_words)
        end = min(len(words), end_word_index + num_words)
        
        return " ".join(words[start:end])

    results = []
    
    for idx, diff in sorted(diffs_dict.items()):
        if diff['type'] == 'Replacement':
            original_text = f"`{diff['original']}`"
            revised_text = f"`{diff['revised']}`"
            original_len = len(diff['original'])
            revised_len = len(diff['revised'])
            origin_surr = get_surrounding_text(original, diff['origin_index'], original_len)
            revised_surr = get_surrounding_text(revised, diff['revised_index'], revised_len)
            results.append(f"replacement: {origin_surr.replace(diff['original'], original_text)} => {revised_surr.replace(diff['revised'], revised_text)}")
        
        elif diff['type'] == 'Insertion':
            revised_text = f"`{diff['revised']}`"
            revised_len = len(diff['revised'])
            revised_surr = get_surrounding_text(revised, diff['revised_index'], revised_len)
            results.append(f"insertion: {revised_surr.replace(diff['revised'], revised_text)}")
        
        elif diff['type'] == 'Deletion':
            original_text = f"`{diff['original']}`"
            original_len = len(diff['original'])
            origin_surr = get_surrounding_text(original, diff['origin_index'], original_len)
            results.append(f"deletion: {origin_surr.replace(diff['original'], original_text)} => {origin_surr.replace(diff['original'], '').strip()}")

    return results
```
"""

def generate_markdown_revision(original, revised, diffs_dict, index_of_revision_list=0):
    result_text = original
    changes_dict = {} # {1: "$markdown_text", 2: "$markdown_text}
    offset = 0  # Offset to manage the changes affecting text positions

    # Sort the diffs by original index to handle them in the correct order
    sorted_diffs = sorted(diffs_dict.items(), key=lambda x: x[1]['origin_index'])
    for idx, diff in sorted_diffs:
        true_index = str(index_of_revision_list + idx)
        start_index = diff['origin_index'] + offset

        if diff['type'] == 'Replacement':
            end_index = start_index + len(diff['original'])
            replacement_text = f"<span style='color:red; font-weight:bold;'>{diff['revised']}</span>"
            # add into changes_dict
            change = f"~~{diff['original']}~~{replacement_text}"
            changes_dict[true_index] = change
            change_with_index = true_index + change
            result_text = result_text[:start_index] + change_with_index + result_text[end_index:]
            offset += len(change) - len(diff['original'])  # Update offset

        elif diff['type'] == 'Insertion':
            insertion_text = f"<span style='color:red; font-weight:bold;'>{diff['revised']}</span>"
            changes_dict[true_index] = insertion_text
            insertion_text_with_index = true_index + insertion_text
            result_text = result_text[:start_index] + insertion_text_with_index + result_text[start_index:]
            offset += len(insertion_text_with_index)

        elif diff['type'] == 'Deletion':
            deletion_text = f"<span style='color:red; font-weight:bold;'>~~{diff['original']}~~</span>"
            changes_dict[true_index] = deletion_text
            deletion_text_with_index = true_index + deletion_text
            result_text = result_text[:start_index] + deletion_text_with_index + result_text[start_index + len(diff['original']):]
            offset += len(deletion_text_with_index) - len(diff['original'])

    return {    
        "result_text": result_text,
        "changes_dict": changes_dict,
    }


"""
I need you to create the python function based on generate_markdown_revision function 
to generate revise explanation table based on the input and output.

In the `generate_markdown_revision` function, your output is a long string, but actually, the function already now each revision with index, this is important, because the markdown revised format content should be used in the  explanation table with index.

Let's begin from input:

input:
```
@changes_dict:  

```python dict
{1: {'1': "~~No~~<span style='color:red; font-weight:bold;'>There is no</span>", '2': "<span style='color:red; font-weight:bold;'>just</span>", '3': "~~distraction~~<span style='color:red; font-weight:bold;'>diversion</span>"}}
```

@revise_comments:
```json
{"$paragraph_index": {
    "$true_index": [$criteria, $error_point, $reason],
}}
```

```json
  {"1":{
        "1": ["CC", "Enhanced Clarity", "Expanded the phrase to provide a clearer introduction, setting a formal tone from the outset."],
        "2": ["LR", "Lexical Variation", "The insertion of 'just' adds emphasis and nuances the sentence, suggesting that children are beyond simply important."],
        "3": ["LR", "Word Choice", "Replaced 'distraction' with 'diversion' to avoid negative connotations associated with the original word."],
        }
      }
```
      
Fro output:

rules of explanation revise table:
- format of revise table is markdown table, has 4 columns, INDEX, ERRORS/CHANGES, ERROR TYPE, COMMENTS/BENCHMARK
- For INDEX column, it just the $true_index
- for ERRORS/CHANGES column, it just value of "$changes_dict" of the specific $true_index, e.g.`~~good~~<style>beneficial</style>`
- for ERROR TYPE column, it is used to summary what type of literacy problem is related to the criteria of IELTS writing task, it has 2 parts of information
	1. $error_point: $revise_comments[$paragraph_index][$true_index][1]
	2. $criteria: $revise_comments[$paragraph_index][$true_index][0]
  markdown output: <span style='color:red; font-weight:bold;'>$error_point</span><br>$criteria
- for COMMENTS/BENCHMARK column, use $reason, markdown output: 
  $reason: $revise_comments[$paragraph_index][$true_index][2]
    
Ok, after output rules, there is the sample json output
json
{
  'md_content': '''
| INDEX | ERRORS/CHANGES                      | Error Type                                          | COMMENTS/BENCHMARK                                                   |
|-------|-------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------|
| $true_index    | $changes_dict[$true_index]      | <span style='color:red; font-weight:bold;'>$error_point</span><br>$criteria          | $reason |
'''
}
```

"""

def generate_revision_explanation(changes_dict, revise_comments):
    # Initialize the markdown table header
    md_content = "| INDEX | ERRORS/CHANGES | Error Type | COMMENTS/BENCHMARK |\n"
    md_content += "|-------|-----------------|------------|--------------------|\n"

    # Iterate through each true_index and extract corresponding information
    for true_index, changes in changes_dict.items():
        # Get error point, criteria, and reason from revise_comments
        error_point = revise_comments.get(true_index,  [''])[0]
        criteria = revise_comments.get(true_index,  [''])[1]
        reason = revise_comments.get(true_index,  [''])[2]

        # Format the markdown content for this row
        md_content += f"| {true_index} | {changes} | <span style='color:red; font-weight:bold;'>{error_point}</span><br>{criteria} | {reason} |\n"

    return {'md_content': md_content}

'''
generate_task_analysis_md
'''
def generate_task_analysis_md(json_input):
    # Load the JSON data
    data = json.loads(json_input)
    
    # Initialize Markdown output with the table header
    markdown_output = '''
## Task Analysis

| Aspect                 | Details                                                                                                  |
|------------------------|----------------------------------------------------------------------------------------------------------|
'''
    
    # Process each aspect in the JSON
    for aspect in data['Aspect']:
        for key, value in aspect.items():
            if key == 'Essay Topic':
                # Add the essay topic
                markdown_output += f'| **{key}** | {value} |\n'
            elif key == 'Key Questions':
                # Add key questions with enumerated list
                markdown_output += f'| **{key}** | '
                markdown_output += ' |\n|                        | '.join([f'{i+1}. {q}' for i, q in enumerate(value)])
                markdown_output += ' |\n'
            elif key == 'Keywords and Synonyms':
                # Add keywords and synonyms
                markdown_output += f'| **{key}** | \n'
                for sub_key, synonyms in value.items():
                    markdown_output += f'| *{sub_key}* | {synonyms} |\n'

    return markdown_output

'''
markdown_revision_output = {
    "task_analysis_output": generate_task_analysis_md(json.dumps(revised_dict['Task Analysis'])),
    "paragraph_revision_output": {
        "1": {
            "result_text": "",
            "table_explain": "",
        }
    },
    "score_output": {}
}
'''
def save_md_file(output, essay_id):
    result_str = ''
    task_analysis_md_str = output['task_analysis_output']
    result_str += task_analysis_md_str

    result_str += "## Paragraph Revision\n\n"

    def combine_paragraph_revision_output(paragraph_revision_output, md_str):
        for paragraph_index, paragraph_output in paragraph_revision_output.items():
            result_text = paragraph_output['result_text']

            table_explain = paragraph_output['table_explain'].get("md_content", "")
            md_str += f"{result_text}\n\n"
            md_str += f"{table_explain}\n\n"
        return md_str

    result_str = combine_paragraph_revision_output(output['paragraph_revision_output'], result_str)

    with open(f"tmp/essays/{essay_id}/revision.md", "w") as f:
        f.write(result_str)




'''
def test_detect_paragraphs():
    essay = """
paragraph 1"
paragraph '2

paragraph 3
paragraph 4


paragraph 5
"""
    expected_output = {
        "1": "paragraph 1\"",
        "2": "paragraph \'2",
        "3": "paragraph 3",
        "4": "paragraph 4",
        "5": "paragraph 5"
    }
    print(detect_paragraphs(essay))
    assert detect_paragraphs(essay) == expected_output

# Run updated test case
test_detect_paragraphs()
'''
def detect_paragraphs(essay: str) -> dict:
    """
    Detects paragraphs in an essay based on blank lines.

    Args:
    - essay (str): The input essay containing paragraphs separated by blank lines.

    Returns:
    - dict: A dictionary where keys represent the index of paragraphs and values represent the paragraph content.
    """
    paragraphs = list(filter(lambda x: not not x, essay.split("\n")))  # Split essay into paragraphs based on non-empty lines
    return {str(i + 1): paragraph.strip() for i, paragraph in enumerate(paragraphs)}


'''
under tmp/essays/{essay_id}, there always topic.txt and content.txt,
this function need to read from these 2 files and return the dict as
{
  "topic": "$topic",
  "content": "$content_dict" (detect_paragraphs)
}
'''
def compose_part1_input_json(essay_id):
    with open(f"tmp/essays/{essay_id}/topic.txt", "r") as f:
        topic = f.read().strip()

    with open(f"tmp/essays/{essay_id}/content.txt", "r") as f:
        content = f.read().strip()

    # save json into file at tmp/essays/{essay_id}/part1_input.json
    # json dump in utf-8 format
    with open(f"tmp/essays/{essay_id}/part1_input.json", "w") as f:
        json.dump({
            "topic": topic,
            "origin_content_dict": detect_paragraphs(content)
        }, f, ensure_ascii=False, indent=4)




# import markdown2
# from weasyprint import HTML

def markdown_to_pdf(essay_id):
    pass
#     # Read the Markdown file
#     input_file = f"tmp/essays/{essay_id}/revision.md"
#     output_file = f"tmp/essays/{essay_id}/revision.pdf"

#     with open(input_file, "r", encoding="utf-8") as f:
#         markdown_content = f.read()

#     # Convert Markdown to HTML
#     html_content = markdown2.markdown(markdown_content)

#     # Save HTML to a temporary file
#     html_temp_file = "temp.html"
#     with open(html_temp_file, "w", encoding="utf-8") as f:
#         f.write(html_content)

#     # Convert HTML to PDF using WeasyPrint
#     HTML(html_temp_file).write_pdf(output_file)

#     # Delete the temporary HTML file
#     import os
#     os.remove(html_temp_file)

