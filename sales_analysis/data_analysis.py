import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load sales data from a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the file: {filepath}")
    return df


def calculate_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Add a revenue column (quantity * price) to the DataFrame."""
    if "quantity" not in df.columns or "price" not in df.columns:
        raise ValueError("Data must contain 'quantity' and 'price' columns")
    df["revenue"] = df["quantity"] * df["price"]
    return df