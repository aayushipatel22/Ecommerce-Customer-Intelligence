import requests
import pandas as pd

from utils.helper import create_folder


def fetch_comments():

    print("Fetching Customer Comments...")

    url = "https://dummyjson.com/comments"
    response = requests.get(url)

    data = response.json()
    comments = data["comments"]

    df = pd.DataFrame(comments)

    create_folder("data/raw")

    df.to_csv("data/raw/comments.csv", index=False)
    print("Comments Saved Successfully")


if __name__ == "__main__":
    fetch_comments()