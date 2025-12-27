# Crime Data Analysis & Hotspot Detection

## Project Overview
Crime analysis plays a vital role in public safety and urban planning. With the increasing availability of crime-related data, data mining techniques can be applied to uncover hidden patterns, crime hotspots, and temporal trends.

This project focuses on analyzing crime data to:
- Identify crime-prone areas (hotspots)
- Analyze time-based crime patterns
- Predict crime severity levels

The project integrates **Data Mining techniques** (clustering, classification, trend analysis) with **Data Warehousing concepts** (fact and dimension tables, star schema design) using Python-based tools.

---

## Problem Statement
The objectives of this project are to:
- Identify crime hotspots based on location and time
- Classify crime incidents based on severity levels
- Analyze trends in crime occurrences over time
- Design a data warehouse schema to support multidimensional crime analysis

---

## Dataset Description
Each record in the dataset represents a single reported crime incident in Karachi. The dataset, karachi_crime_2020_2025, is obtained from Kaggle and covers crimes reported between 2020 and 2025. It captures spatial, temporal, and severity information of various crime incidents, suitable for academic purposes, exploratory data analysis, and predictive modeling.

## Features Used
**Incident Type**: Type of crime (e.g., theft, robbery, assault)
**Geographical Location**: Area where the incident occurred (town, subdivision, latitude, longitude)
**Temporal Attributes**:
Date of occurrence
Time of occurrence (hour)
Day of the week
**Severity Score**: Numeric score representing the seriousness of the crime
**Zone Indicators**: Binary flags representing crime zones (Red, Orange, Yellow, Green, White)
**Priority & Rank Metrics**:
Town priority rank
Subdivision priority rank
Overall crime rank

---

## Data Preprocessing & Feature Engineering
Before analysis and modeling, the following preprocessing steps are applied:
**Data Cleaning**: Handling missing or invalid values and removing duplicate records.
**Data Type Optimization**: Converting date fields to datetime format, casting categorical attributes to categorical type.
**Categorical Feature Encoding**: Encoding incident type, location, and temporal categories for machine learning models.
**Numerical Feature Processing**: Scaling and normalization of numeric attributes (e.g., severity score, priority ranks).
**Feature Engineering**: Deriving temporal features from the date column (year, month, day of the week, peak/off-peak hours, weekend/weekday), and creating binary zone indicators for hotspot analysis.

These steps ensure data consistency, realism in synthetic patterns, and improved performance of crime pattern analysis and hotspot detection models.

---

## Data Mining Techniques

### Clustering – Crime Hotspot Detection
Clustering is used to identify crime hotspots without predefined labels.

- **Algorithm Used**: K-Means Clustering
- **Features Used for Clustering**:
  - Location (Latitude, Longitude)

**Outcome**:
- Identification of high-crime zones (hotspots)
- Ranking clusters by crime intensity
- Linking clusters to towns/subdivisions for actionable insights

---

### Classification – Crime Severity Prediction
Classification is used to predict whether a crime incident is of high, medium, or low severity.

- **Target Variable**: SEVERITY (High / Medium / Low)
- **Algorithms Used**: Random Forest Classifier (with class balancing to handle class imbalance)
- **Features Used**:
  -  Location: LATITUDE, LONGITUDE
  -  Crime details: CRIME_TYPE, TOWN, SUBDIVISION
  -  Temporal: HOUR, DAY_OF_WEEK, MONTH, IS_PEAK_HOUR, IS_WEEKEND
- **Evaluation Metrics**:
  - Accuracy (~86%)
  - Confusion Matrix
  - Classification Report (Precision, Recall, F1-score)

**Insights**:
  - Random Forest identified which features most influence severity.
  - Model performs well across all classes, enabling prioritization of high-severity crimes.

---

### Trend Mining
Trend analysis was performed to uncover temporal crime patterns:
- **Crime Frequency by Day of the Week**: Revealed which weekdays have higher incidents.
- **Monthly Crime Trends**: Identified seasonal patterns within each year.
- **Yearly Crime Trends**: highlighted increasing or decreasing trends over the years.
- **Month vs Year Heatmap**: → provided a detailed view of crime distribution across.
- **Top Crime Types**: highlighted the most frequent crimes in Karachi.

These insights help authorities prioritize interventions based on both **time** and **crime type**.

---

## Data Warehouse Design
To support analytical reporting and multidimensional analysis, a star schema–based data warehouse is designed and implemented using PostgreSQL (Supabase).

### Fact Table: `Crime_Fact`
Stores measurable crime events and links to dimension tables.
- Crime_Fact_ID
- Time_ID
- Location_ID
- CrimeType_ID
- severity_score
- is_peak_hour
- is_weekend
- zone_indicator
- cluster_label (reserved for ML hotspot linkage)

### Dimension Tables

#### `Time_Dim`
Captures temporal attributes for trend analysis.
- Time_ID
- date
- hour
- day_of_week
- month
- year
- is_peak_hour
- is_weekend

#### `Location_Dim`
Stores spatial and administrative location details.
- Location_ID
- town
- subdivision
- latitude
- longitude
- risk_zone

#### `CrimeType_Dim`
Defines crime categories and severity labels.
- CrimeType_ID
- crime_type
- severity

This schema enables efficient slice-and-dice analysis across time, location, crime type, and severity.

---

## Tools and Technologies Used
- Python (Pandas, NumPy)
- Machine Learning (scikit-learn: K-Means, Random Forest)
- Data Visualization (Matplotlib)
- PostgreSQL (Supabase)
- SQL (Star Schema, Views, Aggregations)
- Git & GitHub

---

## Results and Visualizations
The project generates analytical insights through:
- Monthly crime trends by severity
- Top towns with high-severity crimes
- Peak vs non-peak hour crime analysis
- Crime hotspot detection using spatial clustering
- Feature importance analysis for crime severity prediction

These visualizations and SQL views support data-driven decision-making and crime pattern analysis.

---

## Conclusion
This project demonstrates the practical application of data mining and data warehousing techniques on real-world–style crime data. By combining machine learning models with a structured PostgreSQL data warehouse, the system enables:
- Identification of crime hotspots
- Prediction of crime severity levels
- Temporal and spatial trend analysis

The warehouse design ensures scalability, structured querying, and reproducible analytics.

---

## Future Enhancements
- Populate and analyze cluster_label directly within the warehouse
- Integrate interactive dashboards (Streamlit / Plotly)
- Apply advanced clustering techniques (DBSCAN, HDBSCAN)
- Add geospatial visualizations using maps
- Incorporate real-time or streaming crime data

---

## References
- scikit-learn Documentation  
- PostgreSQL & Supabase Documentation
- Data Mining and Data Warehousing textbooks
