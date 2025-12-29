# Crime Data Analysis & Hotspot Detection

🔗 **GitHub Repository**:  
https://github.com/shoaibhassancs/crime-data-analysis-and-hotspot-detection

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
Dataset: `karachi_crime_2020_2025` (from Kaggle)  
Covers crimes reported in Karachi from 2020–2025, including:
- Spatial data (town, subdivision, latitude, longitude)
- Temporal data (date, hour, day of week)
- Severity scores and zone indicators

**Features Used**
- **Incident Type**: Type of crime (e.g., theft, robbery, assault)  
- **Geographical Location**: Town, subdivision, latitude, longitude  
- **Temporal Attributes**:
  - Date of occurrence
  - Hour
  - Day of the week
- **Severity Score**: Numeric measure of crime seriousness  
- **Zone Indicators**: Red, Orange, Yellow, Green, White  
- **Priority Metrics**:
  - Town priority rank
  - Subdivision priority rank
  - Overall crime rank

---

## Data Preprocessing & Feature Engineering
- **Data Cleaning**: Handling missing/invalid values, removing duplicates  
- **Data Type Optimization**: Convert dates, cast categorical features  
- **Encoding**: Encode incident type, location, temporal features  
- **Numerical Processing**: Scale/normalize severity and rank metrics  
- **Feature Engineering**: Derived temporal features (year, month, day_of_week, peak/off-peak, weekend/weekday) and binary zone indicators

---

## Data Mining Techniques

### Clustering – Crime Hotspot Detection
- **Algorithm**: K-Means Clustering  
- **Features Used**: Latitude, Longitude  
- **Outcome**:
  - Identify high-crime zones (hotspots)
  - Rank clusters by crime intensity
  - Link clusters to towns/subdivisions for actionable insights

### Classification – Crime Severity Prediction
- **Target Variable**: SEVERITY (High / Medium / Low)  
- **Algorithm**: Random Forest Classifier (with class balancing)  
- **Features Used**:
  - Location: LATITUDE, LONGITUDE  
  - Crime details: CRIME_TYPE, TOWN, SUBDIVISION  
  - Temporal: HOUR, DAY_OF_WEEK, MONTH, IS_PEAK_HOUR, IS_WEEKEND  
- **Evaluation Metrics**:
  - Accuracy (~86%)
  - Confusion Matrix
  - Precision, Recall, F1-score  

**Insights**:
- Random Forest identifies key features influencing severity  
- Enables prioritization of high-severity crimes

### Trend Mining
- Crime frequency by day of the week  
- Monthly and yearly crime trends  
- Month vs year heatmap  
- Top crime types in Karachi  

**Insights**: Supports temporal and spatial decision-making for law enforcement

---

## Data Warehouse Design
To support analytical reporting and multidimensional analysis, a **star schema**–based data warehouse is implemented using PostgreSQL (Supabase).

### Fact Table: `Crime_Fact`
Stores measurable crime events and links to dimension tables:
- Crime_Fact_ID  
- Time_ID  
- Location_ID  
- CrimeType_ID  
- severity_score  
- is_peak_hour  
- is_weekend  
- zone_indicator  
- cluster_label (for ML hotspots)

### Dimension Tables

#### `Time_Dim`
- Time_ID  
- date  
- hour  
- day_of_week  
- month  
- year  
- is_peak_hour  
- is_weekend

#### `Location_Dim`
- Location_ID  
- town  
- subdivision  
- latitude  
- longitude  
- risk_zone

#### `CrimeType_Dim`
- CrimeType_ID  
- crime_type  
- severity

This schema enables efficient slice-and-dice analysis across time, location, crime type, and severity.

---

### Star Schema Diagram
```mermaid
erDiagram
    Crime_Fact {
        int Crime_Fact_ID PK
        int Time_ID FK
        int Location_ID FK
        int CrimeType_ID FK
        int severity_score
        boolean is_peak_hour
        boolean is_weekend
        string zone_indicator
        int cluster_label
    }

    Time_Dim {
        int Time_ID PK
        date date
        int hour
        int day_of_week
        int month
        int year
        boolean is_peak_hour
        boolean is_weekend
    }

    Location_Dim {
        int Location_ID PK
        string town
        string subdivision
        float latitude
        float longitude
        string risk_zone
    }

    CrimeType_Dim {
        int CrimeType_ID PK
        string crime_type
        string severity
    }

    Crime_Fact }o--|| Time_Dim : references
    Crime_Fact }o--|| Location_Dim : references
    Crime_Fact }o--|| CrimeType_Dim : references

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
This project demonstrates how data mining and data warehousing techniques can be applied to crime data for:
- Identification of crime hotspots
- Prediction of crime severity levels
- Temporal and spatial trend analysis

The star schema ensures structured, scalable, and reproducible analytics.

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
