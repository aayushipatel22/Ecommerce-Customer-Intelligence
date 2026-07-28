import os

def create_folder(folder_name):
    """
    Create folder if it doesn't exist.
    """
    os.makedirs(folder_name, exist_ok=True)