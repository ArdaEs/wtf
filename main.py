import openai
import sys
import os



openai.api_key = "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"



def correctTypo(prompt):

	response = openai.Completion.create(
	  model="text-davinci-003",
	  prompt = gpt_prompt,
	  temperature=0,
	  max_tokens=100,
	  top_p=1.0,
	  frequency_penalty=0.0,
	  presence_penalty=0.0
	)

	return (response['choices'][0]['text'].lstrip())



if __name__ == '__main__':
	
	prev_command = ' '.join(sys.argv[1:])

	gpt_prompt = "Can you correct the typo that I've made in this shell command: '%s'. Please just write the corrected command without any explanations." % (prev_command)
	
	corrected_command = correctTypo(gpt_prompt)
	
	notif_user = input('Did you mean %s y/n: ' % (corrected_command))
	
	if notif_user.lower() == 'y':
		
		os.system(corrected_command)

	else:

		print('Sorry :(\n')
