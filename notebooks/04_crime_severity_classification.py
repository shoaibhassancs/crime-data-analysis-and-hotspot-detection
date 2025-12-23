import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

raw_df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/karachi_crime_2020_2025_cleaned.csv')
raw_df.head().columns
raw_df.head()

le_df = pd.read_csv('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/data-processed/karachi_crime_2020_2025_label_encoded.csv')
le_df.head().columns
le_df.head()

# -----------------------------
# Define Target and Features
# -----------------------------
X = le_df[
    ['LATITUDE', 'LONGITUDE', 'TOWN', 'SUBDIVISION', 'CRIME_TYPE', 'HOUR', 'DAY_OF_WEEK', 'MONTH', 'IS_PEAK_HOUR', 'IS_WEEKEND']
]  # encoded categorical + numeric features
y = raw_df['SEVERITY']  # categorical: High / Medium / Low

print("Features shape:", X.shape)
print("Target shape:", y.shape)

# -----------------------------
# Train / Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
le = LabelEncoder()
y_train_enc = le.fit_transform(y_train)
y_test_enc = le.transform(y_test)

print(le.classes_)

# -----------------------------
# Train Random Forest Classifier
# -----------------------------
rf_clf = RandomForestClassifier(
    n_estimators=100, # More trees → usually better performance, but slower training and more memory
    random_state=42, 
    class_weight='balanced' # automatically balances classes
)
rf_clf.fit(X_train, y_train_enc)
y_pred = rf_clf.predict(X_test)

# Evaluate Random Forest Classifier
print("Accuracy:", accuracy_score(y_test_enc, y_pred)) # overall correctness
print("Confusion Matrix:\n", confusion_matrix(y_test_enc, y_pred)) # see which classes are confused
print("Classification Report:\n", classification_report(y_test_enc, y_pred, target_names=le.classes_)) # precision, recall, f1-score


# -----------------------------
# Feature Importance Visualization
# -----------------------------
importances = rf_clf.feature_importances_
feature_names = X.columns
feat_df = pd.DataFrame(
    {'Feature': feature_names, 
     'Importance': importances}
)
feat_df = feat_df.sort_values(by='Importance', ascending=False)
print(feat_df)

# -----------------------------
# Visualize
# -----------------------------
plt.figure(figsize=(10,6))
plt.barh(feat_df['Feature'], feat_df['Importance'])
plt.xlabel('Importance')
plt.title('Feature Importance for Crime Severity Classification')
plt.gca().invert_yaxis()  # highest importance on top
plt.show()
plt.savefig('/Users/shoaibhassan/Desktop/AI/PythonProjects/crime-data-analysis-&-hotspot-detection/visuals/crime_severity_feature_importance.png')