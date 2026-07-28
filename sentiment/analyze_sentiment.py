import pandas as pd
from tqdm import tqdm

from sentiment.sentiment_model import sentiment_pipeline
from utils.helper import create_folder


def analyze_sentiment():

    print("Loading Dataset...")

    df = pd.read_csv("data/cleaned/final_dataset.csv")

    sentiments = []
    confidence_scores = []
    sentiment_scores = []

    tqdm.pandas()

    for text in tqdm(df["review_text"].fillna("")):    # Loop through every review.
        # Great quality--> Model--> Positive

        # result = sentiment_pipeline(str(text))[0]

        # sentiments.append(result["label"].capitalize())
        # confidence_scores.append(round(result["score"], 4))

        result = sentiment_pipeline(str(text))[0]

        # Get sentiment label
        label = result["label"].capitalize()

        # Store sentiment label
        sentiments.append(label)

        # Store confidence score
        confidence_scores.append(round(result["score"], 4))

        # Convert sentiment into numeric value
        if label == "Positive":
            sentiment_scores.append(1)
        elif label == "Negative":
            sentiment_scores.append(-1)
        else:
            sentiment_scores.append(0)

    # Add new columns
    df["sentiment"] = sentiments
    df["confidence_score"] = confidence_scores
    df["sentiment_score"] = sentiment_scores

    create_folder("data/processed")

    df.to_csv(
        "data/processed/ai_ready_dataset.csv",
        index=False,
    )

    print("\nSentiment Analysis Completed Successfully!")


if __name__ == "__main__":
    analyze_sentiment()