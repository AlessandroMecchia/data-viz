# Timestamp
1990-2022

# Data source
FAOSTAT - Pesticides Total:
https://www.fao.org/faostat/en/#data/RP

# Dataset
modified_flourish_long_format_exclude_total.csv
	
# Protocol: Flourish + Python

# Preprocessing steps:
1. Load the Dataset: Read the CSV file (`cleaned_dataset.csv`) into a Pandas DataFrame.  
2. Reshape with Melt: Use the `melt` function to reshape the DataFrame. Keep `Year` as the identifier column (`id_vars`) and transform selected pesticide-related columns (`value_vars`) into a long format with `Pesticide Type` and `Usage` columns.  
3. Filter Rows: Exclude rows where the `Pesticide Type` column equals `'Pesticides (total)'`.  
4. Pivot Data: Transform the long-format DataFrame back into a wide format with `Year` as rows and `Pesticide Type` as columns. Aggregate usage values using the `sum` function.  
5. Save Transformed Data: Write the transformed dataset to a new CSV file (`modified_tableau_long_format_exclude_total.csv`).  
