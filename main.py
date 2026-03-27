import logging
import time

from extract import fetch_crypto
from transform import transform_data
from load import create_table, load_to_db


# Configure logging
logging.basicConfig(
    filename="etl.log",  # log file name
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    try:
        logging.info("ETL pipeline started")

        # Step 1: Extract
        print("Extracting data...")
        data = fetch_crypto()
        logging.info("Data extracted successfully")

        if not data:
            raise Exception("No data received from API")

        # Step 2: Transform
        print("Transforming data...")
        df = transform_data(data)
        logging.info("Data transformed successfully")

        if df.empty:
            raise Exception("Transformed data is empty")

        # Step 3: Load
        print("Loading data...")
        create_table()
        load_to_db(df)
        logging.info("Data loaded into database successfully")

        print("ETL process completed!")
        logging.info("ETL pipeline completed successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("Error:", e)
        raise  # important for retry logic


# Retry mechanism
if __name__ == "__main__":
    max_retries = 3

    for attempt in range(max_retries):
        try:
            run_pipeline()
            break  # stop if success

        except Exception as e:
            print(f"Attempt {attempt + 1} failed")

            if attempt < max_retries - 1:
                print("Retrying in 5 seconds...\n")
                time.sleep(5)
            else:
                print("All retries failed.")
                logging.error("ETL failed after multiple attempts")