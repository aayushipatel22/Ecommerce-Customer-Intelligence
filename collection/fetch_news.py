from newsapi import NewsApiClient
import pandas as pd

from utils.config import NEWS_API_KEY
from utils.helper import create_folder


def fetch_news():

    print("Fetching News...")

    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    articles = newsapi.get_everything(
        q="ecommerce OR amazon shopping OR online shopping",
        language="en",
        sort_by="publishedAt",
        page_size=50,
    )

    df = pd.DataFrame(articles["articles"])

    create_folder("data/raw")

    df.to_csv("data/raw/news.csv", index=False)

    print("News Saved Successfully")


if __name__ == "__main__":
    fetch_news()




# in cmd ---> D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m collection.fetch_news