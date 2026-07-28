from etl.clean_products import clean_products
from etl.clean_news import clean_news
from etl.clean_comments import clean_comments
from etl.clean_reviews import clean_reviews
from etl.feature_engineering import feature_engineering
from etl.merge_data import merge_data


def run_etl():

    clean_products()
    clean_news()
    clean_comments()
    clean_reviews()

    feature_engineering()

    merge_data()

    print("\nETL Completed Successfully!")


if __name__ == "__main__":
    run_etl()


# cmd--> D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m etl.run_etl