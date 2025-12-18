import pandas as pd

# 1. Load Dataset
df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-raw/karachi_crime_2020_2025.csv')
df.head()

# 2. Handle Missing Values & Duplicates
df.isnull().sum() #check missing values
df.duplicated().sum() #check duplicates

# 3. Correct Data Types
df.dtypes

df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d', errors='coerce') # Change DATE from text (object) to a proper datetime format
df['DATE'].dtype

categorical_cols = ['TOWN', 'TOWN_RISK_LEVEL', 'SUBDIVISION', 'SUBDIVISION_RISK_LEVEL', 'CRIME_TYPE', 'SEVERITY', 'RISK_ZONE', 'SOURCE']
df[categorical_cols] = df[categorical_cols].astype('category') # Mark categorical columns as categorical
df.info()

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns # Verify numeric columns
print("Numeric columns:", numeric_cols)

# 4. Feature Engineering
# Derive temporal features from DATE
df['HOUR'] = df['DATE'].dt.hour
df['DAY_OF_WEEK'] = df['DATE'].dt.dayofweek
df['MONTH'] = df['DATE'].dt.month
df['YEAR'] = df['DATE'].dt.year
df['IS_PEAK_HOUR'] = df['HOUR'].apply(lambda x: 1 if 17 <= x <= 20 else 0) # Define peak hours as 5 PM to 8 PM
df['IS_WEEKEND'] = df['DAY_OF_WEEK'].apply(lambda x: 1 if x >= 5 else 0) # Define weekend as Saturday (5) and Sunday (6)
df[['HOUR', 'DAY_OF_WEEK', 'MONTH', 'YEAR', 'IS_PEAK_HOUR', 'IS_WEEKEND']].head(10)

df = df.drop(columns=['INCIDENT_ID', 'SOURCE', 'SEVERITY', 'RISK_ZONE']) # Drop unnecessary columns

df.isnull().sum()
df.describe()

# 5. Encode Categorical Variables
# 6. Scale Numeric Features
# 7. Save Preprocessed Dataset
# 8. Quick Visual Checks
