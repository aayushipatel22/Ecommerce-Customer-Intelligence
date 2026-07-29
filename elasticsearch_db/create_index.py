from elasticsearch_db.elastic_client import es

INDEX_NAME = "customer_reviews"

def create_index():

    if es.indices.exists(index=INDEX_NAME):
        print("Index already exists.")
        return

    mapping = {
        "mappings": {
            "properties": {
                "review_text": {"type": "text"},
                "sentiment": {"type": "keyword"},
                "source": {"type": "keyword"},
                "rating": {"type": "float"},
                "confidence_score": {"type": "float"},
                "sentiment_score": {"type": "integer"}
            }
        }
    }

    es.indices.create(
        index=INDEX_NAME,
        body=mapping
    )

    print("Index Created Successfully!")

if __name__ == "__main__":
    create_index()