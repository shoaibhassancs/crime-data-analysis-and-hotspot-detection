import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-raw/karachi_crime_2020_2025.csv')

# First few rows
df.head()
df.info()

# Check distribution of categorical columns
df['SEVERITY'].value_counts()
df['CRIME_TYPE'].value_counts() 
df['TOWN'].value_counts()
df['SUBDIVISION'].value_counts()

# Summary statistics for numerical columns
df[['SEVERITY_SCORE','LATITUDE','LONGITUDE']].describe()

# Function to plot and save bar charts
def plot_and_save(series, title, xlabel, ylabel, filename, top_n=None, figsize=(12,6)):
    data = series.value_counts()
    if top_n:
        data = data.head(top_n)
    plt.figure(figsize=figsize)
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.tight_layout()
    plt.savefig(f'/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/visuals/{filename}', bbox_inches='tight')
    plt.show()

# Plotting
plot_and_save(df['SEVERITY'], 'Severity Distribution', 'Severity', 'Count', 'severity_distribution.png', figsize=(8,6))

plot_and_save(df['CRIME_TYPE'], 'Crime Type Distribution', 'Crime Type', 'Count', 'crime_type_distribution.png', figsize=(12,6))

plot_and_save(df['TOWN'], 'Crime Distribution by Town', 'Town', 'Number of Crimes', 'crime_by_town.png')

plot_and_save(df['SUBDIVISION'], 'Top 20 Subdivisions by Crime Count', 'Subdivision', 'Number of Crimes', 'crime_by_subdivision.png', top_n=20)
