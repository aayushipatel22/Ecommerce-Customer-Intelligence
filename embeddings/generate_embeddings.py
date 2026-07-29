import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer
from utils.helper import create_folder


def generate_embeddings():

    print("Loading AI Ready Dataset...")
    df = pd.read_csv("data/processed/ai_ready_dataset.csv")

    print("Loading Embedding Model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Generating Embeddings...")

    texts = df["review_text"].fillna("").tolist()

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    # Store embeddings as a list
    df["embedding"] = embeddings.tolist()

    create_folder("data/processed")

    df.to_pickle("data/processed/embedded_dataset.pkl")

    print("Embeddings Generated Successfully!")


if __name__ == "__main__":
    generate_embeddings()


# A CSV stores only text and numbers cleanly.

# An embedding looks like: [0.24, -0.91, 0.18, ...]
# Each row contains 384 numbers.

# Saving that to CSV is messy.

# So we use: df.to_pickle(...)