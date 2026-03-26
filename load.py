import psycopg2
from config import DB_CONFIG


# Function to create table if it doesn't exist
def create_table():
    # Connect to PostgreSQL using credentials from .env
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # SQL query to create table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS crypto_data (
        id TEXT PRIMARY KEY,              -- unique identifier
        name TEXT,                        -- cryptocurrency name
        current_price FLOAT,              -- current price
        price_change_pct FLOAT            -- calculated price change %
    );
    """)

    # Save changes
    conn.commit()

    # Close connection
    cur.close()
    conn.close()


# Function to insert data into database
def load_to_db(df):
    # Connect to database
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    count = 0  # To track number of inserted rows

    # Loop through each row in DataFrame
    for _, row in df.iterrows():

        # Insert query with conflict handling
        cur.execute("""
        INSERT INTO crypto_data (id, name, current_price, price_change_pct)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;   -- avoid duplicate records
        """, (
            row["id"],                   # crypto id
            row["name"],                 # crypto name
            row["current_price"],        # current price
            row["price_change_pct"]      # calculated value
        ))

        count += 1  # increment counter

    # Commit all inserts
    conn.commit()

    # Close connection
    cur.close()
    conn.close()

    # Print how many rows processed
    print(f"Inserted {count} rows")