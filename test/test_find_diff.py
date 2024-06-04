from find_diff import find_diff, extract_text_by_index

# Test case for punctuation and spacing
original="""It is known to all that how to become a good parent has been talked about all the time. Since young children has many demands, the way of parents to satisfy and teach them is curial for the future development of them. Whether to permit children to do whatever they want or set some limitations will cause different results. If parents allow their children to do everything, Children may get such benefits. But,,"""


revised="""It is known to all that how to become a beneficial parent has been talked about all the time. Since young children have many demands, the way parents satisfy and teach them is crucial for their future development. Whether to permit children to do whatever they want or set some limitations will cause different results. In my opinion, if parents allow their children to do everything, children may get such benefits. .But,"""

# Run the function and print results
diffs_dict = find_diff(original, revised)

expect_result = {
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
  4: {
    'type': 'Deletion',
    'original': 'to',
    'origin_index': 146,
    'revised': '',
    'revised_index': 150
  },
  5: {
    'type': 'Replacement',
    'original': 'curial',
    'origin_index': 175,
    'revised': 'crucial',
    'revised_index': 176
  },
  6: {
    'type': 'Replacement',
    'original': 'the',
    'origin_index': 186,
    'revised': 'their',
    'revised_index': 188
  },
  7: {
    'type': 'Deletion',
    'original': 'of them',
    'origin_index': 209,
    'revised': '',
    'revised_index': 212
  },
  8: {
    'type': 'Replacement',
    'original': 'If',
    'origin_index': 324,
    'revised': 'In my opinion, if',
    'revised_index': 320
  },
  9: {
    'type': 'Replacement',
    'original': 'Children',
    'origin_index': 374,
    'revised': 'children',
    'revised_index': 385
  },
  10: {
    'type': 'Insertion',
    'original': '',
    'origin_index': 406,
    'revised': '.',
    'revised_index': 417
  },
  11: {
    'type': 'Deletion',
    'original': ',',
    'origin_index': 410,
    'revised': '',
    'revised_index': 422
  }
}

# Compare diffs_dict == expect_result
# use a loop method to check each item in the expect_result and diffs_dict
# and compare the values of the two dicts
for idx, change in expect_result.items():
    print('diffs_dict[idx]: ', diffs_dict[idx], change)
    assert diffs_dict[idx] == change, f"Test failed for index {idx}!"


#  Compare the text extracted by index
for idx, change in expect_result.items():
    origin_text = extract_text_by_index(original, change['origin_index'], len(change['original']))
    revised_text = extract_text_by_index(revised, change['revised_index'], len(change['revised']))

    assert origin_text == change['original'], f"Original text mismatch: expected {change['original']}, found {origin_text}"
    assert revised_text == change['revised'], f"Revised text mismatch: expected {change['revised']}, found {revised_text}"
