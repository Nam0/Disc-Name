import json

def limit_tokens(text, max_tokens=64):
    tokens = text.split()
    return " ".join(tokens[:max_tokens])

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            data = json.loads(line)
            data["prompt"] = limit_tokens(data["prompt"], max_tokens=64)
            data["response"] = limit_tokens(data["response"], max_tokens=64)
            outfile.write(json.dumps(data) + '\n')

files = [
    ("Data/train_data1.jsonl", "Data/processedtrain_data1.jsonl"),
    ("Data/train_data2.jsonl", "Data/processedtrain_data2.jsonl"),
    ("Data/train_data3.jsonl", "Data/processedtrain_data3.jsonl"),
    ("Data/train_data4.jsonl", "Data/processedtrain_data4.jsonl")
]

for input_file, output_file in files:
    process_file(input_file, output_file)

print("Processing complete.")
