import requests

print("PumpHunter AI Started")

try:
    url = "https://api.binance.com/api/v3/ticker/24hr"
    data = requests.get(url, timeout=20).json()

    coins = sorted(
        data,
        key=lambda x: float(x["priceChangePercent"]),
        reverse=True
    )[:10]

    print("\nTop Movers:\n")

    for c in coins:
        print(
            f'{c["symbol"]} | {c["priceChangePercent"]}% | Vol:{c["quoteVolume"]}'
        )

except Exception as e:
    print(e)
