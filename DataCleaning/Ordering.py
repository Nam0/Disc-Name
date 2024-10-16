import json
import os

def find_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def sort_conversations(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data["Conversations"].sort(key=lambda x: int(x["Conversation"]))

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def sort_all_json_files(directory_path):
    json_files = find_json_files(directory_path)
    for json_file_path in json_files:
        sort_conversations(json_file_path)
        print(f'Sorted conversations in {json_file_path}')

directory_path = "C:/Users/Namo/Documents/GitHub/Disc-Name/New/data/Combined"
sort_all_json_files(directory_path)
