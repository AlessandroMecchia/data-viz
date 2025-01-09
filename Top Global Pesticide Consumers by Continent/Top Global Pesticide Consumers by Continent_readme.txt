# Timestamp
1990-2022

# Data source
FAOSTAT - Pesticides Total:
https://www.fao.org/faostat/en/#data/RP

# Dataset
modified_flourish_wide_format_countries_with_flags.csv
	
# Protocol: Flourish + Python

# Preprocessing steps:

1. Load the dataset: Read the CSV file (`modified_tableau_wide_format_countries_with_flags.csv`) into a Pandas DataFrame.  
2. Map countries to continents: Create a new `Continent` column by mapping country names in the `Area` column to their corresponding continent using the `country_to_continent` dictionary.  
3. Drop missing mappings: Remove rows where the `Continent` mapping is missing (i.e., `NaN` in the `Continent` column).  
4. Aggregate data by continent: Group the dataset by the `Continent` column and sum all numeric columns.  
5. Save the transformed dataset: Write the aggregated dataset to a new CSV file at the specified output path.  

