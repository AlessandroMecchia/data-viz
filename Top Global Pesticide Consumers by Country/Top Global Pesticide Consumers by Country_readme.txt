# Timestamp
1990-2022

# Data source
FAOSTAT - Pesticides Total:
https://www.fao.org/faostat/en/#data/RP

# Dataset
modified_flourish_wide_format_countries_with_flags.csv
	
# Protocol: Flourish + Python

# Preprocessing steps:
1. Load the Dataset: Read the CSV file (`cleaned_dataset.csv`) into a Pandas DataFrame.  
2. Reshape with Melt: Use the `melt` function to reshape the DataFrame. Include `Area` and `Year` as identifier columns (`id_vars`) and transform selected pesticide-related columns (`value_vars`) into a long format with `Pesticide Type` and `Usage` columns.  
3. Filter Rows: Exclude rows where the `Pesticide Type` column equals `'Pesticides (total)'`.  
4. Harmonize Country Names: Replace `China, mainland` and `Mainland` in the `Area` column with `China`.  
5. Pivot Data: Transform the long-format DataFrame into a wide format with `Area` as rows and `Year` as columns. Aggregate `Usage` values using the `sum` function.  
6. Generate Flag URLs: Create a dictionary mapping country names to their flag URLs using the ISO codes provided.  
7. Map Flag URLs: Add a `Flag URL` column to the DataFrame by mapping the `Area` column to the flag URL dictionary.  
8. Save Transformed Data: Write the transformed dataset with flag URLs to a new CSV file (`modified_tableau_wide_format_countries_with_flags.csv`).  
