import requests

response = requests.get(
    "https://api.coingecko.com/api/v3/coins/bitcoin/ohlc",
    params={"vs_currency": "usd", "days": "7"}
)
candles = response.json()

strategy_profit = 0.0   # our rule: enter after a GREEN candle
buyhold_profit  = 0.0   # always in market (for comparison)

for i in range(1, len(candles)):
    prev_open, prev_close = candles[i-1][1], candles[i-1][4]
    curr_open, curr_close = candles[i][1], candles[i][4]
    curr_change = (curr_close - curr_open) / curr_open * 100

    buyhold_profit += curr_change
    if prev_close > prev_open:      # signal from previous candle
        strategy_profit += curr_change

print(f"Buy & Hold : {buyhold_profit:+.2f}%")
print(f"Strategy   : {strategy_profit:+.2f}%")