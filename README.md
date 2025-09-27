# 🏦 Online-Banking-Scam-Analysis

## Project Overview
Account Takeover (ATO) fraud is one of the most damaging types of online banking scams.  
Fraudsters gain unauthorized access to customer accounts (through phishing, stolen credentials, or malware) and perform illegal transactions.  

This project applies **data analytics and machine learning (Random Forest)** to detect suspicious login and transaction patterns that indicate potential ATO fraud.  
The system analyzes transaction data, identifies anomalies, and flags high-risk activities before financial damage occurs.  

---

## Objectives
- Understand behavioural differences between legitimate users and fraudsters.  
- Detect unusual login behaviours (e.g., repeated failed login attempts).  
- Flag suspicious transactions following compromised logins.  
- Build a **Random Forest classifier** to predict fraud.  
- Provide **visual insights via dashboards in Power BI** for fraud analysts.  

---

## Dataset
The dataset contains transaction records with fraud labels.  

### Example Fields
| Column | Description |
|--------|-------------|
| `TransactionID` | Unique transaction identifier (dropped in training) |
| `AccountID` | Customer account number (dropped in training) |
| `TransactionAmount` | Amount of money in the transaction |
| `TransactionDate` | Transaction date |
| `TransactionTime` | Transaction time |
| `TransactionType` | Debit / Credit |
| `Location` | City where the transaction occurred |
| `DeviceID` | Device identifier (dropped in training) |
| `IP Address` | IP address of session (dropped in training) |
| `MerchantID` | Merchant identifier (dropped in training) |
| `Channel` | Transaction channel (Online / ATM / Branch) |
| `CustomerAge` | Age of customer |
| `CustomerOccupation` | Occupation of customer |
| `TransactionDuration` | Session duration |
| `LoginAttempts` | Number of login attempts before success |
| `AccountBalance` | Balance after transaction |
| `PreviousTransactionDate` | Timestamp of last transaction |
| `is_fraud` | Target label → `1 = Fraud`, `0 = Genuine` |

---

## Methods

### Data Preprocessing
- Dropped non-predictive identifiers (`TransactionID`, `AccountID`, `DeviceID`, `IP Address`, `MerchantID`).  
- Combined `Transation_Date` + `Transaction_Time` → `TransactionDateTime`.  
- Converted datetime features into **numeric timestamps**.  
- Encoded categorical variables using **LabelEncoder**.  
- Scaled numeric features with **StandardScaler**.  
- Split dataset: **70% training / 30% testing**.  

### Exploratory Data Analysis (EDA) in Power BI
- Fraud rate by **transaction type, location, channel**.  
- Fraud count vs **login attempts**.  
- **Customer age vs transaction amount** (fraud vs non-fraud).  
- **Transaction duration analysis** (normal vs suspicious).  
- Dashboard KPIs: fraud rate, fraud losses, suspicious accounts.  

### Feature Engineering
- Login anomalies → multiple login attempts.  
- Transaction anomalies → large transfer amounts, account draining.  
- Demographic risk → elderly victims with large transfers.  
- Behavioural → short session duration, frequent rapid transactions.  

### Modeling
- Algorithm: **Random Forest Classifier**  
  - `n_estimators = 200`  
  - `max_depth = 12`  
  - `class_weight = 'balanced'`  
- Compared against Logistic Regression baseline.  
- Random Forest chosen for **higher recall and ROC-AUC**.  

### Evaluation Metrics
- **Confusion Matrix**  
- **Classification Report** (Precision, Recall, F1-score)  
- **ROC-AUC Score**  
- **Precision-Recall AUC** (better for imbalanced data)  

#### Example Results (Random Forest)
- Accuracy: **98%**  
- Recall (Fraud): **82%**  
- ROC-AUC: **0.99**  
- Precision-Recall AUC: **0.98**  

---

## Tools & Technologies
- **Python** → pandas, numpy, scikit-learn, imbalanced-learn  
- **Modeling** → Random Forest Classifier  
- **Visualization** → Power BI  
- **Data Storage** → Excel dataset  
- **Model Persistence** → joblib (`rf_fraud_model.pkl`, `scaler.pkl`, `label_encoders.pkl`)  
- **Version Control** → GitHub  

---

## Dashboard Insights (Power BI)
Fraud monitoring dashboard includes:  
- **KPIs** → total transactions, fraud count, fraud rate  
- **Fraud distribution** → by channel, location, transaction type  
- **Time series** → fraud attempts over time  
- **Customer demographics** → age group risk patterns  
- **Top risky accounts** → accounts with multiple suspicious transactions  

---

## Deliverables
- Processed dataset  
- Power BI dashboard (EDA + fraud insights)  
- Python scripts: `training.py` (train model), `testing.py` (predict new data)  
- Trained artifacts: `rf_fraud_model.pkl`, `scaler.pkl`, `label_encoders.pkl`  
- Final documentation (methods, results, implications)  
- Presentation slides  

---

## Project Workflow
1. Data Cleaning & Preprocessing  
2. Exploratory Data Analysis (**Power BI**)  
3. Feature Engineering  
4. Model Training (**Random Forest**)  
5. Model Evaluation  
6. Fraud Detection Dashboard  
7. Documentation & Reporting  

---

**Prepared by**: Amaranth Prakash  
**Date**: 16th Sep, 2025  
