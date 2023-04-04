import requests
import time

# Set the cryptocurrency symbols to retrieve data for
symbols = ['bitcoin', 'ethereum', 'cardano']

# Set the CoinGecko API endpoint
endpoint = 'https://api.coingecko.com/api/v3/simple/price'

# Create a dictionary to store the previous prices for each cryptocurrency
previous_prices = {}

while True:
    # Retrieve the cryptocurrency data from CoinGecko for each symbol
    data = {}
    for symbol in symbols:
        response = requests.get(f'{endpoint}?ids={symbol}&vs_currencies=usd')
        data[symbol] = response.json()[symbol]['usd']

    # Print the current prices of each cryptocurrency
    print("Current prices:")
    for symbol, price in data.items():
        if symbol not in previous_prices:
            previous_prices[symbol] = price
        if price > previous_prices[symbol]:
            trend = "up"
        elif price < previous_prices[symbol]:
            trend = "down"
        else:
            trend = "stable"
        print(f"{symbol}: ${price:.2f} USD ({trend})")
        previous_prices[symbol] = price
    
    # Wait for 10 seconds before updating the prices again
    time.sleep(5)
