# data_cleaning_basic

Data Cleaning and Analysis Task
You have a file named unclean_data.csv with comma-separated values, currently lacking headers and containing potential formatting inconsistencies. The data looks like this:

1, NAB, CBA,0004563.56,20250607
23, DFR,ADFC,0003421.45,20250608

Your task involves two main parts: cleaning this data and then performing a specific analysis.

Part 1: Clean the Data
Please perform the following steps to clean unclean_data.csv and save it as clean.csv:

Remove "HEAD" and "TAIL" entries: If these literal strings appear as rows in the file, they should be deleted.

Add Headers: Insert the following headers as the first row in the clean.csv file: slno,acq,iss,amt,date_of_settlement.

Format as Proper CSV: Ensure all fields are properly delimited by commas. This includes trimming any leading or trailing whitespace from the data fields and removing any extraneous characters that would prevent it from being a standard CSV file.

Part 2: Analyze the Cleaned Data
Once clean.csv is ready, read its contents and calculate the total amount (amt) for all rows where the iss (issuer) field is "RELM". 