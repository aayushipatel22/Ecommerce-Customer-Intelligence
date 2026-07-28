from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Read News API Key
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
# REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
# REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")