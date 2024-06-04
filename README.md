virtualenv -p $PYENV_ROOT/versions/3.12.2/bin/python .py3 
source .py3/bin/activate
pip install markdown2pdf


## TODO
[x] generate input function
[] update prompt to get score
[] [prompt update] Task Analysis => "key question" should be based on type of topic
[] convert output under comments and revised into a markdown output
[] be careful with escape in input, like origin text use ", input will appear \", which may make chatGPT consider \" is origin text.




## Optimize prompt
https://platform.openai.com/docs/guides/prompt-engineering

https://platform.openai.com/docs/guides/prompt-engineering/tactic-specify-the-steps-required-to-complete-a-task
### step by step:

Use the following step-by-step instructions to respond to user inputs.

Step 1 - The user will provide you with text in triple quotes. Summarize this text in one sentence with a prefix that says "Summary: ".

Step 2 - Translate the summary from Step 1 into Spanish, with a prefix that says "Translation: ".



**temperature** number or null
Optional
Defaults to 1
What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

We generally recommend altering this or top_p but not both.# ielts_writing_coach
