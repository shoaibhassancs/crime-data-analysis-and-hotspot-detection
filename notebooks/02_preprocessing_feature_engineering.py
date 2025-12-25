import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

# -----------------------------
# Load the Dataset
# -----------------------------
df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-raw/karachi_crime_2020_2025.csv')

# -----------------------------
# Handle Missing Values & Duplicates
# -----------------------------
df.isnull().sum() #check missing values
df = df.dropna() #remove rows with missing values
df.duplicated().sum() #check duplicates
df = df.drop_duplicates() # remove duplicates

# -----------------------------
# Correct Data Types
# -----------------------------
df.dtypes

df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d', errors='coerce') # Change DATE from text (object) to a proper datetime format
df['DATE'].dtype

categorical_cols = ['TOWN', 'TOWN_RISK_LEVEL', 'SUBDIVISION', 'SUBDIVISION_RISK_LEVEL', 'CRIME_TYPE', 'SEVERITY', 'RISK_ZONE', 'SOURCE']
df[categorical_cols] = df[categorical_cols].astype('category') # Mark categorical columns as categorical
df.info()

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns # Verify numeric columns
print("Numeric columns:", numeric_cols)

# -----------------------------
# Feature Engineering
# -----------------------------
# Derive temporal features from DATE
df['HOUR'] = df['DATE'].dt.hour
df['DAY_OF_WEEK'] = df['DATE'].dt.dayofweek
df['MONTH'] = df['DATE'].dt.month
df['YEAR'] = df['DATE'].dt.year
df['IS_PEAK_HOUR'] = df['HOUR'].apply(lambda x: 1 if 17 <= x <= 20 else 0) # Define peak hours as 5 PM to 8 PM
df['IS_WEEKEND'] = df['DAY_OF_WEEK'].apply(lambda x: 1 if x >= 5 else 0) # Define weekend as Saturday (5) and Sunday (6)
df[['HOUR', 'DAY_OF_WEEK', 'MONTH', 'YEAR', 'IS_PEAK_HOUR', 'IS_WEEKEND']].head(10)

# save the cleaned dataset
df.to_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/02_01_karachi_crime_2020_2025_cleaned.csv', index=False)

df = df.drop(columns=['INCIDENT_ID', 'SOURCE', 'SEVERITY', 'RISK_ZONE']) # Drop unnecessary columns

df.isnull().sum()
df.describe()

# -----------------------------
# Encode Categorical Variables
# -----------------------------
cat_cols = ['TOWN', 'TOWN_RISK_LEVEL', 'SUBDIVISION', 'SUBDIVISION_RISK_LEVEL', 'CRIME_TYPE']

# Label encoding
le_df = df.copy()
le = LabelEncoder()
for col in cat_cols:
    le_df[col] = le.fit_transform(le_df[col])
le_df.head()

# One-hot encoding (if needed for KMeans clustering)
ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
ohe_encoded = ohe.fit_transform(df[cat_cols])

# Convert the encoded array to a DataFrame
encoded_df = pd.DataFrame(
    ohe_encoded, 
    columns=ohe.get_feature_names_out(cat_cols),
    index=df.index
)
df = df.drop(columns=cat_cols) # Drop original categorical columns
df = pd.concat([df, encoded_df], axis=1) # Concatenate the one-hot encoded columns
df.head()

# -----------------------------
# Scale Numeric Features
# -----------------------------
numeric_cols_to_scale = [
    'TOWN_PRIORITY_RANK', 
    'SUBDIVISION_PRIORITY_RANK', 
    'SEVERITY_SCORE', 
    'LATITUDE', 
    'LONGITUDE'
]

scaler = StandardScaler()
le_df[numeric_cols_to_scale] = scaler.fit_transform(le_df[numeric_cols_to_scale]) # scale label encoded numeric columns
df[numeric_cols_to_scale] = scaler.fit_transform(df[numeric_cols_to_scale]) # scale one-hot encoded numeric columns

# Verify scaling
le_df[numeric_cols_to_scale].mean()
le_df[numeric_cols_to_scale].std()
df[numeric_cols_to_scale].mean()
df[numeric_cols_to_scale].std()

# -----------------------------
# Save Preprocessed Dataset
# -----------------------------
df.to_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/02_02_karachi_crime_2020_2025_label_encoded.csv', index=False)
le_df.to_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/02_03_karachi_crime_2020_2025_label_encoded.csv', index=False)