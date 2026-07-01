def revenue_by_region(df):
    """Return total revenue grouped by region."""
    return df.groupby("region")["revenue"].sum()


def revenue_by_category(df):
    """Return total revenue grouped by category."""
    return df.groupby("category")["revenue"].sum()


def top_products(df):
    """Return products ranked by total revenue, highest first."""
    return df.groupby("product")["revenue"].sum().sort_values(ascending=False)


def summary_stats(df):
    """Return a dictionary of overall sales summary statistics."""
    return {
        "total_revenue": df["revenue"].sum(),
        "total_orders": len(df),
        "average_order_value": df["revenue"].mean(),
        "num_regions": df["region"].nunique(),
        "num_products": df["product"].nunique(),
    }
