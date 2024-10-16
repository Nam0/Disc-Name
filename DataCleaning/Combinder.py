import os
import json

def combine_json_files(input_dir, output_dir):
    for folder_name in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder_name)
        if os.path.isdir(folder_path):
            combined_data = {'Conversations': []}
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.json'):
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)
                        combined_data['Conversations'].extend(data['Conversations'])

            output_file = os.path.join(output_dir, f'{folder_name}.json')
            with open(output_file, 'w', encoding='utf-8') as outfile:
                json.dump(combined_data, outfile, ensure_ascii=False, indent=4)

def main():
    input_directory = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\data\Formatted'
    output_directory = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\data\Combined'
    combine_json_files(input_directory, output_directory)

if __name__ == "__main__":
    main()
