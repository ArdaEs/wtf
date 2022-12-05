import re
import sys
import openai


def regex_gpt(prompt):

	openai.api_key = "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"

	response = openai.Completion.create(
	  model="text-davinci-003",
	  prompt=prompt,
	  temperature=0,
	  max_tokens=100,
	  top_p = 1.0,
	  frequency_penalty=0.0,
	  presence_penalty=0.0
	)

	return response['choices'][0]['text'].strip()


def main():
	
	regex_prompt = input("Please explain the pattern: \n")
	gpt_prompt = "Can you write the regex code of following condition: %s. Please just write the regex code without any explanations." % (regex_prompt)

	regex_code = regex_gpt(gpt_prompt)

	read_file = open(sys.argv[-1]).read()
	match_list = re.findall(regex_code, read_file)

	for match in match_list:
		print(match)


if __name__ == "__main__":
	main()
