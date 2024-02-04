#!/usr/bin/env python
# coding: utf-8

import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine

import pyarrow.parquet as pq

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    taxi_table_name = params.taxi_table_name
    zone_table_name = params.zone_table_name
    url_taxi = params.url_taxi
    url_zone = params.url_zone
   
    taxi_data_file = "taxi_data.parquet"
    zone_data_file = "zone_data.csv"

    os.system(f"wget {url_taxi} -O {taxi_data_file}")
    os.system(f"wget {url_zone} -O {zone_data_file}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_zones = pd.read_csv(zone_data_file)

    df_taxi = pq.read_table(taxi_data_file).to_pandas()
    df_taxi.to_csv('output.csv', index=False)    

    df_taxi_iter = pd.read_csv("output.csv", iterator=True, chunksize=100000)

    df_taxi_next = next(df_taxi_iter)

    df_taxi_next.tpep_pickup_datetime = pd.to_datetime(df_taxi.tpep_pickup_datetime)
    df_taxi_next.tpep_dropoff_datetime = pd.to_datetime(df_taxi.tpep_dropoff_datetime)

    df_zones.to_sql(name=zone_table_name, con=engine, if_exists='replace')

    print('Zone data ingested into the postgres database')


    df_taxi_next.head(n=0).to_sql(name=taxi_table_name, con=engine, if_exists='replace')

    df_taxi_next.to_sql(name=taxi_table_name, con=engine, if_exists='append')


    while True: 

        try:
            t_start = time()
            
            df = next(df_taxi_iter)

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=taxi_table_name, con=engine, if_exists='append')

            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))

        except StopIteration:
            if os.path.exists(taxi_data_file) and os.path.exists('output.csv'):
                os.remove(taxi_data_file)
                os.remove('output.csv')
            print("Finished ingesting data into the postgres database")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--taxi_table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--zone_table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url_taxi', required=True, help='url of the parquet file')
    parser.add_argument('--url_zone', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)