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

## 🗄️ Data Warehouse Design
To support analytical reporting, a **star schema** is designed.

### 📊 Fact Table: `Crime_Fact`
- Crime_ID  
- Time_Key  
- Location_Key  
- CrimeType_Key  
- Severity  

### 🧱 Dimension Tables

#### `Time_Dim`
- Time_Key  
- Hour  
- Day  
- Weekday / Weekend  

#### `Location_Dim`
- Location_Key  
- Area_Name  
- City  
- Zone  

#### `CrimeType_Dim`
- CrimeType_Key  
- Crime_Type  
- Category  

This schema enables efficient multidimensional analysis of crime data.

---

## 🛠️ Tools and Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- scikit-learn
- CSV files (for data storage and warehouse simulation)

---

## 📈 Results and Visualizations
The following visualizations are generated:
- Crime frequency by location
- Crime occurrence by time of day
- Cluster visualization showing crime hotspots
- Crime severity distribution charts

These visualizations support analytical insights derived from the data.

---

## ✅ Conclusion
This project demonstrates how data mining and data warehousing techniques can be effectively applied to crime data analysis. By identifying crime hotspots, predicting crime severity, and analyzing temporal trends, the project provides meaningful insights that can assist law enforcement agencies and policymakers.

The integration of a data warehouse schema further enables structured and scalable crime data analysis.

---

## 🚀 Future Enhancements
- Incorporate real-time crime data
- Use advanced clustering techniques (DBSCAN, Hierarchical Clustering)
- Add geographical visualizations using maps
- Integrate SQL-based warehouse querying

---

## 📚 References
- scikit-learn Documentation  
- Open Government Crime Data Portals  
- Data Mining and Data Warehousing Textbooks  
