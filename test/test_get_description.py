from get_description import generate_diff_description


original="""It is known to all that how to become a good parent has been talked about all the time. Since young children has many demands, the way of parents to satisfy and teach them is curial for the future development of them. Whether to permit children to do whatever they want or set some limitations will cause different results. If parents allow their children to do everything, Children may get such benefits. But,,"""

revised="""It is known to all that how to become a beneficial parent has been talked about all the time. Since young children have many demands, the way parents satisfy and teach them is crucial for their future development. Whether to permit children to do whatever they want or set some limitations will cause different results. In my opinion, if parents allow their children to do everything, children may get such benefits. .But,"""

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

# Generate the diff descriptions
diff_descriptions = generate_diff_description(original, revised, expect_result)
for i in diff_descriptions:
    print(i)


# [
#   replacement: a good parent => a beneficial parent
#   replacement: children has many => children have many
#   deletion: way of parents => way  parents
#   deletion: parents to satisfy => parents  satisfy
#   replacement: is curial for => is crucial for
#   replacement: for the future => for their future
#   deletion: development of them. Whether => development . Whether
#   replacement: results. If parents => results. In my opinion, if parents
#   replacement: everything, Children may => everything, children may
#   insertion: benefits. .But,
#   deletion: benefits. But,, => benefits. But
# ]