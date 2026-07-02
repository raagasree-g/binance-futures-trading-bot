import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = Client(
    api_key=API_KEY,
    api_secret=API_SECRET,
    testnet=True
)