from embeddings.generate_embeddings import generate_embeddings

def run():

    print("=" * 50)
    print("Generating Embeddings")
    print("=" * 50)

    generate_embeddings()

    print("\nEmbedding Generation Completed Successfully!")

if __name__ == "__main__":
    run()

# cmd --> D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m embeddings.run_embeddings