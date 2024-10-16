import json
import os
import re
from pathlib import Path

def find_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def clean_text(text):
    text = re.sub(r'[\*\_\~]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def reformat_messages(json_file_path, output_directory, ai_author):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    output_lines = []

    for conversation in data["Conversations"]:
        messages_by_author = {}
        for message in conversation["Messages"]:
            author = message["author"]
            if author not in messages_by_author:
                messages_by_author[author] = []
            cleaned_content = clean_text(message["content"])
            messages_by_author[author].append(cleaned_content)

        for author, messages in messages_by_author.items():
            if author == ai_author:
                output_lines.append(f'Response: {" ".join(messages)}')
            else:
                output_lines.append(f'Prompt: {" ".join(messages)}')

    Path(output_directory).mkdir(parents=True, exist_ok=True)

    file_name = os.path.basename(json_file_path).replace('.json', '.txt')
    output_file_path = os.path.join(output_directory, file_name)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(output_lines))

    print(f'Reformatted messages and saved to {output_file_path}')

def reformat_all_json_files(input_directory, output_directory, ai_author):
    json_files = find_json_files(input_directory)
    for json_file_path in json_files:
        reformat_messages(json_file_path, output_directory, ai_author)

input_directory = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\data\SSSGrepped'
output_directory = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\data\SSSMorphed'
ai_author = 'i.am.name'
reformat_all_json_files(input_directory, output_directory, ai_author)
