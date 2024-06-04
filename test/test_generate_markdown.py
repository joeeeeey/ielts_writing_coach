from generate_markdown import generate_task_analysis_md

# Example JSON input
json_input = '''
{
    "Aspect": [
        {
            "Essay Topic": "Some parents give their children everything that their children ask for or allow them to do whatever they want to do. Is this good for children? What could be consequences for these children when they grow up?"
        },
        {
            "Key Questions": [
                "Give your opinion if this situation is good for children?",
                "What could be consequences for these children when they grow up?"
            ]
        },
        {
            "Keywords and Synonyms": {
                "parents": "guardians, caregivers",
                "children": "youngsters, offspring, minors",
                "everything": "all things, every need or demand",
                "ask for": "request, seek",
                "allow": "permit, let",
                "consequences": "results, effects, outcomes",
                "grow up": "mature, develop, age"
            }
        }
    ]
}
'''

# Convert JSON to Markdown
markdown_output = generate_task_analysis_md(json_input)
print(markdown_output)
