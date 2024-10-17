"""
ETL-Query script
"""
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_query, read_query, update_query, delete_query

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

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
