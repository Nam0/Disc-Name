import os
from pathlib import Path

def combine_consecutive_lines(file_path, output_directory):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    combined_lines = []
    current_line = ""
    current_prefix = ""

    for line in lines:
        prefix, content = line.split(': ', 1)
        if prefix == current_prefix:
            current_line += " " + content.strip()
        else:
            if current_line:
                current_line = current_line.replace('"', "'") 
                combined_lines.append(f'{current_prefix}: "{current_line.strip()}"')
            current_prefix = prefix
            current_line = content.strip()

    if current_line:
        current_line = current_line.replace('"', "'") 
        combined_lines.append(f'{current_prefix}: "{current_line.strip()}"')

    Path(output_directory).mkdir(parents=True, exist_ok=True)

    file_name = os.path.basename(file_path)
    output_file_path = os.path.join(output_directory, file_name)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(combined_lines))

    print(f'Combined lines and saved to {output_file_path}')

def combine_lines_in_all_files(input_directory, output_directory):
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                combine_consecutive_lines(file_path, output_directory)

input_directory = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\data\SSSMorphed'
output_directory = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\data\Combined'
combine_lines_in_all_files(input_directory, output_directory)
