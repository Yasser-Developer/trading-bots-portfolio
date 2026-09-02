import requests

coin = "bitcoin"

response = requests.get(
    f"https://api.coingecko.com/api/v3/coins/{coin}/ohlc",
    params={"vs_currency": "usd", "days": "1"}
)

candles = response.json()

green = 0
red = 0

for c in candles:
    open_price = c[1]
    close = c[4]
    if close > open_price:
        green += 1    # green = green + 1
    else:
        red += 1

total = green + red
print(f"Green candles: {green}")
print(f"Red candles:   {red}")
print("-" * 40)

if green > red:
    print(f"Buyers ruled the day ({green} of {total} candles)")
elif red > green:
    print(f"Sellers ruled the day ({red} of {total} candles)")
else:
    print("Perfectly balanced market!")