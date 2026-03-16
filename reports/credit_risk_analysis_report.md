# CreditGuard: Retail Lending Risk Intelligence

## 1. Business Background

GM Bank is a mid-sized retail banking institution offering loan products such as personal loans, home loans, auto loans, and credit cards. Rapid growth in loan disbursement has led to an increase in loan defaults and Non-Performing Assets (NPAs).  

This project analyzes historical loan data to identify risk factors influencing borrower repayment behavior and support improved credit risk management.

---

## 2. Business Objectives

1. Identify key drivers influencing loan default
2. Segment customers based on credit risk
3. Analyze repayment delays and delinquency patterns
4. Reduce NPAs using predictive insights
5. Support stronger credit approval and monitoring policies

---

## 3. Dataset Overview

The dataset contains **1500+ retail loan records** representing various loan products issued by GM Bank.

Key features include:

- Customer age
- Monthly income
- Employment type
- Credit score
- Loan amount
- Loan tenure
- EMI amount
- EMI delay days
- Loan status
- Region

Each record represents a single loan issued to a customer.

---

## 4. Data Quality Validation

Before performing analysis, the dataset was validated for potential issues.

The following checks were performed:

- Detection of missing values in income and credit score fields
- Identification of extreme loan amount outliers using the IQR method
- Detection of duplicate loan or customer records

These checks ensured the reliability of the dataset before further analysis.

---

## 5. Loan Default Assessment

The analysis evaluated overall portfolio health and default risk patterns.

Key findings:

- Certain loan products such as **personal loans and credit cards show higher default rates**
- Default risk increases among **lower income groups**
- Loan type plays a significant role in borrower repayment behavior

---

## 6. Customer Risk Profiling

Borrower characteristics were analyzed to identify risk patterns.

Key observations:

- Customers with **lower credit scores show higher default probability**
- Borrowers with **unstable income or employment types** exhibit higher risk
- Risk segmentation categorized customers into **low, medium, and high-risk groups**

---

## 7. Repayment Behavior & Delinquency Analysis

Repayment patterns were analyzed to identify early warning signals.

Insights:

- Customers with **frequent EMI delays are more likely to default**
- **Long-tenure loans may show increased delinquency risk**
- Customers holding **multiple loans tend to show higher repayment stress**

---

## 8. Regional & Product Risk Evaluation

Operational risk varies across geographic regions and loan products.

Key insights:

- Certain regions contribute more significantly to loan defaults
- **Unsecured loans** generally show higher risk compared to secured loans

---

## 9. Key Risk Drivers Identified

Major factors influencing loan defaults include:

- Low credit score
- High EMI-to-income ratio
- Unsecured loan types
- Frequent EMI delays
- Regional economic variations

---

## 10. Business Recommendations

Based on the analysis, the following actions are recommended:

1. Strengthen credit approval criteria for low credit score customers
2. Implement income-based EMI affordability limits
3. Monitor high-risk regions more closely
4. Introduce early warning systems for EMI payment delays
5. Adjust pricing or approval rules for unsecured loans

---

## 11. Conclusion

This analysis provides insights into borrower risk patterns and loan performance across GM Bank's retail portfolio.  

By strengthening credit evaluation and monitoring repayment behavior, the bank can reduce NPAs and improve overall loan portfolio health.