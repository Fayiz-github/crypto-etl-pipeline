# Crypto ETL Pipeline

## Overview

This project implements a complete ETL (Extract, Transform, Load) pipeline using Python. It collects real-time cryptocurrency data from the CoinGecko API, processes it, and stores it in a PostgreSQL database.

## Features

* Real-time data extraction from API
* Data cleaning and transformation using pandas
* PostgreSQL database integration
* Logging system for tracking execution
* Retry mechanism for handling failures
* Exception handling for robustness

## Tech Stack

* Python
* pandas
* requests
* psycopg2
* PostgreSQL

## ETL Flow

CoinGecko API → Extract → Transform → Load → PostgreSQL

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Configure environment variables in `.env`

3. Run the pipeline:
   python main.py

## Output

* Data stored in PostgreSQL table: `crypto_data`
* Logs stored in: `etl.log`

## Project Structure

* extract.py → API data extraction
* transform.py → Data cleaning and processing
* load.py → Database loading
* main.py → Pipeline orchestration
* config.py → Configuration management

## Screenshot

(Add your database screenshot here)

## Author

Mohamed Fayiz
