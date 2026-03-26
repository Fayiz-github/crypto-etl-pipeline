from extract import fetch_crypto
from transform import transform_data
from load import create_table, load_to_db

def run_pipeline():
    print("Extracting data...")
    data = fetch_crypto()

    print("Transforming data...")
    df = transform_data(data)

    print("Loading data...")
    create_table()
    load_to_db(df)

    print("ETL process completed!")

if __name__ == "__main__":
    run_pipeline()