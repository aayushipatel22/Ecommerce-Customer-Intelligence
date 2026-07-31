from elasticsearch_db.elastic_client import es

INDEX_NAME = "customer_reviews"

# def search(query):

#     response = es.search(
#         index=INDEX_NAME,
#         query={
#             "match": {
#                 "review_text": query
#             }
#         },
#         size=5
#     )

#     print("\nTop Results\n")

#     for hit in response["hits"]["hits"]:

#         data = hit["_source"]

#         print("-" * 60)
#         print(f"Score      : {hit['_score']:.4f}")
#         print(f"Review     : {data['review_text']}")
#         print(f"Sentiment  : {data['sentiment']}")
#         print(f"Source     : {data['source']}")


def search(query, limit=5):

    response = es.search(
        index=INDEX_NAME,
        query={
            "match": {
                "review_text": query
            }
        },
        size=limit
    )

    results = []

    print("\nTop Results\n")

    for hit in response["hits"]["hits"]:

        data = hit["_source"]

        print("-" * 60)
        print(f"Score      : {hit['_score']:.4f}")
        print(f"Review     : {data['review_text']}")
        print(f"Sentiment  : {data['sentiment']}")
        print(f"Source     : {data['source']}")

        results.append(
            {
                "review_text": data["review_text"],
                "sentiment": data["sentiment"],
                "source": data["source"],
                "score": hit["_score"],
            }
        )

    return results

if __name__ == "__main__":

    while True:

        query = input("\nEnter search query (or exit): ")

        if query.lower() == "exit":
            break

        search(query)

# cmd--> D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m elasticsearch_db.search_documents