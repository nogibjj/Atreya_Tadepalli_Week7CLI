"""
Extract a dataset from a URL like Kaggle
or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests
import os


def extract(url="https://shorturl.at/Ewjp4", 
            file_path="data/mlb-test.csv",
            directory="data",
):
    """"Extract a url to a file path"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path


def extract_second(url="https://shorturl.at/LgVvR", 
            file_path="data/MLB.csv",
            directory="data",
):
    """"Extract a url to a file path"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path
