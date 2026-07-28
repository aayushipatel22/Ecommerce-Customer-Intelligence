import pandas as pd
from utils.helper import create_folder


def clean_products():

    print("Cleaning Products...")

    df = pd.read_csv("data/raw/products.csv")

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing title
    df = df.dropna(subset=["title"])

    # Fill missing descriptions
    df["description"] = df["description"].fillna("No Description")

    # Convert price to numeric
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Remove rows with invalid price
    df = df.dropna(subset=["price"])

    create_folder("data/cleaned")

    df.to_csv("data/cleaned/products_clean.csv", index=False)

    print("Products Cleaned Successfully")


if __name__ == "__main__":
    clean_products()