import argparse
import os
import logging
from utils import load_csv_files, ensure_directory_exists, setup_logging
from preprocessing import read_csv_files, create_dialogues
from model_training import train_model

def main(input_folder, output_directory):
    ensure_directory_exists(output_directory)

    log_file = os.path.join(output_directory, 'chatbot.log')
    setup_logging(log_file)

    try:
        logging.info("Reading CSV files")
        csv_files = load_csv_files(input_folder)
        
        data = read_csv_files(csv_files)
        
        logging.info("Creating dialogues")
        dialogues = create_dialogues(data)
        
        logging.info("Training the chatbot model")
        trained_model_path = train_model(dialogues, output_directory)

        logging.info("Chatbot model training completed successfully.")
        logging.info(f"Trained model saved at: {trained_model_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a chatbot model.")
    parser.add_argument('input_folder', type=str, help="Path to the input folder containing CSV files.")
    parser.add_argument('output_directory', type=str, help="Directory to save the trained model.")
    args = parser.parse_args()

    main(args.input_folder, args.output_directory)