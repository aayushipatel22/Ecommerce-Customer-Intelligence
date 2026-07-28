import pandas as pd
from utils.helper import create_folder


def clean_comments():

    print("Cleaning Comments...")

    df = pd.read_csv("data/raw/comments.csv")

    df.columns = df.columns.str.lower()

    df = df.drop_duplicates()

    df["body"] = df["body"].fillna("No Comment")

    # Create a username column from nested user data if available
    if "user.username" in df.columns:
        df = df.rename(columns={"user.username": "username"})
    elif "user" in df.columns:
        df["username"] = "Unknown"

    df.to_csv("data/cleaned/comments_clean.csv", index=False)

    print("Comments Cleaned Successfully")


if __name__ == "__main__":
    clean_comments()