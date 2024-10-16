import os
import json
from datetime import datetime

def find_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def merge_outliers_to_conversations(conversations, outliers):
    def parse_timestamp(message):
        return datetime.fromisoformat(message['timestamp'].replace('Z', '+00:00'))

    conversation_dict = {conv['Conversation']: conv for conv in conversations}

    for outlier in outliers:
        conv_id = outlier['Conversation']
        if conv_id in conversation_dict:
            conversation_dict[conv_id]['Messages'].extend(outlier['Messages'])
        else:
            conversation_dict[conv_id] = outlier

    for conv in conversation_dict.values():
        conv['Messages'].sort(key=parse_timestamp)

    return list(conversation_dict.values())

def integrate_outliers(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    conversations = data.get('Conversations', [])
    outliers = data.get('Outliers', [])

    updated_conversations = merge_outliers_to_conversations(conversations, outliers)

    data['Conversations'] = updated_conversations
    if 'Outliers' in data:
        del data['Outliers']

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def process_directory(directory):
    json_files = find_json_files(directory)
    for json_file in json_files:
        integrate_outliers(json_file)

directory_path = "C:/Users/Namo/Documents/GitHub/Disc-Name/New/data/Dm"
process_directory(directory_path)
