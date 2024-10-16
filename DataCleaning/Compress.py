import os

def combine_data_files(input_directory, output_file):
    data_files = []
    for file in os.listdir(input_directory):
        if file.endswith('.txt'):
            data_files.append(os.path.join(input_directory, file))

    combined_lines = []
    for file_path in data_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            combined_lines.extend(lines)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(combined_lines)

input_directory = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\Data\Combined'
output_file = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\Data\Dataset.txt'
combine_data_files(input_directory, output_file)
