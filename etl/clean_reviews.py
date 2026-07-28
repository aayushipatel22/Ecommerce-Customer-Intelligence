import pandas as pd
from utils.helper import create_folder


def clean_reviews():

    print("Cleaning Reviews...")

    df = pd.read_csv("data/raw/reviews.csv")

    df.columns = df.columns.str.lower()

    df = df.drop_duplicates()

    # Rename columns according to your dataset
    df = df.rename(
        columns={
            "review text": "review_text",
            "review": "review_text",
            "rating": "rating",
        }
    )

    df = df.dropna(subset=["review_text"])

    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    df["rating"] = df["rating"].fillna(df["rating"].median())

    df.to_csv("data/cleaned/reviews_clean.csv", index=False)

    print("Reviews Cleaned Successfully")


if __name__ == "__main__":
    clean_reviews()