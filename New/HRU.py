import os
import logging
import re
#Must be above gpt2 import
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('tensorflow').setLevel(logging.ERROR)
import gpt_2_simple as gpt2

def generate_response(prompt):
    system_prompt = "Your name is Name-AI, You are 23 years old\n"
    promptstr = f'{system_prompt}Prompt: "{prompt}"\nResponse'
    response_text = ""

    response_list = gpt2.generate(
        sess,
        run_name='AiName_new',
        checkpoint_dir=checkpoint_dir,
        prefix=promptstr,
        length=40,
        temperature=0.25,
        top_k=40,
        return_as_list=True,
        include_prefix=True
    )

    if response_list:
        response_text = response_list[0].split('\n')[2].strip()
        response_text = response_text.replace('"', '')
        response_text = response_text.split(': ')[1]

    return response_text

checkpoint_dir = r"C:\Users\Namo\Documents\GitHub\Disc-Name\New\checkpoint\AiName"
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='AiName_new', checkpoint_dir=checkpoint_dir)

try:
    while True:
        prompt = input("Enter a prompt: ")
        response_text = generate_response(prompt)
        if response_text and not response_text.isspace():
            print(f'Prompt: "{prompt}"')
            print(f'Response: "{response_text}"')
        else:
            print('No valid response generated.')
except KeyboardInterrupt:
    print("\nExiting the program.")
