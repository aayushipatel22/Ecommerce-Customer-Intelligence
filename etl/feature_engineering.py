# Feature Engineering means: creating new useful columns from existing data.

import pandas as pd


def feature_engineering():

    print("Creating Features...")

    df = pd.read_csv("data/cleaned/reviews_clean.csv")

    # Count the number of words in each review
    df["review_length"] = df["review_text"].astype(str).apply(lambda x: len(x.split()))

    # Categorize ratings
    df["rating_category"] = df["rating"].apply(
        lambda x: (
            "Positive"
            if x >= 4
            else "Neutral"
            if x == 3
            else "Negative"
        )
    )

    df.to_csv("data/cleaned/reviews_clean.csv", index=False)

    print("Features Created Successfully")


if __name__ == "__main__":
    feature_engineering()