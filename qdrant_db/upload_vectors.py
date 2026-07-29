import pandas as pd
from qdrant_client.models import PointStruct
from qdrant_db.qdrant_client import client

COLLECTION_NAME = "customer_reviews"
BATCH_SIZE = 200


def upload_vectors():

    print("Loading Embedded Dataset...")

    df = pd.read_pickle("data/processed/embedded_dataset.pkl")

    print(f"Total Records: {len(df)}")

    for start in range(0, len(df), BATCH_SIZE):

        end = min(start + BATCH_SIZE, len(df))

        batch = []

        for idx, row in df.iloc[start:end].iterrows():

            batch.append(
                PointStruct(
                    id=int(idx),
                    vector=row["embedding"],
                    payload={
                        "review_text": row["review_text"],
                        "sentiment": row["sentiment"],
                        "source": row["source"],
                    },
                )
            )

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=batch,
            wait=True
        )

        print(f"Uploaded {end}/{len(df)}")

    print("\nVectors Uploaded Successfully!")


if __name__ == "__main__":
    upload_vectors()
















# import pandas as pd
# from qdrant_client.models import PointStruct
# from qdrant_db.qdrant_client import client

# COLLECTION_NAME = "customer_reviews"

# def upload_vectors():

#     print("Loading Embedded Dataset...")

#     df = pd.read_pickle(
#         "data/processed/embedded_dataset.pkl"
#     )

#     points = []

#     for idx, row in df.iterrows():

#         point = PointStruct(

#             id=int(idx),

#             vector=row["embedding"],

#             payload={                         #when Qdrant finds a similar vector, it returns the payload so you can display useful information
#                 "review_text": row["review_text"],
#                 "sentiment": row["sentiment"],
#                 "source": row["source"]
#             }
#         )
#         points.append(point)

#     client.upsert(

#         collection_name=COLLECTION_NAME,
#         points=points
#     )

#     print("Vectors Uploaded Successfully!")

# if __name__ == "__main__":
#     upload_vectors()

