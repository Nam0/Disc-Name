from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

output_dir = "JimmyV3-finetuned"
tokenizer = AutoTokenizer.from_pretrained(output_dir)

tokenizer.pad_token = "<pad>"
tokenizer.add_special_tokens({'pad_token': tokenizer.pad_token})
model = AutoModelForCausalLM.from_pretrained(output_dir)
model.resize_token_embeddings(len(tokenizer))

def generate_response(prompt, history=None):
    
    if history is not None:
        prompt = history + prompt + tokenizer.eos_token
    else:
        prompt = prompt + tokenizer.eos_token

    input_ids = tokenizer.encode(prompt, return_tensors='pt', padding=True, truncation=True)
    attention_mask = (input_ids != tokenizer.pad_token_id).long()  

    with torch.no_grad():
        response_ids = model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=256,
            num_return_sequences=1,  
            pad_token_id=tokenizer.pad_token_id,
            do_sample=True,
            temperature=0.9, 
            top_p=0.2,
            top_k=50,  
        )

    response = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    if not response.strip():
        response = "Hmm, I didn't get that. Can you say it differently?"
    return response

def chat():
    history = []
    print("Chat with Jimmy! Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending chat.")
            break
        
        history.append(f"You: {user_input} {tokenizer.eos_token}")
        response = generate_response(user_input, history=' '.join(history[-6:]))  
        print("Jimmy:", response)
        history.append(f"Jimmy: {response} {tokenizer.eos_token}")
        if len(history) > 10:  
            history.pop(0)  

if __name__ == "__main__":
    chat()
