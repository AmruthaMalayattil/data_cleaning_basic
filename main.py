import pandas as pd
import re
import os # Import the os module for good practice, though not strictly needed here

def csv_clean(input_filename, header_names, output_filepath):
    df = pd.read_csv(input_filename, skiprows=1, skipfooter=1, header=None, engine='python')
    df.columns = header_names

    for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()

    df.to_csv(output_filepath, index=False)
    # Clean 'Amount' column specifically: remove non-numeric chars (except dot), then convert to numeric
    if 'amt' in df.columns:
            # Remove any characters that are not digits or a decimal point
        df['amt'] = df['amt'].astype(str).str.replace(r'[^\d.]', '', regex=True)
            # Convert to numeric. 'coerce' will turn non-convertible values into NaN
        df['amt'] = pd.to_numeric(df['amt'], errors='coerce')
            # Fill any NaN values that resulted from conversion errors with 0, or drop rows
        df['amt'] = df['amt'].fillna(0) # Or df.dropna(subset=['Amount'], inplace=True)

        filtered_df = df.loc[df['iss'] == 'RELM']

        total_amount = filtered_df['amt'].sum()
        print(f"\nCalculated Total Amount: {total_amount:.2f}")
    else:
        print("Warning: 'amt' column not found for sum calculation.")



    

# 2. Define the input and output filenames
# These are just the filenames, as they are in the same directory as your script.
input_file = "unclean_data.csv"
output_file = "clean.csv"


new_headers = ['slno','acq','iss','amt','date_of_settlement']
csv_clean(input_file, new_headers, output_file)

