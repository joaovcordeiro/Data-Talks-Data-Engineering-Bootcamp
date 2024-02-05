## Docker and SQL

## Commands

Criar pastas que seram os volumes

```bash
mkdir data_pgadmin
mkdir ny_taxi_postgres_data
```

### Running Postgres and PgAdmin with Docker

To make pgAdmin configuration persistent

```bash
sudo chown 5050:5050 data_pgadmin
```

```bash
docker-compose up
```

### Running Data Ingestion

Build the image

```bash
docker build -t taxi_ingest:v001 .
```

Run the container

```bash
docker run -it --network 2_docker_sql_pg-network taxi_ingest:v001
```
