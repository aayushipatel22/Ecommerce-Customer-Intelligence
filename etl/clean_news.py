import pandas as pd
from utils.helper import create_folder


def clean_news():

    print("Cleaning News...")

    df = pd.read_csv("data/raw/news.csv")

    df.columns = df.columns.str.lower()

    df = df.drop_duplicates()

    df["title"] = df["title"].fillna("No Title")

    df["description"] = df["description"].fillna("No Description")

    df["content"] = df["content"].fillna("No Content")

    df.to_csv("data/cleaned/news_clean.csv", index=False)

    print("News Cleaned Successfully")


if __name__ == "__main__":
    clean_news()