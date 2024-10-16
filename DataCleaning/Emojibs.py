import re

def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  
        "\U0001F300-\U0001F5FF"  
        "\U0001F680-\U0001F6FF"  
        "\U0001F1E0-\U0001F1FF" 
        "\U00002702-\U000027B0" 
        "\U000024C2-\U0001F251" 
        "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)

def remove_emojis_from_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    text_without_emojis = remove_emojis(text)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text_without_emojis)


if __name__ == "__main__":
    input_file = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\Dataset.txt'
    output_file = r'C:\Users\Namo\Documents\GitHub\Disc-Name\New\Dataset2.txt'
    remove_emojis_from_file(input_file, output_file)
    print(f'Emojis removed. Check the output file: {output_file}')
