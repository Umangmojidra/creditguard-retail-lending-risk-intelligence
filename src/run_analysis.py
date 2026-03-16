import pandas as pd

from visualization import generate_all_visualizations

# Load dataset
df = pd.read_csv("data/raw/RetailLendingRiskIntelligence.csv")

# Generate visualizations
generate_all_visualizations(df)