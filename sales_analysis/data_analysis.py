import pandas as pd


def load_data(filepath):
    """Load sales data from a CSV file into a pandas dataframe"""
    df = pd.read_csv(filepath)
    return df


def calculate_revenue(df):
    """Add a revenue column (quantity * price) to the dataframe"""
    df["revenue"] = df["quantity"] * df["price"]
    return df