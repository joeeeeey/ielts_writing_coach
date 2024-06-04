'''
functionality: compare origin and revise content

input: original, revised
output: changes_dict
'''
import re
import difflib

def find_diff(original, revised):
    # Tokenize the text, handling punctuation and spacing correctly
    original_tokens = re.findall(r'\w+|[.,!?;]', original)
    revised_tokens = re.findall(r'\w+|[.,!?;]', revised)

    # Mapping tokens back to their positions in the original texts
    original_positions = []
    revised_positions = []
    pos = 0
    for token in original_tokens:
        start = original.find(token, pos)
        end = start + len(token)
        original_positions.append((start, end))
        pos = end

    pos = 0
    for token in revised_tokens:
        start = revised.find(token, pos)
        end = start + len(token)
        revised_positions.append((start, end))
        pos = end

    # Using difflib to get a more structured output of differences
    s = difflib.SequenceMatcher(None, original_tokens, revised_tokens)
    changes_dict = {}
    idx = 1

    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag == 'replace':
            # Joining tokens carefully to avoid unwanted spaces before punctuation
            original_part = ' '.join(original_tokens[i1:i2]).replace(' ,', ',').replace(' .', '.')
            revised_part = ' '.join(revised_tokens[j1:j2]).replace(' ,', ',').replace(' .', '.')
            changes_dict[idx] = {
                'type': 'Replacement',
                'original': original_part,
                'origin_index': original_positions[i1][0],
                'revised': revised_part,
                'revised_index': revised_positions[j1][0],
            }
            idx += 1
        elif tag == 'insert':
            # Properly joining tokens for insertion
            revised_part = ' '.join(revised_tokens[j1:j2]).replace(' ,', ',').replace(' .', '.')
            changes_dict[idx] = {
                'type': 'Insertion',
                'original': '',
                'origin_index': original_positions[i1][0] if i1 < len(original_positions) else len(original),
                'revised': revised_part,
                'revised_index': revised_positions[j1][0],
            }
            idx += 1
        elif tag == 'delete':
            original_part = ' '.join(original_tokens[i1:i2]).replace(' ,', ',').replace(' .', '.')
            changes_dict[idx] = {
                'type': 'Deletion',
                'original': original_part,
                'origin_index': original_positions[i1][0],
                'revised': '',
                'revised_index': revised_positions[j1][0] if j1 < len(revised_positions) else len(revised),
            }
            idx += 1

    return changes_dict


# Function to extract text by index
def extract_text_by_index(text, start_index, length):
    return text[start_index:start_index + length]


