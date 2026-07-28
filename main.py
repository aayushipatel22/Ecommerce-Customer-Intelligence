from collection.fetch_products import fetch_products
from collection.fetch_news import fetch_news
from collection.fetch_comments import fetch_comments
from collection.fetch_reviews import fetch_reviews


def main():

    print("=" * 50)
    print("Starting Data Collection")
    print("=" * 50)

    fetch_products()
    print()

    fetch_news()
    print()

    fetch_comments()
    print()

    fetch_reviews()
    print("\nData Collection Completed Successfully")


if __name__ == "__main__":
    main()