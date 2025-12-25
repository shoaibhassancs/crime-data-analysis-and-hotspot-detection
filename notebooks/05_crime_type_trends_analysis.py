import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/02_01_karachi_crime_2020_2025_cleaned.csv')

# -----------------------------
# Prepare the Dataset (Temporal Features)
# -----------------------------
"""
categorical_cols = ['TOWN', 'TOWN_RISK_LEVEL', 'SUBDIVISION', 'SUBDIVISION_RISK_LEVEL', 'CRIME_TYPE', 'SEVERITY', 'RISK_ZONE', 'SOURCE']
df[categorical_cols] = df[categorical_cols].astype('category') # Mark categorical columns as categorical
df.info()
"""

# Change DATE from object to datetime
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d', errors='coerce')

# Derive temporal features from DATE
# df['HOUR'] = df['DATE'].dt.hour
df['DAY_OF_WEEK'] = df['DATE'].dt.dayofweek
df['MONTH'] = df['DATE'].dt.month
df['YEAR'] = df['DATE'].dt.year
df['IS_PEAK_HOUR'] = df['HOUR'].apply(lambda x: 1 if 17 <= x <= 20 else 0) # Define peak hours as 5 PM to 8 PM
df['IS_WEEKEND'] = df['DAY_OF_WEEK'].apply(lambda x: 1 if x >= 5 else 0) # Define weekend as Saturday (5) and Sunday (6)
df[
    ['HOUR', 'DAY_OF_WEEK', 'MONTH', 'YEAR', 'IS_PEAK_HOUR', 'IS_WEEKEND']
].head(10)
df.dtypes

# -----------------------------
# Overall Crime Frequency Over Time
# -----------------------------
"""
# Crime count by hour
crime_by_hour = (
    df.groupby('HOUR')
    .size() # Counts the number of rows in each group
    .reset_index(name='CRIME_COUNT_BY_HOUR') # Converts the grouped index (DAY_OF_WEEK) back into a normal column 
)
crime_by_hour
"""

# Crime count by day of week
crime_by_day = (
    df.groupby('DAY_OF_WEEK') # # Group data by DAY OF THE WEEK
    .size() # Count number of crimes in each group
    .reset_index(name='CRIME_COUNT') # Convert Series to DataFrame with column 'CRIME_COUNT'
)
# Map numeric day codes to names
day_mapping = {
    0: 'Monday', 
    1: 'Tuesday', 
    2: 'Wednesday', 
    3: 'Thursday', 
    4: 'Friday', 
    5: 'Saturday', 
    6: 'Sunday'
}
crime_by_day['DAY_NAME'] = crime_by_day['DAY_OF_WEEK'].map(day_mapping)
crime_by_day[['DAY_NAME', 'CRIME_COUNT']]

"""
# Aggregate crime frequency by day of week and hour
day_hour_counts = (
    df.groupby(['DAY_OF_WEEK', 'HOUR']).size().reset_index(name='CRIME_COUNT')
)
print(day_hour_counts)
"""

# Crime count by month
crime_by_month = (
    df.groupby('MONTH').size().reset_index(name='CRIME_COUNT')
)
crime_by_month

# Crime count by year
crime_by_year = (
    df.groupby('YEAR').size().reset_index(name='CRIME_COUNT')
)
crime_by_year

# Aggregate crime frequency by month and year
crime_by_month_year = (
    df.groupby(['YEAR', 'MONTH']).size().reset_index(name='CRIME_COUNT')
)

# Create a datetime for plotting
crime_by_month_year['YEAR_MONTH'] = pd.to_datetime(
    crime_by_month_year['YEAR'].astype(str) + '/' + crime_by_month_year['MONTH'].astype(str) + '-01'
)
# Creates a 2D matrix (12×n_years) where each cell = # crimes in that month/year
heatmap_data = crime_by_month_year.pivot(
    index='MONTH', # rows = months 1–12
    columns='YEAR', # columns = years (2020-2025)
    values='CRIME_COUNT' # values = crime counts
).fillna(0) # replace missing values with 0

# Crime count by crime type
crime_by_crime_type = (
    df.groupby('CRIME_TYPE').size().reset_index(name='CRIME_COUNT') # .sort_values(by='CRIME_COUNT', ascending=False)
)
crime_by_crime_type

# -----------------------------
# Visualize 
# -----------------------------
# Function for plotting and saving
def plot_and_save(df, category_col, value_col, kind, title, xlabel, ylabel, filename, figsize=(10,6), xticks=None, xtick_rotation=45):
    plt.figure(figsize=figsize)

    # pandas plotting
    df.plot(
        x=category_col,
        y=value_col,
        kind=kind,
        legend=False,   # hide legend for single series
        ax=plt.gca()    # current axes
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    if xticks is not None:
        plt.xticks(ticks=xticks, rotation=xtick_rotation, horizontalalignment='right')
    else:
        plt.xticks(rotation=xtick_rotation, horizontalalignment='right')

    plt.tight_layout()
    
    # Save figure
    plt.savefig(f'/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/visuals/{filename}', bbox_inches='tight')
    plt.show()

# Day of the week
plot_and_save(
    crime_by_day,
    category_col='DAY_NAME',
    value_col='CRIME_COUNT',
    kind='bar',
    title='Crime Frequency by Day of the Week',
    xlabel='Day of the Week',
    ylabel='Number of Crimes',
    filename='05_01_crime_by_day_of_the_week.png'
)

# Monthly
plot_and_save(
    crime_by_month,
    'MONTH',
    'CRIME_COUNT',
    'line',
    'Monthly Crime Trend',
    'Month',
    'Number of Crimes',
    '05_02_crime_by_month.png',
    xticks=range(1,13),
    xtick_rotation=0
)

# Yearly
plot_and_save(
    crime_by_year, 
    'YEAR', 
    'CRIME_COUNT', 
    'line', 
    'Yearly Crime Trend', 
    'YEAR', 
    'Number of Crimes', 
    '05_03_crime_by_year.png',
    xtick_rotation=0
)

# Month_year
plt.figure(figsize=(12,6))
sns.heatmap(
    heatmap_data,          # the pivoted data
    annot=True,            # show numbers in cells
    fmt='g',               # integer format
    cmap='YlOrRd'          # color map (yellow → red)
)
plt.title('Crime Frequency Heatmap: Month vs Year')
plt.xlabel('Year')
plt.ylabel('Month')
plt.savefig('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/visuals/05_04_crime_by_month_year.png')
plt.show()

# Top Crime Types
crime_by_crime_type_sorted = crime_by_crime_type.sort_values(by='CRIME_COUNT', ascending=True)
plot_and_save(
    crime_by_crime_type_sorted, 
    'CRIME_TYPE', 
    'CRIME_COUNT', 
    'barh', 
    'Top Crime Types', 
    'Crime Type', 
    'Number of Crimes', 
    '05_05_top_crime_types', 
    xtick_rotation=0,
)