# CreditGuard: Retail Lending Risk Intelligence

## Project Overview
CreditGuard is a data analytics project focused on analyzing retail lending data to identify key drivers of loan defaults and credit risk patterns.

The objective of this project is to help financial institutions understand borrower behavior, identify high-risk customers, and improve credit approval strategies to reduce Non-Performing Assets (NPAs).

---

## Business Objectives
- Identify key drivers influencing loan defaults
- Segment customers based on credit risk
- Analyze repayment delays and delinquency patterns
- Evaluate regional and product-level risk
- Support stronger credit approval and monitoring policies

---

## Dataset
The dataset contains **1500+ retail loan records** with customer, loan, and repayment attributes.

Key features include:

- Customer age
- Monthly income
- Employment type
- Credit score
- Loan amount
- Loan tenure
- EMI delay days
- Loan status
- Region

Each record represents **one loan issued to a borrower**.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- SQL

---

## Key Analysis Performed

### Loan Default Assessment
- Calculated default percentage
- Identified loan products with the highest default risk
- Analyzed default risk across income brackets

### Customer Risk Profiling
- Age vs repayment behavior
- Employment type impact on loan repayment
- Credit score impact on default probability
- Customer risk segmentation

### Repayment Behavior Analysis
- Average EMI delay analysis
- Loan tenure risk evaluation
- Multiple loan delinquency analysis

### Regional & Product Risk Evaluation
- Region-wise NPA analysis
- Secured vs unsecured loan risk comparison

---

## Key Insights
- Personal loans and credit cards show higher default risk
- Customers with **low credit scores** have significantly higher default probability
- **EMI delays above 30 days** strongly indicate delinquency risk
- Certain regions consistently show **higher loan default rates**
- Unsecured loans carry higher risk compared to secured loans

---

## Project Structure
# CreditGuard: Retail Lending Risk Intelligence

## Project Overview
CreditGuard is a data analytics project focused on analyzing retail lending data to identify key drivers of loan defaults and credit risk patterns.

The objective of this project is to help financial institutions understand borrower behavior, identify high-risk customers, and improve credit approval strategies to reduce Non-Performing Assets (NPAs).

---

## Business Objectives
- Identify key drivers influencing loan defaults
- Segment customers based on credit risk
- Analyze repayment delays and delinquency patterns
- Evaluate regional and product-level risk
- Support stronger credit approval and monitoring policies

---

## Dataset
The dataset contains **1500+ retail loan records** with customer, loan, and repayment attributes.

Key features include:

- Customer age
- Monthly income
- Employment type
- Credit score
- Loan amount
- Loan tenure
- EMI delay days
- Loan status
- Region

Each record represents **one loan issued to a borrower**.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- SQL

---

## Key Analysis Performed

### Loan Default Assessment
- Calculated default percentage
- Identified loan products with the highest default risk
- Analyzed default risk across income brackets

### Customer Risk Profiling
- Age vs repayment behavior
- Employment type impact on loan repayment
- Credit score impact on default probability
- Customer risk segmentation

### Repayment Behavior Analysis
- Average EMI delay analysis
- Loan tenure risk evaluation
- Multiple loan delinquency analysis

### Regional & Product Risk Evaluation
- Region-wise NPA analysis
- Secured vs unsecured loan risk comparison

---

## Key Insights
- Personal loans and credit cards show higher default risk
- Customers with **low credit scores** have significantly higher default probability
- **EMI delays above 30 days** strongly indicate delinquency risk
- Certain regions consistently show **higher loan default rates**
- Unsecured loans carry higher risk compared to secured loans

---

## Project Structure
CreditGuard
│
├── data
│ ├── raw
│ └── processed
│
├── src
│ ├── data_quality.py
│ ├── data_cleaning.py
│ ├── feature_engineering.py
│ ├── eda_analysis.py
│ └── visualization.py
│
├── visuals
│
├── sql
│ └── risk_analysis_queries.sql
│
├── reports
│ └── credit_risk_analysis_report.md
│
└── README.md


---

## Report
The full analytical report is available here:

`reports/credit_risk_analysis_report.md`

---

## Future Improvements
- Build a Flask API for loan risk analytics
- Create an interactive dashboard for monitoring credit risk
- Develop predictive models for loan default prediction.