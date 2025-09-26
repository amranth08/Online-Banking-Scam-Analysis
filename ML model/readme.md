ONLINE BANKING FRAUD DETECTION (RANDOM FOREST MODEL)

PROJECT OVERVIEW

This project builds a machine learning model to detect fraudulent online banking transactions. The model is trained on transaction-level data and predicts whether a new transaction is fraudulent (1) or genuine (0).
We use the Random Forest Classifier, which is an ensemble of decision trees. It works well with mixed data (numerical + categorical), handles class imbalance (via class_weight='balanced'), and provides probabilities for predictions.

DATASET FEATURES

Column - Description
TransactionID	- Unique identifier for transaction (dropped during training)
AccountID -	Customer account number (dropped during training)
TransactionAmount	- Amount of money in the transaction
TransactionDate -	Date of transaction
TransactionTime -	Time of transaction
TransactionType -	Debit / Credit
Location -	City where the transaction occurred
DeviceID	- Device used (dropped during training)
IP Address -	Session IP (dropped during training)
MerchantID	- Merchant identifier (dropped during training)
Channel	- Transaction channel (Online/ATM/Branch)
CustomerAge	- Age of customer
CustomerOccupation	- Occupation of customer
TransactionDuration -	Duration of transaction (in seconds/minutes)
LoginAttempts	- Number of login attempts before success
AccountBalance - Account balance after transaction
PreviousTransactionDate	- Timestamp of previous transaction
is_fraud - Target label → 1 (Fraud), 0 (Not Fraud)

PREPROCESSING STEPS

1. Dropped non-predictive identifiers: TransactionID, AccountID, DeviceID, IP Address, MerchantID.
2. Date handling:
•	Combined Transation_Date + Transaction_Time → TransactionDateTime.
•	Converted all date columns (TransactionDate, PreviousTransactionDate, TransactionDateTime) into numeric timestamps (seconds since epoch).
3. Categorical encoding: Used LabelEncoder for categorical variables (TransactionType, Location, Channel, CustomerOccupation).
4. Scaling numeric values: Standardized numerical features with StandardScaler.
5. Train-test split: 70% training, 30% testing (stratified to preserve fraud ratio).

MODEL TRAINING

1. Algorithm: Random Forest Classifier
2. Hyperparameters:
•	n_estimators = 200 (number of trees)
•	max_depth = 12 (to prevent overfitting)
•	class_weight = 'balanced' (handles fraud class imbalance)
•	random_state = 42 (for reproducibility)
The model is trained using balanced resampling to avoid bias toward majority class (non-fraud).

MODEL EVALUATION

Metrics used:
1. Confusion Matrix - Fraud detection performance.
2. Classification Report - Precision, Recall, F1-score.
3. ROC-AUC Score - Ability to separate fraud vs non-fraud.
4. Precision-Recall AUC - More relevant for imbalanced data.

USING WORKFLOW

1.	Train the model → Run training.py.
•	Saves model + preprocessing artifacts.
2.	Test new transactions → Run testing.py.
•	Loads model, preprocesses input, predicts fraud probability.
