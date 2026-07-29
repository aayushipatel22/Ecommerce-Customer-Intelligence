import pandas as pd
from elasticsearch.helpers import bulk

from elasticsearch_db.elastic_client import es

INDEX_NAME = "customer_reviews"

def upload_documents():

    print("Loading AI Ready Dataset...")
    df = pd.read_csv("data/processed/ai_ready_dataset.csv")

    actions = []

    for idx, row in df.iterrows():

        action = {
            "_index": INDEX_NAME,
            "_id": idx,
            "_source": {
                "review_text": row["review_text"],
                "rating": None if pd.isna(row["rating"]) else float(row["rating"]),
                "source": row["source"],
                "sentiment": row["sentiment"],
                "confidence_score": float(row["confidence_score"]),
                "sentiment_score": int(row["sentiment_score"])
            }
        }

        actions.append(action)

    bulk(es, actions)

    print("Documents Uploaded Successfully!")

if __name__ == "__main__":
    upload_documents()