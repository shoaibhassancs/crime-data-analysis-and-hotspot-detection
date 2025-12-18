# Crime Data Analysis & Hotspot Detection

## 📌 Project Overview
Crime analysis plays a vital role in public safety and urban planning. With the increasing availability of crime-related data, data mining techniques can be applied to uncover hidden patterns, crime hotspots, and temporal trends.

This project focuses on analyzing crime data to:
- Identify crime-prone areas (hotspots)
- Analyze time-based crime patterns
- Predict crime severity levels

The project integrates **Data Mining techniques** (clustering, classification, trend analysis) with **Data Warehousing concepts** (fact and dimension tables, star schema design) using Python-based tools.

---

## 🎯 Problem Statement
The objectives of this project are to:
- Identify crime hotspots based on location and time
- Classify crime incidents based on severity levels
- Analyze trends in crime occurrences over time
- Design a data warehouse schema to support multidimensional crime analysis

---

## 📂 Dataset Description
Each record in the dataset represents a single reported crime incident in Karachi. The dataset, karachi_crime_2020_2025, is obtained from Kaggle and covers crimes reported between 2020 and 2025. It captures spatial, temporal, and severity information of various crime incidents, suitable for academic purposes, exploratory data analysis, and predictive modeling.

## 🧾 Features Used
**Incident Type:** Type of crime (e.g., theft, robbery, assault)
**Geographical Location:** Area where the incident occurred (town, subdivision, latitude, longitude)
**Temporal Attributes:**
Date of occurrence
Time of occurrence (hour)
Day of the week
**Severity Score:** Numeric score representing the seriousness of the crime
**Zone Indicators:** Binary flags representing crime zones (Red, Orange, Yellow, Green, White)
**Priority & Rank Metrics:**
Town priority rank
Subdivision priority rank
Overall crime rank

---

## 🧹 Data Preprocessing & Feature Engineering
Before analysis and modeling, the following preprocessing steps are applied:
**Data cleaning:** Handling missing or invalid values and removing duplicate records.
**Data type optimization:** Converting date fields to datetime format, casting categorical attributes to categorical type.
**Categorical feature encoding:** Encoding incident type, location, and temporal categories for machine learning models.
**Numerical feature processing:** Scaling and normalization of numeric attributes (e.g., severity score, priority ranks).
**Feature engineering:** Deriving temporal features from the date column (year, month, day of the week, peak/off-peak hours, weekend/weekday), and creating binary zone indicators for hotspot analysis.

These steps ensure data consistency, realism in synthetic patterns, and improved performance of crime pattern analysis and hotspot detection models.

---

## 🧠 Data Mining Techniques

### 1️⃣ Clustering – Crime Hotspot Detection
Clustering is used to identify crime hotspots without predefined labels.

- **Algorithm Used**: K-Means Clustering
- **Features**:
  - Location (encoded)
  - Time
  - Crime frequency

**Outcome**:
- Identification of high-crime zones
- Discovery of areas with frequent crime occurrences during specific time periods

---

### 2️⃣ Classification – Crime Severity Prediction
Classification is used to predict whether a crime incident is of high or low severity.

- **Target Variable**: Severity (High / Low)
- **Algorithms Used**:
  - Logistic Regression
  - Decision Tree Classifier
- **Evaluation Metrics**:
  - Accuracy
  - Confusion Matrix

This analysis helps understand factors contributing to severe crimes.

---

### 3️⃣ Trend Mining
Trend analysis is performed to analyze crime patterns over time, including:

- Crime frequency by day of the week
- Crime occurrence by hour of the day
- Monthly or seasonal crime trends

These trends help identify peak crime periods.

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
