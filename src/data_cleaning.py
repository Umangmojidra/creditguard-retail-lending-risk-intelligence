from load_data import load_dataset

df = load_dataset()



# Check missing values
def detect_missing_values(df):

    missing_income = df["monthly_income"].isnull().sum()
    missing_credit_score = df["credit_score"].isnull().sum()

    result = {
        "missing_income_values": int(missing_income),
        "missing_credit_score_values": int(missing_credit_score)
    }

    return result


# Remove dulicate values 

def detect_duplicate_records(df):

    duplicate_loans = df.duplicated(subset=["loan_id"]).sum()

    duplicate_customers = df.duplicated(subset=["customer_id"]).sum()

    result = {
        "duplicate_loan_records": int(duplicate_loans),
        "duplicate_customer_records": int(duplicate_customers)
    }

    return result

# Identify Extreme Loan Amount Outliers
def detect_loan_amount_outliers(df):

    Q1 = df['loan_amount'].quantile(0.25)
    Q3 = df['loan_amount'].quantile(0.75)

    IQR =  Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 - 1.5 * IQR

    outliers = df[
        (df['loan_amount']< lower_bound) |
        (df['loan_amount']> upper_bound)
    ]

    return {
        'total_outliers' : len(outliers),
        'lower_bound' : float(lower_bound),
        'higher_bound' : float(upper_bound)
    }

print(detect_loan_amount_outliers(df))

# Save Cleaned dataset
# df.to_csv("data/processed/clean_loans.csv", index=False)
# print("\nClean dataset saved to data/processed/")

