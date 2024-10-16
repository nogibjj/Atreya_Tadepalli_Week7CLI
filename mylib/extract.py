"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url="https://raw.githubusercontent.com/\
            RafaganCarvalho/CourseraMichiganCourses/refs/heads/main/Introduction%20to%20Data%20Science/\
            assignments/assignment4/assets/mlb.csv", 
            file_path="data/mlb-test.csv",
            directory="data",
):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



