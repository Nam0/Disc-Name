import json
import os
from pathlib import Path

def find_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def collect_conversations_with_author(json_file_path, author_name):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    convos_to_keep = set()
    conversations = data["Conversations"]
    
    for idx, conversation in enumerate(conversations):
        for message in conversation["Messages"]:
            if message["author"] == author_name:
                convos_to_keep.add(int(conversation["Conversation"]))
                if idx > 0:
                    convos_to_keep.add(int(conversations[idx - 1]["Conversation"]))
                if idx < len(conversations) - 1:
                    convos_to_keep.add(int(conversations[idx + 1]["Conversation"]))
                break
    
    return sorted(convos_to_keep)

def export_conversations(json_file_path, convos_to_keep, output_directory):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    filtered_conversations = [conv for conv in data["Conversations"] if int(conv["Conversation"]) in convos_to_keep]
    
    new_data = {
        "Conversations": filtered_conversations
    }

    Path(output_directory).mkdir(parents=True, exist_ok=True)

    file_name = os.path.basename(json_file_path)
    output_file_path = os.path.join(output_directory, file_name)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

    print(f'Exported filtered conversations to {output_file_path}')

def collect_and_export_conversations(directory_path, author_name, output_directory):
    json_files = find_json_files(directory_path)
    
    for json_file_path in json_files:
        convos_to_keep = collect_conversations_with_author(json_file_path, author_name)
        if convos_to_keep:
            export_conversations(json_file_path, convos_to_keep, output_directory)

directory_path = "C:/Users/Namo/Documents/GitHub/Disc-Name/New/data/Combined"
author_name = 'i.am.name'
output_directory = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\data\SSSGrepped'
collect_and_export_conversations(directory_path, author_name, output_directory)
