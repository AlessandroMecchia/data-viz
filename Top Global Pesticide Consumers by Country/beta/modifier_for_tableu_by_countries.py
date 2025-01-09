import pandas as pd

# Read the original CSV file
input_file = "/home/fjg/raspnas/universitá/data_visualization/final_group_project/simple_dataset.csv"  # Input file path
output_file = 'modified_tableau_wide_format_countries.csv'  # Desired output file path

# Load the dataset
df = pd.read_csv(input_file)

# Melt the DataFrame to reshape it first
df_melted = df.melt(id_vars=['Area', 'Year'],  # Include 'Area' for countries
                    value_vars=['Fungicides and Bactericides', 'Herbicides', 'Insecticides', 
                                'Other Pesticides nes', 'Pesticides (total)', 
                                'Plant Growth Regulators', 'Rodenticides'],
                    var_name='Pesticide Type', 
                    value_name='Usage')

# Filter out the 'Pesticides (total)' row
df_melted = df_melted[df_melted['Pesticide Type'] != 'Pesticides (total)']

# Pivot the melted DataFrame to get countries as rows and years as columns
df_pivot = df_melted.pivot_table(index='Area',  # Set countries as rows
                                   columns='Year', 
                                   values='Usage', 
                                   aggfunc='sum').reset_index()

# Save the modified dataset to a new CSV file
df_pivot.to_csv(output_file, index=False)

print(f"Wide-format dataset with countries as rows saved to {output_file}")
