import pandas as pd 

def load_dataset():
    file_path = "data/raw/RetailLendingRiskIntelligence.csv"

    df = pd.read_csv(file_path)

    print("Dataset Loaded Succcessfully")
    print("Shape :",df.shape)

    return df

if __name__ == "__main__":
    df = load_dataset()
    print(df.head())

