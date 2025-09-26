import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, precision_recall_curve, auc


# Load dataset
file_path = "Online Banking Scam 2.xlsx"   # <-- update path
df = pd.read_excel(file_path)

# Preprocessing
drop_cols = ['TransactionID', 'AccountID', 'DeviceID', 'IP Address', 'MerchantID']
df = df.drop(columns=[c for c in drop_cols if c in df.columns])

# Handle combined date/time
if 'Transation_Date' in df.columns and 'Transaction_Time' in df.columns:
    df['TransactionDateTime'] = pd.to_datetime(
        df['Transation_Date'].astype(str) + ' ' + df['Transaction_Time'].astype(str),
        dayfirst=True, errors='coerce'
    )
    df = df.drop(columns=['Transation_Date', 'Transaction_Time'])

datetime_cols = ['TransactionDate', 'PreviousTransactionDate', 'TransactionDateTime']
for col in datetime_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        df[col] = df[col].astype('int64') // 10**9

# Separate target
y = df['is_fraud']
X = df.drop('is_fraud', axis=1)

# Encode categoricals
cat_cols = X.select_dtypes(include=['object']).columns
label_encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    label_encoders[col] = le

# Scale numeric
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, stratify=y, random_state=42
)

# Train Random Forest
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    class_weight='balanced',
    random_state=42
)
rf_model.fit(X_train, y_train)


# Evaluation
y_pred = rf_model.predict(X_test)
y_proba = rf_model.predict_proba(X_test)[:, 1]

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("ROC-AUC Score:", roc_auc_score(y_test, y_proba))
precision, recall, _ = precision_recall_curve(y_test, y_proba)
print("Precision-Recall AUC:", auc(recall, precision))


# Save artifacts
joblib.dump(rf_model, "rf_fraud_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")
print("Model, scaler, and encoders saved successfully.")