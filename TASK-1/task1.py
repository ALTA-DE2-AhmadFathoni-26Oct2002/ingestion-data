import pandas as pd

path = "dataset/yellow_tripdata_2020-07.csv"

#1. membuat dataframe
df = pd.read_csv (path, sep=',')

#2. menampilkan info kolom
print(df.info())

#2. rename nama kolom
df = df.rename (
    columns= {'VendorID':'Vendor_ID', 'RatecodeID':'Ratecode_ID', 'PULocationID': 'PU_Location_ID', 'DOLocationID':'DO_Location_ID'}    
)

#3. menentukan top 10 dari passenger_count
top_10 = df.nlargest(10, 'passenger_count')
[['Vendor_ID, passenger_count', 'trip_distance','payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount', 'congestion_surcharge']]


#extra: menghapus nilai null dan infinite (diperlukan ketika ingin merubah data vendor_id dll ke int)
df = df.dropna()

#4. merubah object ke  datatime (atau timestamp)
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

#4. merubah tipe data ke interger
df['Vendor_ID']  = df['Vendor_ID'].astype(int)
df['passenger_count']  = df['passenger_count'].astype(int)
df['Ratecode_ID']  = df['Ratecode_ID'].astype(int)

#4. merubah object menjadi boolean

df['store_and_fwd_flag'] = df['store_and_fwd_flag'].replace(['N', 'Y'], [False, True])
df['store_and_fwd_flag'] = df['store_and_fwd_flag'].astype('boolean')

#4.mengecek tipe data
print(df.dtypes)




