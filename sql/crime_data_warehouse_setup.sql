-- -----------------------------
-- Crime Data Warehouse Setup
-- -----------------------------

-- Temporary table matching the CSV
CREATE TABLE temp_crime_data (
    "INCIDENT_ID" VARCHAR(100),
    "TOWN" VARCHAR(100),
    "TOWN_RISK_LEVEL" VARCHAR(10),
    "TOWN_PRIORITY_RANK" INT,
    "SUBDIVISION" VARCHAR(100),
    "SUBDIVISION_RISK_LEVEL" VARCHAR(10),
    "SUBDIVISION_PRIORITY_RANK" INT,
    "SEVERITY_SCORE" INT,
    "SEVERITY" VARCHAR(10),
    "DATE" DATE,
    "LATITUDE" DOUBLE PRECISION,
    "LONGITUDE" DOUBLE PRECISION,
    "CRIME_TYPE" VARCHAR(100),
    "IS_RED_ZONE" BOOLEAN,
    "IS_ORANGE_ZONE" BOOLEAN,
    "IS_YELLOW_ZONE" BOOLEAN,
    "IS_GREEN_ZONE" BOOLEAN,
    "IS_WHITE_ZONE" BOOLEAN,
    "RISK_ZONE" VARCHAR(10),
    "SOURCE" VARCHAR(100),
    "RANK" INT,
    "HOUR" INT,
    "DAY_OF_WEEK" INT,
    "MONTH" INT,
    "YEAR" INT,
    "IS_PEAK_HOUR" BOOLEAN,
    "IS_WEEKEND" BOOLEAN
);

-- -----------------------------
-- Time Dimension
-- -----------------------------
CREATE TABLE Time_Dim (
    Time_ID SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    hour INT CHECK (hour >= 0 AND hour <= 23),
    day_of_week INT CHECK (day_of_week >= 0 AND day_of_week <= 6),
    month INT CHECK (month >= 1 AND month <= 12),
    year INT CHECK (year >= 2020 AND year <= 2025),
    is_peak_hour BOOLEAN,
    is_weekend BOOLEAN
);

-- -----------------------------
-- Location Dimension
-- -----------------------------
CREATE TABLE Location_Dim (
    Location_ID SERIAL PRIMARY KEY,
    town VARCHAR(100) NOT NULL,
    subdivision VARCHAR(100),
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    risk_zone VARCHAR(10) CHECK (risk_zone IN ('Red','Orange','Yellow','Green'))
);

-- -----------------------------
-- Crime Type Dimension
-- -----------------------------
CREATE TABLE CrimeType_Dim (
    CrimeType_ID SERIAL PRIMARY KEY,
    crime_type VARCHAR(100) NOT NULL,
    severity VARCHAR(10) CHECK (severity IN ('High','Medium','Low'))
);

-- -----------------------------
-- Crime Fact Table
-- -----------------------------
CREATE TABLE Crime_Fact (
    Crime_Fact_ID SERIAL PRIMARY KEY,
    Time_ID INT REFERENCES Time_Dim(Time_ID),
    Location_ID INT REFERENCES Location_Dim(Location_ID),
    CrimeType_ID INT REFERENCES CrimeType_Dim(CrimeType_ID),
    severity_score INT,
    is_peak_hour BOOLEAN,
    is_weekend BOOLEAN,
    zone_indicator VARCHAR(10) CHECK (zone_indicator IN ('Red','Orange','Yellow','Green')),
    cluster_label INT
);

-- -----------------------------
-- Populate Dimension Tables
-- -----------------------------
INSERT INTO Time_Dim (date, hour, day_of_week, month, year, is_peak_hour, is_weekend)
SELECT DISTINCT 
    "DATE", 
    "HOUR", 
    "DAY_OF_WEEK", 
    "MONTH", 
    "YEAR", 
    "IS_PEAK_HOUR", 
    "IS_WEEKEND"
FROM temp_crime_data;

INSERT INTO Location_Dim (town, subdivision, latitude, longitude, risk_zone)
SELECT DISTINCT 
    "TOWN", 
    "SUBDIVISION", 
    "LATITUDE", 
    "LONGITUDE", 
    "RISK_ZONE"
FROM temp_crime_data;

INSERT INTO CrimeType_Dim (crime_type, severity)
SELECT DISTINCT 
    "CRIME_TYPE", 
    "SEVERITY"
FROM temp_crime_data;

-- -----------------------------
-- Populate Fact Table
-- -----------------------------
INSERT INTO Crime_Fact (
    Time_ID,
    Location_ID,
    CrimeType_ID,
    severity_score,
    is_peak_hour,
    is_weekend,
    zone_indicator,
    cluster_label
)
SELECT
    t.Time_ID,
    l.Location_ID,
    c.CrimeType_ID,
    tc."SEVERITY_SCORE",
    t.is_peak_hour,
    t.is_weekend,
    l.risk_zone,
    NULL
FROM temp_crime_data tc
JOIN Time_Dim t
    ON tc."DATE" = t.date AND tc."HOUR" = t.hour
JOIN Location_Dim l
    ON tc."TOWN" = l.town AND tc."SUBDIVISION" = l.subdivision
JOIN CrimeType_Dim c
    ON tc."CRIME_TYPE" = c.crime_type AND tc."SEVERITY" = c.severity;


-- -----------------------------
-- Queries
-- -----------------------------
-- Monthly crime trends by severity
CREATE OR REPLACE VIEW vw_monthly_crime_trends AS
SELECT 
    t.year,
    t.month,
    c.severity,
    COUNT(*) AS crime_count
FROM Crime_Fact f
JOIN Time_Dim t ON f.Time_ID = t.Time_ID
JOIN CrimeType_Dim c ON f.CrimeType_ID = c.CrimeType_ID
GROUP BY t.year, t.month, c.severity
ORDER BY t.year, t.month;

-- Top towns by high-severity crimes
CREATE OR REPLACE VIEW vw_top_high_severity_towns AS
SELECT 
    l.town,
    COUNT(*) AS crime_count
FROM Crime_Fact f
JOIN Location_Dim l ON f.Location_ID = l.Location_ID
JOIN CrimeType_Dim c ON f.CrimeType_ID = c.CrimeType_ID
WHERE c.severity = 'High'
GROUP BY l.town
ORDER BY crime_count DESC
LIMIT 10;

-- Peak vs non-peak hour crimes (if needed)
CREATE OR REPLACE VIEW vw_peak_hour_crimes AS
SELECT 
    is_peak_hour,
    COUNT(*) AS crime_count
FROM Crime_Fact
GROUP BY is_peak_hour;