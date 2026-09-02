import requests

coin = "bitcoin"

# Get hourly prices for the last 7 days
response = requests.get(
    f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart",
    params={"vs_currency": "usd", "days": "7"}
)

data = response.json()

# Each item is [time, price] -> we only need the prices
prices = [p[1] for p in data["prices"]]

current = prices[-1]                      # last price = now
sma24 = sum(prices[-24:]) / len(prices[-24:])   # average of last 24 hours

print(f"Coin: {coin.upper()}")
print(f"Current price : ${current:,.2f}")
print(f"24h average   : ${sma24:,.2f}")
print("-" * 45)

# --- Simple trend strategy ---
if current > sma24 * 1.01:
    print("Signal: UPTREND  -> look for BUY")
elif current < sma24 * 0.99:
    print("Signal: DOWNTREND -> look for SELL")
else:
    print("Signal: SIDEWAYS  -> WAIT")