import pandas as pd

def clean_data(df):
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Handle missing values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")
        else:
            df[column] = df[column].fillna(0)

    return df