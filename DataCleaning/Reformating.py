import os
import json
import re

def find_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def filter_messages(messages):
    url_pattern = re.compile(r'https?://\S+')
    emoji_pattern = re.compile(r':\w+:')
    
    filtered_messages = []
    for message in messages:
        content = message['content']
        if url_pattern.search(content):
            continue
        
        content = emoji_pattern.sub('', content).strip()
        
        if content:
            filtered_message = {
                'id': message['id'],
                'timestamp': message['timestamp'],
                'content': content,
                'author': message['author']['name']
            }
            if 'reference' in message and 'messageId' in message['reference']:
                filtered_message['referenceMessageId'] = message['reference']['messageId']
            filtered_messages.append(filtered_message)
    return filtered_messages

def load_and_filter_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        messages = data.get('messages', [])
        filtered_messages = filter_messages(messages)
        guild_name = data['guild']['name']
        channel_name = data['channel']['name']
        channel_id = data['channel']['id']
    return filtered_messages, guild_name, channel_name, channel_id

def reformat_filename(original_filename, guild_name, channel_name, channel_id):
    guild_name = re.sub(r'[^\w\s]', '', guild_name).replace(' ', '')
    channel_name = re.sub(r'[^\w\s]', '', channel_name).replace(' ', '')
    
    if guild_name == "DirectMessages":
        new_filename = f"DirectMessages{channel_id}.json"
    else:
        new_filename = f"{guild_name}{channel_id}.json"
    
    part_info = re.search(r'\[part \d+\]', original_filename)
    if part_info:
        new_filename = new_filename.replace('.json', f"{part_info.group()}.json")
    
    return new_filename

def save_filtered_data(directory, filtered_data, original_path, new_filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    new_filepath = os.path.join(directory, new_filename)
    
    with open(new_filepath, 'w', encoding='utf-8') as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=4)

def process_json_files(source_directory, target_directory):
    json_files = find_json_files(source_directory)
    for file_path in json_files:
        filtered_data, guild_name, channel_name, channel_id = load_and_filter_json(file_path)
        original_filename = os.path.basename(file_path)
        new_filename = reformat_filename(original_filename, guild_name, channel_name, channel_id)
        save_filtered_data(target_directory, filtered_data, file_path, new_filename)

def main():
    source_directory = "C:/Users/Namo/Documents/DiscData/Name"
    target_directory = "C:/Users/Namo/Documents/GitHub/Disc-Name/New/data/Formatted"
    process_json_files(source_directory, target_directory)

if __name__ == "__main__":
    main()
