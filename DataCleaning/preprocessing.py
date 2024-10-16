import pandas as pd

def read_csv_files(file_paths):
    all_data = pd.concat([pd.read_csv(file_path) for file_path in file_paths])
    return all_data[['AuthorID', 'Author', 'Date', 'Content', 'Attachments', 'Reactions']]

def create_dialogues(data):
    dialogues = []
    current_dialogue = []
    prev_author = None

    for index, row in data.iterrows():
        author = row['Author']
        content = row['Content']

        if author != prev_author and prev_author is not None:
            dialogues.append(current_dialogue)
            current_dialogue = []

        current_dialogue.append(content)
        prev_author = author

    dialogues.append(current_dialogue)

    return dialogues
