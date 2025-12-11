import pandas as pd
import matplotlib.pyplot as plt

# =============================================
# ZAIN'S PART — Excel Export + Visualization
# =============================================


def clean_price_column(df):
    # Remove commas, $, and convert to float
    df["Price"] = df["Price"].replace('[\$,]', '', regex=True)
    df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
    return df

def load_and_clean_data():
    # load CSVs created by the scrapers
    amazon_df = pd.read_csv("amazon_products.csv")
    bestbuy_df = pd.read_csv("bestbuy_products.csv")

    # Add source labels
    amazon_df["Source"] = "Amazon"
    bestbuy_df["Source"] = "BestBuy"

    # price columns
    amazon_df = clean_price_column(amazon_df)
    bestbuy_df = clean_price_column(bestbuy_df)

    # combines datasets for visualization
    combined_df = pd.concat([amazon_df, bestbuy_df], ignore_index=True)
    return amazon_df, bestbuy_df, combined_df

def export_to_excel(amazon_df, bestbuy_df, combined_df):
    # this exports all data to one Excel workbook
    with pd.ExcelWriter("prices_output.xlsx") as writer:
        amazon_df.to_excel(writer, sheet_name="Amazon", index=False)
        bestbuy_df.to_excel(writer, sheet_name="BestBuy", index=False)
        combined_df.to_excel(writer, sheet_name="Combined", index=False)

def plot_bar_chart(combined_df):
    # Average price comparison bar chart
    plt.figure(figsize=(12,6))
    combined_df.groupby("Source")["Price"].mean().plot(kind="bar")
    plt.title("Average Price Comparison: Amazon vs BestBuy")
    plt.ylabel("Average Price ($)")
    plt.savefig("avg_price_comparison.png")
    plt.close()

def plot_product_comparison(combined_df):
    # Product by product line plot
    plt.figure(figsize=(12,6))
    for source in combined_df["Source"].unique():
        df = combined_df[combined_df["Source"] == source]
        plt.plot(df["Product Name"], df["Price"], marker="o", label=source)

    plt.title("Price Comparison for Scraped Products")
    plt.xticks(rotation=90)
    plt.ylabel("Price ($)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("product_price_comparison.png")
    plt.close()
