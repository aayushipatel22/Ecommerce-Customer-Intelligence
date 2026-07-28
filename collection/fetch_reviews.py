import pandas as pd


def fetch_reviews():

    print("Loading Reviews Dataset...")

    df = pd.read_csv("data/raw/reviews.csv")

    print(df.head())

    print(f"\nTotal Reviews : {len(df)}")


if __name__ == "__main__":
    fetch_reviews()