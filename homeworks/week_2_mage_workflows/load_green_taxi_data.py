import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/"
    file_prefix = "green_tripdata_"
    years = [2020]
    months = [10, 11, 12]

    taxi_dtypes = {
                'VendorID': pd.Int64Dtype(),
                'passenger_count': pd.Int64Dtype(),
                'trip_distance': float,
                'RatecodeID':pd.Int64Dtype(),
                'store_and_fwd_flag':str,
                'PULocationID':pd.Int64Dtype(),
                'DOLocationID':pd.Int64Dtype(),
                'payment_type': pd.Int64Dtype(),
                'fare_amount': float,
                'extra':float,
                'mta_tax':float,
                'tip_amount':float,
                'tolls_amount':float,
                'improvement_surcharge':float,
                'total_amount':float,
                'congestion_surcharge':float
            }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    dfs = []

    for year in years:
        for month in months:
            path = f'{url}{file_prefix}{year}-{month}.csv.gz'
            df = pd.read_csv(path, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
            dfs.append(df)

    concated_df = pd.concat(dfs, axis=0, ignore_index=True)

    return concated_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

