import requests

def fetch_crypto():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd"}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error:", response.text)
        return []

    data = response.json()

    if isinstance(data, dict):
        print("API Error:", data)
        return []

    return data


if __name__ == "__main__":
    crypto = fetch_crypto()

    if crypto:
        for coin in crypto[:3]:
            print({
                "id": coin["id"],
                "name": coin["name"],
                "price": coin["current_price"]
            })
    else:
        print("No data received")