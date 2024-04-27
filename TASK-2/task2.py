import pandas as pd
from sqlalchemy import create_engine

path = 'dataset/yellow_tripdata_2023-01.parquet'

#1,2. memuat data parquet ke data frame dan menggunakan fastparquet library
df = pd.read_parquet (path, engine='fastparquet')

#melihat info dari data
print(df.info())

#3. membersikan dataset (merubah object menjadi boolean)
df['store_and_fwd_flag'] = df['store_and_fwd_flag'].replace(['N', 'Y'], [False, True])
df['store_and_fwd_flag'] = df['store_and_fwd_flag'].astype('boolean')

#4.membuat koneksi dengan postgres
def get_postgres_con():
    user = 'postgres'
    password = 'admin'
    host = 'localhost'
    database = 'mydb'
    port = 5439

    conn_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(conn_string)
    return engine

#4. me-define datatype schema menggunakan metode to_sql 
def load_to_postgres():
    df.to_sql(name='task2', con=conn, schema='public', if_exists='replace', index='False', dtype=None)
   
#5. me-ingest data ke postgres
conn = get_postgres_con()
to_postgres = load_to_postgres()
print (to_postgres)