This folder contains original dataset (Online Banking Scam.xlsx) and transformed dataset (Online Banking Scam 2.xlsx). 
-----------------------------------------------------------------------------------------------------------------------

ABOUT THE DATASET

Dataset – Online Banking Scam.csv
Source – 

DETAILS OF DATASET

1.Contains 2516 rows x 16 columns
2.The dataset records transaction and login activity of customers in an online banking environment

Columns:
1. TransactionID – Unique transaction identifier
2. AccountID – Customer account number
3. TransactionAmount – Amount of money in the transaction
4. TransactionDate – Timestamp of transaction
5. TransactionType – Debit / Credit
6. Location – City where the transaction occurred
7. DeviceID – Device identifier used for transaction
8. IP Address – IP address of the session
9. MerchantID – Identifier of the merchant involved
10. Channel – Transaction channel (Online / ATM / Branch)
11. CustomerAge – Age of customer
12. CustomerOccupation – Profession of the customer
13. TransactionDuration – Session duration in seconds/minutes
14. LoginAttempts – Number of login attempts before successful transaction
15. AccountBalance – Balance after transaction
16. PreviousTransactionDate – Timestamp of last transaction

Observations:
1. No column directly indicates whether a transaction is fraudulent or not
2. No missing values in the dataset
3. Rich contextual features are available: demographic, geographic, device, and financial

-----------------------------------------------------------------------------------------------------------------------

LABEL ENGINEERING

Since the dataset doesn’t contain a fraud indicator column, we need to create one. This is important to make Machine Learning models for fraud detection.
We rely on domain knowledge of Account Takeover (ATO) scams to define suspicious activity.

RULE-BASED FRAUD INDICATORS

1. Login Behavior
•	If LoginAttempts > 3 → possible brute-force or stolen credential use
•	If new DeviceID or unusual IP Address for a given account → suspicious
2. Transaction Amount
•	If TransactionAmount > 10,000 → high-risk transaction
•	If TransactionAmount > 80% of AccountBalance → unusual draining of account
3. Geographic / Channel Risk
•	If Channel = Online AND location differs significantly from last transaction → suspicious
•	If Location is unusual for the customer → possible ATO
4. Customer Demographics
•	If CustomerAge > 65 AND large transfers occur (> 5,000) → potential scam targeting seniors
•	If Student / low-income profession suddenly makes a very large transfer → suspicious
5. Transaction Frequency / Duration
•	If TransactionDuration < 10 sec → possible automated/bot behavior
•	If multiple transactions happen in short succession (e.g., < 1 min) → suspicious

Using the above rules, we create a new column is_fraud:
1. is_fraud = 1 if any rule is triggered
2. is_fraud = 0 otherwise

ADDING is_fraud COLUMN USING EXCEL

Excel formula for is_fraud column:
=IF(OR(
   [@LoginAttempts]>3,
   [@TransactionAmount]>10000,
   [@TransactionAmount]>0.8*[@AccountBalance],
   AND([@CustomerAge]>65,[@TransactionAmount]>5000),
   [@TransactionDuration]<10
),1,0)

Flags fraud (1) if:
1. Too many login attempts (LoginAttempts > 3)
2. Very high transaction (TransactionAmount > 10000)
3. Transaction is >80% of balance
4. Senior citizen making unusually large transfer
5. Very fast session duration (possible bot)
Else marks as 0 (not fraud)
Now, we have is_fraud column which specifies the fraudulent transaction. 

The transformed Dataset is ready for visualisation.

