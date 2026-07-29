from qdrant_db.create_collection import create_collection
from qdrant_db.upload_vectors import upload_vectors


def run():

    create_collection()

    upload_vectors()

    print("\nQdrant Setup Completed Successfully!")

if __name__ == "__main__":
    run()

# Qdrant stores: Vector + Payload

# cmd --> D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m qdrant_db.run_qdrant
# D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m qdrant_db.search_vectors

# python -m qdrant_db.search_vectors