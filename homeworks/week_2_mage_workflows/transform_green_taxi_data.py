if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: rows with zero trip distance: {data['trip_distance'].isin([0]).sum()}")

    df = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date

    df.rename(columns={'VendorID': 'vendor_id', 'RatecodeID': 'ratecode_id', 
    'PULocationID': 'pu_location_id', 'DOLocationID': 'do_location_id'}, inplace=True)

    return df

@test
def vendor_id_valid(df) -> None:
    assert df['vendor_id'].isin([1, 2]).all(), 'vendor_id is one of the existing values'

@test
def test_zero_values(df) -> None:
    assert (df['passenger_count'] > 0).all(), 'passenger_count is greater than zero'
    assert (df['trip_distance'] > 0).all(), 'passenger_count is greater than zero'