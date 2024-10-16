import re

input_file_path = "C:/Users/Namo/Documents/GitHub/Disc-Name/New/Data/Dataset2.txt"
output_file_path = "C:/Users/Namo/Documents/GitHub/Disc-Name/New/Data/Dataset3.txt"

def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  
        "\U0001F300-\U0001F5FF"  
        "\U0001F680-\U0001F6FF"  
        "\U0001F700-\U0001F77F"  
        "\U0001F780-\U0001F7FF"  
        "\U0001F800-\U0001F8FF"  
        "\U0001F900-\U0001F9FF"  
        "\U0001FA00-\U0001FA6F"  
        "\U0001FA70-\U0001FAFF"  
        "\U00002702-\U000027B0"  
        "\U000024C2-\U0001F251" 
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r'', text)


converted_lines = []


with open(input_file_path, "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()
    
    for line in lines:
        if line.startswith("Prompt:"):
            prompt = line.replace("Prompt:", "").strip()
            prompt = remove_emojis(prompt)
            converted_lines.append(f"MESSAGE user {prompt} {prompt} {prompt}\n")
        elif line.startswith("Response:"):
            response = line.replace("Response:", "").strip()
            response = remove_emojis(response)
            converted_lines.append(f"MESSAGE assistant {response} {response} {response}\n")


with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.writelines(converted_lines)

print(f"Converted dataset saved to {output_file_path}")