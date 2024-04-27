from sqlalchemy import create_engine
import pandas as pd

#membuat koneksi dengan source potgres
user = 'postgres'
password = 'pass'
port = 5438
database = 'store'
host = 'localhost'

conn_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(conn_string)

conn = engine.connect()

#memasukan data postgre ke dataframe
df_orders = pd.read_sql_table('orders', conn)

df_products = pd.read_sql_table('products', conn)

df_order_details = pd.read_sql_table('order_details', conn)

df_brands = pd.read_sql_table('brands', conn)

#membuat koneksi dengan citus
def get_postgres_con():
    user = 'postgres'
    password = 'pass'
    host = 'localhost'
    database = 'store'
    port = 15432

    conn_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(conn_string)
    return engine

#me-load ke citus
def load_to_postgres():
    df_orders.to_sql(name= 'orders_citus', con=con2, schema='public', if_exists='replace', index='False', dtype=None)

def load_to_postgres():
    df_products.to_sql(name= 'products_citus', con=con2, schema='public', if_exists='replace', index='False', dtype=None)

def load_to_postgres():
    df_order_details.to_sql(name= 'order_details_citus', con=con2, schema='public', if_exists='replace', index='False', dtype=None)

def load_to_postgres():
    df_brands.to_sql(name= 'brands_citus', con=con2, schema='public', if_exists='replace', index='False', dtype=None)

con2 = get_postgres_con()
to_postgres = load_to_postgres()
print (to_postgres)

