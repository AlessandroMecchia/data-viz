# **Mr. Pesticide: Understanding His Role in Global Trade and Agriculture**

## **Project Description**
This project explores the role of **pesticides** in agriculture and their impact on global trade. It provides an informative and interactive webpage that highlights:
- What pesticides are and how they work.
- Their importance in protecting crops from pests, diseases, and weeds.
- Their role in ensuring global food security and enhancing agricultural productivity.

### Preprocessing
1. Load the dataset: Read the original CSV file (`original_merged.csv`) into a Pandas DataFrame.  
2. Select relevant columns: Identify and keep only the necessary columns: `Area`, `Year`, `Fungicides and Bactericides`, `Herbicides`, `Insecticides`, `Other Pesticides nes`, `Pesticides (total)`, `Plant Growth Regulators`, and `Rodenticides`.  
3. Filter the dataset: Remove all columns not listed in the `columns_to_keep` list to retain only relevant data.  
4. Save the transformed dataset: Write the filtered dataset to a new CSV file (`cleaned_dataset.csv`).  

### Top Global Pesticide Consumers by Continent
1. Load the dataset: Read the CSV file (`modified_tableau_wide_format_countries_with_flags.csv`) into a Pandas DataFrame.  
2. Map countries to continents: Create a new `Continent` column by mapping country names in the `Area` column to their corresponding continent using the `country_to_continent` dictionary.  
3. Drop missing mappings: Remove rows where the `Continent` mapping is missing (i.e., `NaN` in the `Continent` column).  
4. Aggregate data by continent: Group the dataset by the `Continent` column and sum all numeric columns.  
5. Save the transformed dataset: Write the aggregated dataset to a new CSV file at the specified output path.  

### Top Global Pesticide Consumers by Country
1. Load the Dataset: Read the CSV file (`cleaned_dataset.csv`) into a Pandas DataFrame.  
2. Reshape with Melt: Use the `melt` function to reshape the DataFrame. Include `Area` and `Year` as identifier columns (`id_vars`) and transform selected pesticide-related columns (`value_vars`) into a long format with `Pesticide Type` and `Usage` columns.  
3. Filter Rows: Exclude rows where the `Pesticide Type` column equals `'Pesticides (total)'`.  
4. Harmonize Country Names: Replace `China, mainland` and `Mainland` in the `Area` column with `China`.  
5. Pivot Data: Transform the long-format DataFrame into a wide format with `Area` as rows and `Year` as columns. Aggregate `Usage` values using the `sum` function.  
6. Generate Flag URLs: Create a dictionary mapping country names to their flag URLs using the ISO codes provided.  
7. Map Flag URLs: Add a `Flag URL` column to the DataFrame by mapping the `Area` column to the flag URL dictionary.  
8. Save Transformed Data: Write the transformed dataset with flag URLs to a new CSV file (`modified_tableau_wide_format_countries_with_flags.csv`).  

### Trends in Global Pesticide Usage by Type
1. Load the Dataset: Read the CSV file (`cleaned_dataset.csv`) into a Pandas DataFrame.  
2. Reshape with Melt: Use the `melt` function to reshape the DataFrame. Keep `Year` as the identifier column (`id_vars`) and transform selected pesticide-related columns (`value_vars`) into a long format with `Pesticide Type` and `Usage` columns.  
3. Filter Rows: Exclude rows where the `Pesticide Type` column equals `'Pesticides (total)'`.  
4. Pivot Data: Transform the long-format DataFrame back into a wide format with `Year` as rows and `Pesticide Type` as columns. Aggregate usage values using the `sum` function.  
5. Save Transformed Data: Write the transformed dataset to a new CSV file (`modified_tableau_long_format_exclude_total.csv`).  

---

## **Project Structure**
The project includes the following components:

### **1. HTML**
- The main structure of the webpage is in `index.html`.
- Key sections:
   - Titles and subtitles introducing the theme.
   - Informative content with highlighted keywords.
   - Images and captions for better understanding.

### **2. CSS**
- Custom styling to ensure a clean, responsive, and visually appealing design.
- Key features:
   - Background images and color themes.
   - Responsive layout optimized for desktop and mobile devices.
   - Hover effects for interactivity.

### **3. Assets**
- Images and other static resources are stored in the `assets/` folder.

### **4. Data Preprocessing Scripts**
- Located in the `preprocessing/` folder:
  - `dataset_cleaner.py`: Script for cleaning and preprocessing raw datasets.
  - `extract_countries.py`: Script for mapping all the countries


# Data visualization course
SUPSI  
Bachelor in Data Science and Artificial Intelligence
Teacher: Giovanni Profeta
https://dataviz-supsi.github.io/2024/

