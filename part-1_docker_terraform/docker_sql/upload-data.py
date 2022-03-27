#!/usr/bin/env python
# coding: utf-8

import os
import argparse
from time import time
import pandas as pd
import terality as te
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'

    te.configure(email="salamiolokun@gmail.com")

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{db}')

    taxi_data = te.read_csv(csv_name, parse_dates=[
                            'tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    taxi_df = taxi_data.to_pandas()

    taxi_df.head(n=0).to_sql(name=table_name, con=engine,
                             if_exists='replace', index=False)
    taxi_df.to_sql(name=table_name, con=engine,
                   if_exists="append", chunksize=100000, index=False)

    print("Finished ingesting data into postgres database")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True,
                        help='user name for postgres')
    parser.add_argument('--password', required=True,
                        help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True,
                        help='database name for postgres')
    parser.add_argument('--table_name', required=True,
                        help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)
