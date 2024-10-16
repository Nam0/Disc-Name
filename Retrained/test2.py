import torch
from transformers import LlamaTokenizer, LlamaForCausalLM


model_dir = r"C:\Users\Namo\Retrain"

tokenizer = LlamaTokenizer.from_pretrained(model_dir)
model = LlamaForCausalLM.from_pretrained(model_dir, torch_dtype=torch.float16)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


def generate_response(prompt):
    system_prompt = "Your name is Name-AI, You are 23 years old\n"
    promptstr = f'{system_prompt}Prompt: "{prompt}"\nResponse'

    inputs = tokenizer(promptstr, return_tensors="pt").to(device)

    outputs = model.generate(
        inputs["input_ids"], max_length=100, temperature=0.25, top_k=40
    )

    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response_text = response_text.replace(promptstr, "").strip()
    return response_text


try:
    while True:
        prompt = input("Enter a prompt: ")
        response_text = generate_response(prompt)
        if response_text and not response_text.isspace():
            print(f'Prompt: "{prompt}"')
            print(f'Response: "{response_text}"')
        else:
            print("No valid response generated.")
except KeyboardInterrupt:
    print("\nExiting the program.")
