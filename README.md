# Online-Banking-Scam-Analysis

PROJECT OVERVIEW

Account Takeover (ATO) is one of the most damaging types of online banking fraud. Fraudsters gain unauthorized access to customer accounts (through phishing, credential leaks, or malware) and perform illegal transactions.

This project applies data analytics and machine learning to detect suspicious login and transaction patterns that indicate potential ATO attacks. The goal is to build a system that can analyse transaction data, identify anomalies, and flag high-risk activities before financial damage occurs.


OBJECTIVES

•	Understand behavioural differences between legitimate users and fraudsters.
•	Detects unusual login behaviours (new device, foreign IP, odd login time).
•	Flag suspicious transactions following compromised logins.
•	Build predictive models to classify or detect anomalies.
•	Provide visual insights through dashboards.


DATASET

The dataset consists of synthetic banking login and transaction records with fraud labels.

Example Fields

Login Data
•	login_id: Unique login attempt ID
•	account_id: Customer account number
•	timestamp: Login time
•	device_id: Device fingerprint
•	ip_country: Login country
•	login_success: 1 if login succeeded, 0 if failed

Transaction Data
•	transaction_id: Transaction unique ID
•	account_id: Customer account
•	timestamp: Transaction time
•	amount: Transaction amount
•	transaction_type: (transfer, payment, withdrawal)
•	destination_country: Receiver’s country
•	is_new_payee: Whether the payee is new
•	is_fraud: 1 = fraudulent, 0 = genuine


METHODS

1. Data Preprocessing
•	Convert timestamps → derive features (hour, day_of_week).
•	Handle missing values & duplicates.
•	Encode categorical fields (country, device, transaction type).
•	Normalize long-tailed features (log-transform amount).
2. Exploratory Data Analysis (EDA)
•	Fraud rate by transaction type, hour, device, and country.
•	Login success vs failed attempts.
•	Geographic fraud hotspots (IP vs account country).
•	Boxplots for transaction amounts (fraud vs legit).
3. Feature Engineering
•	Login anomalies: is_new_device, is_new_location, num_failed_logins.
•	Transaction anomalies: amount/avg_amount_30d, is_new_payee, cross_border_txn.
•	Behavioural features: txn_velocity_1h, txn_count_24h, time_gap_between_login_and_txn.
4. Modelling Approaches
Supervised Learning (if labels available)
•	Logistic Regression → interpretable baseline.
•	Random Forest / XGBoost → strong classifiers with feature importance.
•	Neural Networks (MLP) → capture nonlinear patterns.
Unsupervised Learning (if no labels)
•	Isolation Forest → anomaly detection on transaction features.
•	Autoencoder → reconstruction error flags unusual transactions.
•	One-Class SVM → learns “normal” behaviour, flags outliers.
5. Evaluation Metrics
•	Precision, Recall, F1-score → fraud detection effectiveness.
•	ROC-AUC, PR-AUC → model robustness (PR-AUC better for imbalance).
•	Precision@K → % of real frauds in top K alerts.
•	Cost-based metric → savings from blocked frauds vs false alarms.
6. Explainability
•	SHAP values → explain why a transaction was flagged.
•	Feature importance plots → key fraud indicators.
•	Rule extraction → human-readable fraud rules (e.g., “High-value transfer from new device at 2 AM”).

TOOLS & TECHNOLOGIES

•	Programming: Python (pandas, numpy, scikit-learn, imbalanced-learn, xgboost, matplotlib, seaborn).
•	Anomaly Detection: IsolationForest, Autoencoder (Keras/PyTorch).
•	Visualization/Dashboard: Power BI / Tableau / Streamlit.
•	Data Storage: CSV / SQL database.
•	Version Control: GitHub.
•	Documentation: Jupyter Notebooks, Markdown reports.

DASHBOARD (INSIGHTS FOR ANALYSTS)

Key components of fraud monitoring dashboard:
•	KPIs: total transactions, fraud count, fraud rate, total fraud losses.
•	Time series: fraud attempts per day/hour.
•	Geo map: fraud origin vs destination countries.
•	Top risky accounts and devices.
•	Recent alerts: suspicious transactions with explanations.

DELIVERABLES

1.	Synthetic Dataset (CSV with login + transaction records).
2.	EDA Notebook – trends, fraud patterns, visualizations.
3.	Model Notebook – preprocessing, feature engineering, fraud detection model.
4.	Explainability Report – SHAP values, feature impacts.
5.	Dashboard (Power BI / Streamlit).
6.	Final Report – methods, results, business implications.
7.	Presentation Slides – problem → data → analysis → results → demo.

PROJECT WORKFLOW

1.	Data Collection / Synthetic Data Generation.
2.	Data Cleaning & Preprocessing.
3.	Exploratory Data Analysis (EDA).
4.	Feature Engineering.
5.	Model Training & Evaluation.
6.	Explainability & Fraud Rules.
7.	Dashboard Development.
8.	Report & Presentation.





Amaranth Prakash
16th Sep, 2025
