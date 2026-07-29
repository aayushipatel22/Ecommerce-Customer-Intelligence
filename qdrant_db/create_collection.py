from qdrant_client.models import Distance, VectorParams
from qdrant_db.qdrant_client import client

COLLECTION_NAME = "customer_reviews"

def create_collection():

    collections = client.get_collections().collections

    existing = [c.name for c in collections]

    if COLLECTION_NAME in existing:

        print("Collection already exists.")

        return

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    print("Collection Created Successfully!")


if __name__ == "__main__":
    create_collection()