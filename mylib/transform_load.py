"""
Transforms and Loads data into the local SQLite3 database
Example:
team, W,L, W-L%, GB, Year, League
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="mlb-test.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    next(payload)
    filtered_payload = [row[:7] for row in payload]

    for row in filtered_payload:
        try:
            row[3] = int(row[3])
        except ValueError:
            row[3] = None  # Set to None or some other value if not an integer

    conn = sqlite3.connect('baseball.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS baseball")
    #c.execute("CREATE TABLE baseball\
    #(team,W,L,GB,year,League)")
    c.execute(
        """
        CREATE TABLE baseball (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team TEXT,
            W INTEGER,
            L INTEGER,
            "W-L%" REAL,
            GB INTEGER,
            year INTEGER,
            League TEXT
        )
        """
    )
    #insert
    c.executemany(
        """
        INSERT INTO baseball (
            team, 
            W, 
            L, "W-L%", GB, year, 
            League
        ) 
        VALUES (?, ?, ?, ?,?, ?, ?)
        """,
        filtered_payload,
    )
    conn.commit()
    conn.close()
    return "baseball.db"


def load_second(dataset="MLB.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    next(payload)
    filtered_payload = [row[:3] for row in payload]

    #for row in filtered_payload:
        #try:
            #row[3] = int(row[3])
        #except ValueError:
            #row[3] = None  # Set to None or some other value if not an integer

    conn = sqlite3.connect('baseball_2.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS baseball_2")
    #c.execute("CREATE TABLE baseball\
    #(team,W,L,GB,year,League)")
    c.execute(
        """
        CREATE TABLE baseball_2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Team TEXT,
            Salary INTEGER,
            Winning INTEGER
        )
        """
    )
    #insert
    c.executemany(
        """
        INSERT INTO baseball_2 (
            Team, 
            Salary, 
            Winning
        ) 
        VALUES (?, ?, ?)
        """,
        filtered_payload,
    )
    conn.commit()
    conn.close()
    return "baseball_2.db"

