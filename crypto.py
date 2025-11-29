import requests

# STEP 1: Get Top 20 Crypto Prices in USD
url_crypto = "https://api.coingecko.com/api/v3/coins/markets"
params_crypto = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 20,
    "page": 1
}
crypto_data = requests.get(url_crypto, params=params_crypto).json()

# STEP 2: Get USD → NPR Exchange Rate
fx_url = "https://open.er-api.com/v6/latest/USD"
fx_data = requests.get(fx_url).json()
usd_to_npr = fx_data["rates"]["NPR"]

# STEP 3: Print formatted crypto prices
print("\nTOP 20 CRYPTO PRICES (USD & NPR) \n")

for coin in crypto_data:
    name = coin["name"]
    usd_price = coin["current_price"]
    npr_price = usd_price * usd_to_npr

    print(f"{name}")
    print(f" → USD: ${usd_price}")
    print(f" → NPR: ₹{npr_price:.2f}")
    print("-" * 40)



