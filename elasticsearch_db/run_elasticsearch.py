from elasticsearch_db.create_index import create_index
from elasticsearch_db.upload_documents import upload_documents


def run():

    print("=" * 60)
    print("Setting up Elasticsearch")
    print("=" * 60)

    create_index()
    upload_documents()

    print("\nElasticsearch Setup Completed Successfully!")

if __name__ == "__main__":
    run()

# cmd--> D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m elasticsearch_db.run_elasticsearch