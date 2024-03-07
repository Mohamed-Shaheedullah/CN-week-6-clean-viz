import pandas as pd

# List of file paths
file_paths = [
    "DAY5/megabytes_data/megabytes/sunday_graph.xlsx",
    "DAY5/megabytes_data/megabytes/monday_graph.xlsx",
    # Add more file paths as needed
]

# Define an empty DataFrame to store the results
total_payments_all = pd.DataFrame()

# Loop through each file path
for file_path in file_paths:
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Drop unnecessary columns and rows
    df = df.drop(columns=["Unnamed: 0"])
    df = df.drop([0])
    df = df.dropna(how="any")
    
    # Group by 'Payment Method' and sum the 'Cost'
    total_payments = df.groupby('Payment Method')['Cost'].sum().reset_index()
    
    # Add the file name as a column
    file_name = file_path.split("/")[-1]  # Extracting file name from path
    total_payments['File'] = file_name