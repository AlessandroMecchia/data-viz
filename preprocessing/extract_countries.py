import pandas as pd

# Load the dataset
input_file = "/home/fjg/raspnas/universitá/data_visualization/final_group_project/simple_dataset.csv"  # Replace with your actual file path
df = pd.read_csv(input_file)

# Extract unique country names from the 'Area' column
unique_countries = df['Area'].unique()

# Print unique countries
countries_list = []
for country in unique_countries:
    countries_list.append((country, ''))  # Add an empty string for the ISO code for now

# Output the extracted country names
for country in countries_list:
    print(country)

# Create the flag mapping placeholder
flag_mapping = {}
for country, code in countries_list:
    # Assuming code is provided or will be filled in later
    flag_mapping[country] = f'https://public.flourish.studio/country-flags/svg/{code}.svg' if code else 'URL not available'

# Print the flag mapping
for country, url in flag_mapping.items():
    print(f"{country}")
