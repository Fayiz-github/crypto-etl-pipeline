import requests
import logging


def fetch_crypto():
    try:
        logging.info("Starting data extraction from API")

        # API endpoint
        url = "https://api.coingecko.com/api/v3/coins/markets"

        # Query parameters
        params = {
            "vs_currency": "usd"
        }

        # Send request
        response = requests.get(url, params=params, timeout=10)

        # Check response status
        if response.status_code != 200:
            logging.error(f"API Error: {response.text}")
            return []

        # Convert to JSON
        data = response.json()

        # Validate data type
        if isinstance(data, dict):
            logging.error(f"Unexpected API response: {data}")
            return []

        logging.info(f"Successfully fetched {len(data)} records")

        return data

    except requests.exceptions.Timeout:
        logging.error("Request timed out")
        return []

    except requests.exceptions.ConnectionError:
        logging.error("Connection error while calling API")
        return []

    except Exception as e:
        logging.error(f"Unexpected error in extraction: {e}")
        return []


# Test block (optional)
if __name__ == "__main__":
    crypto = fetch_crypto()

    if crypto:
        print("Sample data:")
        for coin in crypto[:3]:
            print({
                "id": coin.get("id"),
                "name": coin.get("name"),
                "price": coin.get("current_price")
            })
    else:
        print("No data received")