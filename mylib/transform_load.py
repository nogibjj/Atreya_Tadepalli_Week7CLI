"""
Transforms and Loads data into the Databricks database
Example:
team, W,L, W-L%, GB, Year, League
"""

import csv
import os
from dotenv import load_dotenv
from databricks import sql



#load the csv file and insert into a new databricks database
def load(dataset="data/mlb-test.csv"):
    #Transforms and Loads data into the Databricks database

    #prints the full working directory and path
    #print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    next(payload)
    filtered_payload = [row[0:3]+row[4:7] for row in payload]

    for row in filtered_payload:
        try:
            #row[3] = float(row[3])  # Assuming 'W-L%' is a float
            row[3] = int(row[3])    # Assuming 'GB' is an integer
        except ValueError:
            #row[3] = None
            row[3] = None
    load_dotenv()


    with sql.connect(
        server_hostname = os.getenv("SERVER_HOSTNAME"),
        http_path= os.getenv("DATABRICKS_HTTPPATH"),
        access_token= os.getenv("DATABRICKS_KEY")) as connection:
        with connection.cursor() as c:
    #cursor.execute("SELECT * FROM samples.nyctaxi.trips LIMIT 2")
    #result = cursor.fetchall()

    #for local connections
    #conn = sqlite3.connect('baseball.db')
    #c = conn.cursor()

            c.execute("DROP TABLE IF EXISTS baseball")
    #c.execute("CREATE TABLE baseball\
    #(team,W,L,GB,year,League)")
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS baseball (
                    team STRING,
                    W INTEGER,
                    L INTEGER,
                    GB INTEGER,
                    year INTEGER,
                    League STRING
                )"""
            )
            c.execute("SELECT * FROM baseball")
            result = c.fetchall()
            if not result:
                print("here")
                string_sql = """
                INSERT INTO baseball\
                 (team,W,L,GB,year,League)
                VALUES (?,?,?,?,?,?)
                """
    
                for row in filtered_payload:
                # Convert each element to the appropriate SQL representation
                # (e.g., wrap strings in single quotes and leave numbers as they are)
                    c.execute(string_sql,
                    [value if value is not None else None for value in row])

                connection.commit()
                print("Data inserted successfully.")
            else:
                print("Data already exists in the table. No new data inserted.")

            c.close()
            connection.close()
    return "Sucess!"

def load_second(dataset2="data/MLB.csv"):
    #Second dataset
    payload2 = csv.reader(open(dataset2, newline=''), delimiter=',')
    next(payload2)
    load_dotenv()

    with sql.connect(
        server_hostname = os.getenv("SERVER_HOSTNAME"),
        http_path= os.getenv("DATABRICKS_HTTPPATH"),
        access_token= os.getenv("DATABRICKS_KEY")) as connection:
        with connection.cursor() as c:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS mlb_baseball_1 (
                    Team STRING,
                    Salary INTEGER,
                    Winning INTEGER
                )
                """
            )
            c.execute("SELECT * FROM mlb_baseball_1")
            result_2 = c.fetchall()
            if not result_2:
                print("done")
                insert_sql = """
                INSERT INTO mlb_baseball_1\
                 (Team,Salary,Winning)
                VALUES (?,?,?)
                """
                for row in payload2:
                    c.execute(insert_sql,
                    [value if value is not None else None for value in row])

                connection.commit()
                print("Data inserted successfully.")
            else:
                print("Data already exists in the table. No new data inserted.")

            c.close()
            connection.close()
    return "Success!"


if __name__=="__main__":
    load()
    load_second()


