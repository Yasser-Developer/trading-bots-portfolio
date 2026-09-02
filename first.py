# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

import requests

coins = ["bitcoin", "ethereum", "solana", "the-open-network", "dogecoin"]

# همه قیمت‌ها رو با یه درخواست می‌گیریم (نه ۵ تا!)
response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price",
    params={
        "ids": ",".join(coins),
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
)

data = response.json()
print("📊 قیمت لحظه‌ای ارزهای دیجیتال:\n")

for coin in coins:
    if coin in data:   # ← چک می‌کنیم داده اومده یا نه (جلوگیری از کرش!)
        price = data[coin]["usd"]
        change = data[coin].get("usd_24h_change", 0)
        emoji = "🟢" if change > 0 else "🔴"
        name = "TON" if coin == "the-open-network" else coin.upper()
        print(f"{emoji} {name}: ${price:,} ({change:.2f}%)")
    else:
        print(f"⚠️ {coin}: داده نیومد (اشکال از APIـه، نه کد تو!)")

print("\n✅ تمام شد!")