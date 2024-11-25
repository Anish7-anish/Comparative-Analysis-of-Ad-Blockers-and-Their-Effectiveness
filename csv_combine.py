import pandas as pd
import glob
import os

# Specify the pattern to match your CSV files
csv_files = glob.glob('adblocker_effectiveness_no_extension_*.csv')

# List to hold individual DataFrames
dataframes = []

for file in csv_files:
    # Read each CSV file into a DataFrame
    df = pd.read_csv(file)
    
    # Extract the adblock_name from the filename
    filename = os.path.basename(file)
    name_without_extension = os.path.splitext(filename)[0]
    
    # Extract only the name of the adblocker ('adblock_plus' in this case)
    if 'no_extension' in name_without_extension:
        adblock_name = 'no_adblocker' # change the name
    else:
        adblock_name = name_without_extension.replace('adblocker_', '')
    
    # Add the adblock_name column
    df['adblock_name'] = adblock_name
    
    # Append the DataFrame to the list
    dataframes.append(df)

# Combine all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Display the combined DataFrame
print(combined_df)

# Optionally, save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_no_adblocker__data.csv', index=False)
