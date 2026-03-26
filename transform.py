import pandas as pd

def transform_data(api_data):
    df = pd.DataFrame(api_data)

    # Select required columns
    df = df[["id", "name", "current_price", "high_24h"]]

    # Remove missing values
    df.dropna(inplace=True)

    # Feature engineering: price change %
    df["price_change_pct"] = (
        (df["current_price"] - df["high_24h"]) / df["high_24h"]
    ) * 100

    # Remove duplicates
    df.drop_duplicates(subset=["id"], inplace=True)

    return df

if __name__ == "__main__":
    from extract import fetch_crypto

    print("Fetching data...")
    data = fetch_crypto()

    print("Transforming data...")
    df = transform_data(data)

    print(df.head(20))