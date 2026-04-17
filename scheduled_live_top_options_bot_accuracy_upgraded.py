# ===========================
# SIMPLE LIVE OPTIONS BOT
# (EASY VERSION - WORKING)
# ===========================

import requests
import os
from datetime import datetime

ALPACA_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET = os.getenv("ALPACA_SECRET_KEY")

BASE_URL = "https://data.alpaca.markets"

HEADERS = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET
}

SYMBOLS = ["SPY", "QQQ", "AAPL", "TSLA", "NVDA"]

def get_price(symbol):
    url = f"{BASE_URL}/v2/stocks/{symbol}/bars/latest"
    r = requests.get(url, headers=HEADERS)
    data = r.json()
    return data.get("bar", {}).get("c", 0)

def simple_signal(price):
    # very basic logic (we will upgrade later)
    if price > 100:
        return "CALL"
    else:
        return "PUT"

def run_bot():
    print("Running bot at:", datetime.now())
    
    for symbol in SYMBOLS:
        try:
            price = get_price(symbol)
            signal = simple_signal(price)
            
            print(f"{symbol} | Price: {price} | Signal: {signal}")
            
        except Exception as e:
            print(f"{symbol} ERROR:", e)

if __name__ == "__main__":
    run_bot()