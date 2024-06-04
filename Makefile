EASSY_ID ?= essay1

step1:
	python main.py compose_part1_input $(EASSY_ID)

step2:
	python main.py generate_diff_description $(EASSY_ID)

step3:
	python main.py generate_markdown $(EASSY_ID)
