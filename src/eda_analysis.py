import pandas as pd 

df = pd.read_csv('data/processed/clean_loans.csv')
# What percentage of issued loans result in defaults?
def calculate_default_loan_percentage(df):

    total_loans = len(df)

    default_loans = df[df["loan_status"] == "Default"].shape[0]

    default_percentage = (default_loans / total_loans) * 100
    print("Total Loans:", total_loans)
    print("Defaulted Loans:", default_loans)
    print("Default Percentage: {:.2f}%".format(default_percentage))

# calculate_default_loan_percentage(df)

    # Which loan products carry the highest default risk?
def loan_type_default_risk(df):

    loan_defaults = pd.crosstab(df['loan_type'],df['loan_status'])

    loan_defaults['default_rate'] = (
    loan_defaults['Default'] / loan_defaults.sum(axis=1)
    ) * 100

    loan_defaults = loan_defaults.sort_values(by= 'default_rate', ascending= False)

    print('\nDeafult Risk by Loan Type :')
    print(loan_defaults)

# loan_type_default_risk(df)

    # Is default risk higher among specific income brackets?

def income_bracket_default_risk(df):
        
    bins = [0, 30000, 60000, 100000, float('inf')]

    lables = [
            "Low Income",
            "Lower Middle Income",
            "Upper Middle Income",
            "High Income"
    ]

    df['income_bracket'] = pd.cut(df['monthly_income'], bins= bins, labels= lables)

    income_defaults = pd.crosstab(df['income_bracket'], df['loan_status'])

    income_defaults['default_rate'] = (
        income_defaults['Default'] / income_defaults.sum(axis=1)
    ) * 100

    print("\nDefault Risk by Income Bracket:")
    print(income_defaults)
# income_bracket_default_risk(df)


# 2. Customer Risk Profiling 
def age_repayment_analysis(df):
    
    age_groups = pd.cut(
           df['customer_age'],
           bins = [18,30,40,50,60,100],
           labels = ["18-30", "31-40", "41-50", "51-60", "60+"]
    )

    df['age_group'] = age_groups

    age_defaults = pd.crosstab(df['age_group'],df['loan_status'])

    age_defaults['default_rate'] = (
        age_defaults["Default"] / age_defaults.sum(axis=1)
    )*100

    return age_defaults.reset_index().to_dict(orient="records")
# age_repayment_analysis(df)

# Employeement type impect

def employeement_type_impect(df):
       
    employment_defaults = pd.crosstab(df['employment_type'],df['loan_status'])

    employment_defaults['default_rate'] = (employment_defaults['Default']/ employment_defaults.sum(axis = 1))*100

    return employment_defaults.reset_index().to_dict(orient="records")
    
# employeement_type_impect(df)

def credit_score_repayment_analysis(df):
      
    bins = [300, 600, 750, 900]

    labels = ['Low Score', 'Medium Score', 'High Score']

    df['credit_category'] = pd.cut(df['credit_score'], bins=bins, labels= labels)

    credit_defaults = pd.crosstab(df['credit_category'], df['loan_status'])

    credit_defaults['default_rate'] = (
        credit_defaults['Default'] / credit_defaults.sum(axis=1)
      )*100

    return credit_defaults.reset_index().to_dict(orient='records')

# credit_score_repayment_analysis(df)

def customer_risk_segmentation(df):

    def risk_level(row):

        if row["credit_score"] < 600 or row["emi_delay_days"] > 30:
            return "High Risk"

        elif row["credit_score"] < 750:
            return "Medium Risk"

        else:
            return "Low Risk"

    df["risk_segment"] = df.apply(risk_level, axis=1)

    risk_summary = df["risk_segment"].value_counts()

    return risk_summary.to_dict()
    
# customer_risk_segmentation(df)

def average_emi_delay(df):
     
    average_delay = df['emi_delay_days'].mean()

    max_delay = df['emi_delay_days'].max()

    delay_summary = {
        'average_delay' : round(average_delay,2),
        'Maximum_delay' : max_delay
    }

    return delay_summary
    
# average_emi_delay(df)

def tenure_risk_analysis(df):
     
    bins = [0, 24, 60, 120, float('inf')]

    labels = [
        "Short Term (0-2y)",
        "Medium Term (2-5y)",
        "Long Term (5-10y)",
        "Very Long Term"
    ] 

    df['tenure_category'] = pd.cut(df['tenure_months'], bins=bins, labels= labels)

    tenure_defaluts = pd.crosstab(df['tenure_category'], df['loan_status'])
    
    tenure_defaluts = (
        tenure_defaluts['Default'] / tenure_defaluts.sum(axis=1)
    ) * 100

    return tenure_defaluts.reset_index().to_dict(orient='records')

# tenure_risk_analysis(df)

def multiple_loan_delinquency(df):
     
    loan_counts = df.groupby('customer_id')['loan_id'].count().reset_index()

    loan_counts.columns = ["customer_id", "loan_count"] 

    df = df.merge(loan_counts, on="customer_id")

    df['multiple_loans'] = df['loan_count'] > 1

    delinquency_analysis = pd.crosstab(df['multiple_loans'], df['loan_status'])

    delinquency_analysis['default_rate'] = (
        delinquency_analysis['Default'] / delinquency_analysis.sum(axis=1)
    )*100

    return delinquency_analysis.reset_index().to_dict(orient='records')

# multiple_loan_delinquency(df)

def regional_npa_analysis(df):

    regional_defaults = pd.crosstab(df['region'], df['loan_status'])

    regional_defaults['default_rate'] = (
        regional_defaults['Default'] / regional_defaults.sum(axis=1)
    ) * 100

    regional_defaults = regional_defaults.sort_values(
        by= "default_rate",
        ascending= False
    )

    return regional_defaults.reset_index().to_dict(orient='records')

def secured_vs_unsecured_risk(df):

    secured_loans = ['Home Loan', 'Auto Loan']
    df['loan_security'] = df['loan_type'].apply(
        lambda x : 'Secured' if x in secured_loans else 'Unsecured'
    )
    security_defaults = pd.crosstab(df['loan_security'], df['loan_status'])

    security_defaults['default_rate'] = (
        security_defaults['Default'] / security_defaults.sum(axis=1)
    ) * 100

    return security_defaults.reset_index().to_dict(orient='records')

#secured_vs_unsecured_risk(df)


def dataset_summary(df):

    summary = {
        "total_loans": len(df),
        "average_loan_amount": round(df["loan_amount"].mean(), 2),
        "average_income": round(df["monthly_income"].mean(), 2),
        "average_credit_score": round(df["credit_score"].mean(), 2),
        "loan_types": df["loan_type"].value_counts().to_dict(),
        "regions": df["region"].value_counts().to_dict()
    }

    return summary

# dataset_summary(df)