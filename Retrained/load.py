from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the Mistral model and tokenizer
model_name = "mistralai/Mistral-7B-v0.1"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
