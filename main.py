"""
ETL-Query script
"""
from mylib.extract import extract, extract_second
from mylib.transform_load import load, load_second
from mylib.query import create_query, read_query, update_query, delete_query, join, aggregation, sort_db

# Extract
print("Extracting data...")
extract()
extract_second()

# Transform and load
print("Transforming data...")
load()
load_second()

join()
aggregation()
sort_db()
# create
print("Creating data...")
create_query()

# read
print("Reading data...")
read_query()

# update
print("Updating data...")
update_query(80, 63, "Boston Red Sox")

# delete
print("Deleting data...")
delete_query()
