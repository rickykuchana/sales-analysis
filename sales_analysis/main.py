import argparse
from sales_analysis.data_analysis import load_data, calculate_revenue
from sales_analysis.analysis import (
    revenue_by_region,
    revenue_by_category,
    top_products,
    summary_stats,
)


def main():
    """Run the full sales analysis from the command line."""
    parser = argparse.ArgumentParser(description="Analyze sales data from a CSV file.")
    parser.add_argument("filepath", help="Path to the sales CSV file")
    args = parser.parse_args()

    # Load and prepare the data
    df = load_data(args.filepath)
    df = calculate_revenue(df)

    # Run the analyses and print results
    print("=== Revenue by Region ===")
    print(revenue_by_region(df))

    print("\n=== Revenue by Category ===")
    print(revenue_by_category(df))

    print("\n=== Top Products ===")
    print(top_products(df))

    print("\n=== Summary ===")
    for key, value in summary_stats(df).items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()