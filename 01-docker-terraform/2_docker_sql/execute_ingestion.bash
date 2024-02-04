URL_TAXI="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
URL_ZONE="https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"

python ingest_data.py \
  --user=postgres \
  --password=postgres \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --taxi_table_name=yellow_taxi_trips \
  --zone_table_name=yellow_taxi_trips \
  --url_taxi=${URL_TAXI} \
  --url_zone=${URL_ZONE}