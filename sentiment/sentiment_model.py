from transformers import pipeline

print("Loading Sentiment Model... (This may take a minute the first time)")

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    truncation=True,
)

# pipeline(): This loads a pretrained AI model.
# Review Text
    #   │
    #   ▼
# Pretrained AI Model
    #   │
    #   ▼
# Positive / Neutral / Negative

print("Model Loaded Successfully!")