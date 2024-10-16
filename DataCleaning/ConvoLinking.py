import os
import json
from datetime import datetime

def reconstruct_threads(messages):
    threads = []
    current_thread = []
    current_timestamp = None

    for message in messages:
        timestamp = datetime.fromisoformat(message['timestamp'])
        if current_timestamp is None or (timestamp - current_timestamp).seconds > 300:  # Threshold for conversation continuity
            if current_thread:
                threads.append(current_thread.copy())
                current_thread.clear()
            current_thread.append(message)
            current_timestamp = timestamp
        else:
            current_thread.append(message)
            current_timestamp = timestamp

    if current_thread:
        threads.append(current_thread.copy())

    return threads

def categorize_threads(threads):
    categorized_threads = {'Conversations': [], 'Outliers': []}

    for idx, thread in enumerate(threads, start=1):
        thread_data = {'Conversation': f'{idx}', 'Messages': []}
        for message in thread:
            thread_data['Messages'].append({
                'id': message['id'],
                'timestamp': message['timestamp'],
                'content': message['content'],
                'author': message['author']
            })
        if len(thread) > 1:  
            categorized_threads['Conversations'].append(thread_data)
        else: 
            categorized_threads['Outliers'].append(thread_data)

    return categorized_threads

def process_json_files(directory):
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            processed_messages = json.load(file)
        
        threads = reconstruct_threads(processed_messages)
        categorized_threads = categorize_threads(threads)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(categorized_threads, file, ensure_ascii=False, indent=4)

def main():
    source_directory = "C:/Users/Namo/Documents/GitHub/Disc-Name/New/data/Formatted"
    process_json_files(source_directory)

if __name__ == "__main__":
    main()
