"""
Extract a dataset from a URL like Kaggle
or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url="https://raw.githubusercontent.com/\
            RafaganCarvalho/CourseraMichiganCourses/refs/\
            heads/main/Introduction%20to%20Data%20Science/\
            assignments/assignment4/assets/mlb.csv", 
            file_path="mlb-test.csv",
            directory="data",
):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path


def extract_second(url="https://gist.githubusercontent.com/xav\
                   ier-moreno/5cc951dce9af4c6c6655/raw/feb35d621ac8c\
                   bf20bfd36266fbd779e22016158/MLB.csv", 
            file_path="MLB.csv",
            directory="data",
):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path
