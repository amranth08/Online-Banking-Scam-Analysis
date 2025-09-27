import pandas as pd
import numpy as np
import joblib

# Load artifacts
rf_model = joblib.load("rf_fraud_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Columns that were datetime in training
datetime_cols = ['TransactionDate', 'PreviousTransactionDate', 'TransactionDateTime']

def preprocess_new_input(new_df):
    df_copy = new_df.copy()

    # Recreate TransactionDateTime if needed
    if 'Transation_Date' in df_copy.columns and 'Transaction_Time' in df_copy.columns:
        df_copy['TransactionDateTime'] = pd.to_datetime(
            df_copy['Transation_Date'].astype(str) + ' ' + df_copy['Transaction_Time'].astype(str),
            dayfirst=True, errors='coerce'
        )
        df_copy = df_copy.drop(columns=['Transation_Date', 'Transaction_Time'])

    # Convert datetime columns
    for col in ['TransactionDate', 'PreviousTransactionDate', 'TransactionDateTime']:
        if col in df_copy.columns:
            df_copy[col] = pd.to_datetime(df_copy[col], errors='coerce')
            df_copy[col] = df_copy[col].astype('int64') // 10**9

    # Encode categoricals
    for col, le in label_encoders.items():
        if col in df_copy.columns:
            if df_copy[col].iloc[0] not in le.classes_:
                le.classes_ = np.append(le.classes_, df_copy[col].iloc[0])
            df_copy[col] = le.transform(df_copy[col].astype(str))

    # Reorder columns to match training
    df_copy = df_copy.reindex(columns=scaler.feature_names_in_, fill_value=0)

    # Scale numeric
    num_scaled = scaler.transform(df_copy)
    return num_scaled

# example for non-fraudulent transactoin
new_data = pd.DataFrame([{
    'TransactionAmount': 8000,
    'Transation_Date': '20/11/23',       
    'Transaction_Time': '16:39:15',      
    'TransactionType': 'Debit',
    'Location': 'City_X',
    'Channel': 'Online',
    'CustomerAge': 30,
    'CustomerOccupation': 'Engineer',
    'TransactionDuration': 15,
    'LoginAttempts': 3,
    'AccountBalance': 10000,
    'PreviousTransactionDate': '18/11/23 10:00:00'
}])

# example for fraudulent transaction
new_data = pd.DataFrame([{
    'TransactionAmount': 15000,                # > 10,000 → high-risk
    'Transation_Date': '20/11/23',             # recent date
    'Transaction_Time': '00:05:10',            # unusual midnight transaction
    'TransactionType': 'Debit',
    'Location': 'UnknownCity',                 # unusual location
    'Channel': 'Online',                       # risky channel
    'CustomerAge': 70,                         # senior → high-risk if large transfer
    'CustomerOccupation': 'Retired',
    'TransactionDuration': 5,                  # < 10 sec → bot-like
    'LoginAttempts': 5,                        # > 3 → brute-force login
    'AccountBalance': 18000,                   # 15000 is ~83% of balance
    'PreviousTransactionDate': '18/11/23 10:00:00'
}])

# Preprocess & predict
new_input_processed = preprocess_new_input(new_data)
pred = rf_model.predict(new_input_processed)
prob = rf_model.predict_proba(new_input_processed)[:, 1]

print("Prediction (0=Not Fraud, 1=Fraud):", pred)
print("Fraud Probability:", prob)
