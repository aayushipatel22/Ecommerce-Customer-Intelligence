from embeddings.embedding_model import embedding_model
from qdrant_db.qdrant_client import client

COLLECTION_NAME = "customer_reviews"

def search(query):

    print(f"\nSearching for: {query}")

    # Convert query into embedding vector
    query_vector = embedding_model.encode(query).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=5
    )

    print("\nTop Results\n")

    for point in results.points:

        print("-" * 60)
        print(f"Score      : {point.score:.4f}")
        print(f"Review     : {point.payload['review_text']}")
        print(f"Sentiment  : {point.payload['sentiment']}")
        print(f"Source     : {point.payload['source']}")


if __name__ == "__main__":
    while True:
        query = input("\nEnter your search query (or type 'exit'): ")

        if query.lower() == "exit":
            break

        search(query)

# D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m qdrant_db.search_vectors


# Suppose the user asks:

# battery issues
# ↓

# Convert query into an embedding:
# battery issues
# ↓
# [0.22, 0.88, ...]
# ↓

# Qdrant compares that vector with all stored vectors.
# ↓
# Returns the most similar reviews.