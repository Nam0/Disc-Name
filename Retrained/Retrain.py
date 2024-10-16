from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import torch

torch.cuda.empty_cache()

dataset = load_dataset('json', data_files='Data/train_data.jsonl')

model_name = "TinyJimmyV2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

tokenizer.pad_token = tokenizer.eos_token  

def tokenize_function(examples):
    prompts = examples["prompt"] if isinstance(examples["prompt"], list) else [examples["prompt"]]
    responses = examples["response"] if isinstance(examples["response"], list) else [examples["response"]]
    combined_texts = [prompt + tokenizer.eos_token + response for prompt, response in zip(prompts, responses)]
    tokenized_inputs = tokenizer(combined_texts, truncation=True, padding="max_length", max_length=64)
    tokenized_inputs["labels"] = tokenized_inputs["input_ids"].copy()  
    
    return tokenized_inputs


tokenized_dataset = dataset.map(tokenize_function, batched=True)

training_args = TrainingArguments(
    output_dir="./TinyJimmyV2-finetuned",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=2,  
    fp16=True,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir="./logs",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
)

trainer.train()
