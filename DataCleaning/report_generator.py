import pandas as pd
import csv

def generate_text_report(processed_data, output_file):
    """
    Generate a text report summarizing the processed data.
    """
    with open(output_file, 'w') as f:
        for i, data in enumerate(processed_data):
            f.write(f"Report for Dataset {i + 1}\n")
            f.write("Cleaned Data Head:\n")
            f.write(f"{data['cleaned'].head()}\n\n")
            
            f.write("Aggregated Data:\n")
            for key, value in data['aggregated'].items():
                f.write(f"{key.capitalize()}:\n{value}\n\n")
            
            f.write("Top 5 Most Frequent Values in 'value' Column:\n")
            f.write(f"{data['analyzed']}\n\n")
            f.write("="*50 + "\n\n")

def generate_csv_report(processed_data, output_file_prefix):
    """
    Generate a CSV report for the processed data.
    """
    for i, data in enumerate(processed_data):
        cleaned_output_file = f"{output_file_prefix}_cleaned_{i + 1}.csv"
        data['cleaned'].to_csv(cleaned_output_file, index=False)
        
        aggregated_output_file = f"{output_file_prefix}_aggregated_{i + 1}.csv"
        with open(aggregated_output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Metric', 'Value'])
            for key, value in data['aggregated'].items():
                if isinstance(value, pd.Series):
                    for sub_key, sub_value in value.items():
                        writer.writerow([f"{key}_{sub_key}", sub_value])
                else:
                    writer.writerow([key, value])
        
        analyzed_output_file = f"{output_file_prefix}_analyzed_{i + 1}.csv"
        data['analyzed'].to_csv(analyzed_output_file, header=True)

def generate_reports(processed_data, text_output_file, csv_output_file_prefix):
    """
    Generate all reports (text and CSV) for the processed data.
    """
    generate_text_report(processed_data, text_output_file)
    generate_csv_report(processed_data, csv_output_file_prefix)

if __name__ == "__main__":
    processed_data = [
        {
            'cleaned': pd.DataFrame({
                'value': [1, 2, 3, 4, 5],
                'other_column': [10, 20, 30, 40, 50]
            }),
            'aggregated': {
                'mean': pd.Series({'value': 3, 'other_column': 30}),
                'median': pd.Series({'value': 3, 'other_column': 30}),
                'sum': pd.Series({'value': 15, 'other_column': 150})
            },
            'analyzed': pd.Series({'1': 1, '2': 1, '3': 1, '4': 1, '5': 1})
        }
    ]

    text_output_file = "data_report.txt"
    csv_output_file_prefix = "data_report"

    generate_reports(processed_data, text_output_file, csv_output_file_prefix)
