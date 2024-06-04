'''
act as senior software engineer, write a python function which can detect paragraph in a whole essay by blank line. if there are multiple blank lines, it should be considered as one blank line.
The input is a long string may have multiple paragraphs, the output json, key is the index of paragraph, value is the paragraph content. 

sample input:
"""
paragraph 1
paragraph 2

paragraph 3
paragraph 4


paragraph 5
"""

sample output:
{
	"1": "paragraph 1",
	"2": "paragraph 2",
	"3": "paragraph 3",
	"4": "paragraph 4"
}

{'1': 'paragraph 1', '2': 'paragraph 2', '3': 'paragraph 3', '4': 'paragraph 4', '5': 'paragraph 5'}


write a test case to test the function and pass it, reference: 
```python
list(filter(lambda x: not not x, essay.split("\n")))
```
'''

content = {
	"topic": "Some parents give their children everything that their children ask for or allow them to do whatever they want to do. Is this good for children? What could be consequences for these children when they grow up?",
	"origin_content_dict":
		{
			1: """No doubt that children are not a distraction from more important work, they are the most important work. It is true that parent’s education of children has a great influence on children’s growth. Some people hold the view that parents should provide everything that the children want, others argue that it is harmful for children’s growth if parents don’t limit children’s requirements. I deem that the best choice is parents should to give a proper limitation towards children’s ideas but also listening children’s voices to help them choice the correct and happy thing.""",
			2: """The main reason for people who think it is necessary to limit children’s requirements is that restrictions are beneficial to children’s growth including health and study. This is because parents all want to lead their children in a correct way which are good for them. With the limitation, parents has more chance to help children to avoid the bad habits which are not suitable for their growth. For example, some children are fond of eating sweat foods, even they don’t like to brush the teeth. If parents don’t interfere their daily life habits, they will have tooth decay and have to go the hospital which is a more terrible thing for them than not eating the sweat food. But if parents gives much restriction on their habits, then the children can have a good health or study hard and get into a good university in the future. Hence, parents need to limit children to do something correct.""",
			3: """Undeniably, some people may say children are not able to have a happy life if parents give too much limitation towards children’s choice. They believe that children who are free to choose what they like can have a more happy childhood and a bright future. If children have freedom to do everything they want, they can find their interests early and gain a lot of happiness. After they find their interests in a young age, they have more possibility to achieve success in this area after they grow up, because they can spend much more time on learning and practicing the skills than other normal people. As we all know that many technical genius started their interests in a young age, such as Elon Musk, he had interest on computer and game and gained a plenty of knowledges about it in 10 years old. Now he has became a giant crocodile in multiple technology areas. So it is obvious that making children chose the thing they want to do is very important and valuable.""",
			4: """In conclusion, although limitation towards children’s requirements can help children avoid many unhealthy habits, It will also make children have an unhappy childhood and kill their’s interests. From my perspective, parents should balance the constraints towards children’s ideas, they should let children do what they like do and also leads them to a correct way so that children will have a happy, healthy and bright future."""
		}
}