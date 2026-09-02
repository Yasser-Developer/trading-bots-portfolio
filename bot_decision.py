# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import requests

coin = "bitcoin"

response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price",
    params={
        "ids": coin,
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
)

data = response.json()
price = data[coin]["usd"]
change = data[coin]["usd_24h_change"]

print(f"💰 BTC price: ${price:,}")
print(f"📉 24h change: {change:.2f}%")
print("-" * 45)

# --- The bot makes its FIRST decision! ---
if change <= -1:
    print("🟢 Decision: BUY (big drop = possible opportunity!)")
elif change >= 1:
    print("🔴 Decision: SELL (big pump = take profit!)")
else:
    print("⚪ Decision: WAIT (no clear signal)")