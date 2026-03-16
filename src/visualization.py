import matplotlib.pyplot as plt
import pandas as pd

def default_by_loan_type(df):

    data = pd.crosstab(df["loan_type"], df["loan_status"])

    data.plot(kind="bar", stacked=True)

    plt.title("Default Rate by Loan Type")
    plt.xlabel("Loan Type")
    plt.ylabel("Number of Loans")

    plt.savefig("visuals/loan_type_default.png")

    plt.close()


def credit_score_vs_default(df):

    bins = [300, 600, 750, 900]
    labels = ["Low", "Medium", "High"]

    df["credit_category"] = pd.cut(df["credit_score"], bins=bins, labels=labels)

    data = pd.crosstab(df["credit_category"], df["loan_status"])

    data.plot(kind="bar", figsize=(8,5))

    plt.title("Credit Score vs Loan Default")
    plt.xlabel("Credit Score Category")
    plt.ylabel("Number of Loans")

    plt.tight_layout()

    plt.savefig("visuals/credit_score_default.png")

    plt.close()

def emi_delay_distribution(df):

    plt.figure(figsize=(8,5))

    plt.hist(df["emi_delay_days"], bins=20)

    plt.title("Distribution of EMI Delays")
    plt.xlabel("Delay Days")
    plt.ylabel("Number of Customers")

    plt.tight_layout()

    plt.savefig("visuals/emi_delay_distribution.png")

    plt.close()

def region_default_chart(df):

    data = pd.crosstab(df["region"], df["loan_status"])

    data.plot(kind="bar", figsize=(8,5))

    plt.title("Region-wise Loan Default")
    plt.xlabel("Region")
    plt.ylabel("Number of Loans")

    plt.tight_layout()

    plt.savefig("visuals/region_default.png")

    plt.close()

def generate_all_visualizations(df):

    default_by_loan_type(df)

    credit_score_vs_default(df)

    emi_delay_distribution(df)

    region_default_chart(df)

    print("All visualizations saved in visuals/ folder")