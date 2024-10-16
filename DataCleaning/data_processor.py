import pandas as pd

def clean_data(df):
    """
    Clean the data by handling missing values and ensuring correct data types.
    """
    df.fillna(0, inplace=True)  
    
    for column in df.select_dtypes(include=['object']).columns:
        try:
            df[column] = pd.to_numeric(df[column])
        except ValueError:
            pass  
    return df

def aggregate_data(df):
    """
    Aggregate data to compute basic statistics.
    """
    summary = {
        'mean': df.mean(),
        'median': df.median(),
        'sum': df.sum()
    }
    return summary

def analyze_data(df):
    """
    Analyze the data to extract meaningful insights.
    """
    
    if 'value' in df.columns:
        top_values = df['value'].value_counts().head(5)
    else:
        top_values = pd.Series([])  

    return top_values

def process_data(data):
    """
    Process the data by cleaning, aggregating, and analyzing it.
    """
    processed_data = []

    for df in data:
        cleaned_df = clean_data(df)

        aggregated_data = aggregate_data(cleaned_df)

        analyzed_data = analyze_data(cleaned_df)

        processed_data.append({
            'cleaned': cleaned_df,
            'aggregated': aggregated_data,
            'analyzed': analyzed_data
        })
    
    return processed_data
