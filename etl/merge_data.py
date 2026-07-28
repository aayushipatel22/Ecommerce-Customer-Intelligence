import pandas as pd


def merge_data():

    print("Creating Final Dataset...")

    # Read cleaned datasets
    reviews = pd.read_csv("data/cleaned/reviews_clean.csv")
    comments = pd.read_csv("data/cleaned/comments_clean.csv")

    # Add source column
    reviews["source"] = "review"
    comments["source"] = "comment"

    # Rename comments column to match reviews
    comments = comments.rename(columns={"body": "review_text"})

    # Add missing columns to comments
    comments["rating"] = None
    comments["review_length"] = comments["review_text"].astype(str).apply(
        lambda x: len(x.split())
    )
    comments["rating_category"] = "Unknown"

    # Select columns in the same order
    comments = comments[
        [
            "review_text",
            "rating",
            "review_length",
            "rating_category",
            "source",
        ]
    ]

    # Select the same columns from reviews
    reviews = reviews[
        [
            "review_text",
            "rating",
            "review_length",
            "rating_category",
            "source",
        ]
    ]

    # Merge both datasets
    final_df = pd.concat([reviews, comments], ignore_index=True)

    # Save final dataset
    final_df.to_csv("data/cleaned/final_dataset.csv", index=False)

    print("Final Dataset Created Successfully")


if __name__ == "__main__":
    merge_data()














# import pandas as pd


# def merge_data():

#     print("Creating Final Dataset...")

#     reviews = pd.read_csv("data/cleaned/reviews_clean.csv")

#     comments = pd.read_csv("data/cleaned/comments_clean.csv")

#     reviews["source"] = "review"
#     comments["source"] = "comment"

#     # Standardize the text column name
#     comments = comments.rename(columns={"body": "review_text"})

#     comments = comments[["review_text", "source"]]
#     reviews = reviews[["review_text", "rating", "source"]]

#     final_df = pd.concat([reviews, comments], ignore_index=True)

#     final_df.to_csv("data/cleaned/final_dataset.csv", index=False)

#     print("Final Dataset Created Successfully")


# if __name__ == "__main__":
#     merge_data()