# Save the fine-tuned model
model.save_pretrained("./Jimmy-finetuned")
tokenizer.save_pretrained("./Jimmy-finetuned")

# Load the fine-tuned model
model = AutoModelForCausalLM.from_pretrained("./Jimmy-finetuned")
tokenizer = AutoTokenizer.from_pretrained("./Jimmy-finetuned")

input_text = "How are you?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

output = model.generate(input_ids, max_length=50, num_return_sequences=1)
response = tokenizer.decode(output[0], skip_special_tokens=True)

print(response)
