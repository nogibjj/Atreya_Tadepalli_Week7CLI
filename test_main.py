
"""
Test goes here

"""
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_query,read_query,\
update_query,delete_query

def test_extract():
    extracted_data = extract()
    assert extracted_data == "mlb-test.csv"


def test_transform_load():
    loaded_db = load()
    assert loaded_db == "baseball.db"

def test_create():
    assert create_query() \
    == "New row inserted successfully"


def test_read():
    assert read_query() == "Success"


def test_update():
    assert update_query(80,63,"Boston Red Sox") == "Updated successfully"


def test_delete():
    assert delete_query() == "Deleted successfully"
