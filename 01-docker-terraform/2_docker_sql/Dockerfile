FROM python:3.9.1

# Instalar wget e outras dependências, se necessário
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar as bibliotecas Python necessárias
RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app
COPY ingest_data.py ingest_data.py 

# Definir variáveis de ambiente
ENV URL_TAXI="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
ENV URL_ZONE="https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"


CMD ["python", "ingest_data.py", \
     "--user=postgres", \
     "--password=postgres", \
     "--host=pgdatabase", \
     "--port=5432", \
     "--db=ny_taxi", \
     "--taxi_table_name=yellow_taxi_trips", \
     "--zone_table_name=zones", \
     "--url_taxi=${URL_TAXI}", \
     "--url_zone=${URL_ZONE}"]
