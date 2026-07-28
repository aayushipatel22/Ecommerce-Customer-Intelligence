import requests
import pandas as pd

from utils.helper import create_folder


def fetch_products():

    print("Fetching Products...")

    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data) #Convert JSON into a table

    create_folder("data/raw")

    df.to_csv("data/raw/products.csv", index=False)

    print("Products Saved Successfully")


if __name__ == "__main__":
    fetch_products()



