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
Each record in the dataset represents a single crime incident.

### Attributes Used
- **Crime_Type**: Type of crime (e.g., theft, assault, burglary)
- **Location**: Area or zone where the crime occurred
- **Time**: Hour of the incident
- **Day**: Day of the week
- **Severity**: Level of crime severity (Low / High)

📌 *The dataset can be sourced from open government crime datasets or simulated for academic purposes.*

---

## 🧹 Data Preprocessing
Before applying data mining techniques, the following preprocessing steps are performed:

- Handling missing values
- Encoding categorical variables (Crime_Type, Location, Day)
- Feature scaling for numerical attributes
- Feature engineering:
  - Peak vs off-peak hours
  - Weekday vs weekend

These steps ensure data quality and improve model performance.

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
