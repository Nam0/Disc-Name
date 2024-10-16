import pandas as pd
import os
import json
import logging

def load_csv_files(directory):
    csv_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                csv_path = os.path.join(root, file)
                data = pd.read_csv(csv_path)
                csv_files.append(data)
    return csv_files

def read_data(file_path):
    """
    Read data from a given file path.
    Supports CSV and JSON file formats.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() == '.csv':
        data = pd.read_csv(file_path)
    elif file_extension.lower() == '.json':
        data = pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and JSON are supported.")
    
    return data

def save_to_csv(data, file_path):
    """
    Save a pandas DataFrame to a CSV file.
    """
    data.to_csv(file_path, index=False)
    logging.info(f"Data saved to {file_path}")

def save_to_json(data, file_path):
    """
    Save a pandas DataFrame to a JSON file.
    """
    data.to_json(file_path, orient='records', lines=True)
    logging.info(f"Data saved to {file_path}")

def ensure_directory_exists(directory):
    """
    Ensure that a directory exists, creating it if necessary.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory {directory}")

def load_processed_data(file_path):
    """
    Load processed data from a JSON file.
    """
    with open(file_path, 'r') as file:
        processed_data = json.load(file)
    return processed_data

def save_processed_data(processed_data, file_path):
    """
    Save processed data to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(processed_data, file, indent=4)
    logging.info(f"Processed data saved to {file_path}")

def setup_logging(log_file):
    """
    Set up logging configuration.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.info("Logging setup complete.")

if __name__ == "__main__":
    setup_logging("data_processing.log")
    file_path = "example_data.csv"
    data = read_data(file_path)
    save_to_csv(data, "output_data.csv")
    save_to_json(data, "output_data.json")
    ensure_directory_exists("processed_data")
    save_processed_data({"example_key": "example_value"}, "processed_data/example_processed_data.json")
    loaded_data = load_processed_data("processed_data/example_processed_data.json")
    print(loaded_data)
