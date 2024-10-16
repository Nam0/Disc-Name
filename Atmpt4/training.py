from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForSeq2Seq
from datasets import load_dataset
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

model_name = "microsoft/DialoGPT-small"
data_path = os.path.join("Data")
output_dir = os.path.join("DialoGPT-finetuned")

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  
model = AutoModelForCausalLM.from_pretrained(model_name)


data_files = {
    "train": [os.path.join(data_path, f"processedtrain_data{i}.jsonl") for i in range(1, 5)]
}

dataset = load_dataset('json', data_files=data_files)

train_test_split = dataset["train"].train_test_split(test_size=0.1)  
train_dataset = train_test_split["train"]
eval_dataset = train_test_split["test"]

def tokenize_function(examples):
    inputs = [f"{prompt} {tokenizer.eos_token} {response}" for prompt, response in zip(examples["prompt"], examples["response"])]
    tokenized = tokenizer(inputs, truncation=True, padding="max_length", max_length=128)
    
    
    tokenized["labels"] = tokenized["input_ids"].copy()
    
    return tokenized

tokenized_train_dataset = train_dataset.map(tokenize_function, batched=True, remove_columns=["prompt", "response"])
tokenized_eval_dataset = eval_dataset.map(tokenize_function, batched=True, remove_columns=["prompt", "response"])

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, padding=True)

training_args = TrainingArguments(
    output_dir=output_dir,
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_steps=10,
    save_steps=500,
    evaluation_strategy="steps",  
    save_total_limit=2,
    remove_unused_columns=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,  
    data_collator=data_collator
)

trainer.train()

model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)

print(f"Model fine-tuned and saved successfully in {output_dir}.")
