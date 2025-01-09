import pandas as pd

# Read the original CSV file
input_file = 'original_merged.csv'  # Input file path
output_file = 'cleaned_dataset.csv'  # Desired output file path

# Load the dataset
df = pd.read_csv(input_file)

# Select only the relevant columns for the transformation
columns_to_keep = ['Area', 'Year', 'Fungicides and Bactericides', 'Herbicides', 'Insecticides',
                   'Other Pesticides nes', 'Pesticides (total)', 'Plant Growth Regulators', 'Rodenticides']

# Filter the dataset to keep only the necessary columns
df_transformed = df[columns_to_keep]

# Save the transformed dataset to a new CSV file
df_transformed.to_csv(output_file, index=False)

print(f"Transformed dataset saved to {output_file}")
