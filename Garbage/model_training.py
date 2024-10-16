from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

def train_model(dialogues, output_dir):
    model_name = 'gpt2'
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    
    tokenized_dialogues = [tokenizer.encode(dialogue, add_special_tokens=True) for dialogue in dialogues]

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=1000,
        save_total_limit=2,
    )
    trainer = Trainer(
        model=model,
        args=training_args,
    )
    trainer.train(tokenized_dialogues)

    model.save_pretrained(output_dir)

    return output_dir  


if __name__ == "__main__":
    example_dialogues = [["Hello", "Hi there"], ["How are you?", "I'm fine, thank you."]]
    trained_model_path = train_model(example_dialogues, './fine_tuned_model')
    print(f"Trained model saved at: {trained_model_path}")
