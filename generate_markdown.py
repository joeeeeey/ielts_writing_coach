'''
Steps:

Step1. Generate markdown table of Task Analysis from json input, output format:

## Task Analysis

| Aspect                 | Details                                                                                                  |
|------------------------|----------------------------------------------------------------------------------------------------------|
| **Essay Topic**        | Some parents give their children everything that their children ask for or allow them to do whatever they want to do. Is this good for children? What could be consequences for these children when they grow up? |
| **Key Questions**      | 1. Give your opinion if this situation is good for children?                                                                            |
|                        | 2. What could be consequences for these children when they grow up?                                      |
| **Keywords and Synonyms** |                                                                                                          |
| *parents*              | guardians, nurturer, custodian                                                                           |
| *give*                 | extend, provide, supply                                                                                  |
| *children*             | youngsters, minors, young people, offspring, young generation, young population, rising generation       |
| *ask for*              | need and wants, requests, appeal                                                                         |
| *allow*                | permit, authorize, grant                                                                                 |
| *to do whatever they want to do* | do as they please, do as they wish, do what they want    

Step2. Generate markdown paragraph which mixed with original and revised content, input format:
```
{
  diff_dict = {
  1: {
    'type': 'Replacement',
    'original': 'good',
    'origin_index': 40,
    'revised': 'beneficial',
    'revised_index': 40
  },
  2: {
    'type': 'Replacement',
    'original': 'has',
    'origin_index': 109,
    'revised': 'have',
    'revised_index': 115
  },
  3: {
    'type': 'Deletion',
    'original': 'of',
    'origin_index': 135,
    'revised': '',
    'revised_index': 142
  },
},
 origin_text: "",
 revised_text: "",
}
```

output format:
```json
{

1~~good~~#1#beneficial#2# parent has been talked about all the time. Since young children 2~~has~~#1#have#2# many demands, the way 3#1#~~of~~#2#  parents 4#1#~~to~~#2#  satisfy and teach them is 5~~curial~~#1#crucial#2# for 6~~the~~#1#their#2# future development of them. Whether to permit children to do whatever they want or set some limitations will cause different results. 7#1#In my opinion#2#8#1#,#2# 9~~If~~#1#if#2# parents allow their children to do everything, 10~~Children~~#1#children#2# may get such benefits.
}

'''

import json

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

# Example JSON input
