# Netflix Data Cleaning 🧹

This project focuses on **cleaning and preprocessing** the Netflix Movies and TV Shows dataset using Python and Pandas.

## 🗂 Dataset

- **Source**: [Kaggle - Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Original file**: `netflix_titles.csv`
- **Cleaned file**: `netflix_cleaned.csv`

## 🧼 Cleaning Steps Performed

- Loaded the dataset using `pandas.read_csv()`
- Filled missing values:
  - `director` → `'Unknown'`
  - `cast` → `'Not Available'`
  - `country` → `'Unknown'`
- Dropped rows where `date_added` was missing
- Removed duplicate rows
- Standardized:
  - `type` → lowercase
  - `rating` → uppercase
  - Trimmed spaces from `date_added`
- Converted `date_added` column to datetime format
- Renamed all column headers to lowercase with underscores
- Saved cleaned data as `netflix_cleaned.csv`

## 🛠 Tools Used

- Python
- Pandas
- PyCharm
- Excel

## 🔚 Output

A clean and analysis-ready dataset that can now be used for:
- Visualizations (Power BI, Excel, etc.)
- Modeling
- Insights generation

## 🔗 Author

- Gummana Lohitha  
- [LinkedIn Profile](https://www.linkedin.com/in/lohitha-gummana-630958314)
