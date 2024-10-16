"""Query the database"""

import sqlite3


def create_query():
    """Query the database to insert a new row within the baseball table"""
    conn = sqlite3.connect("baseball.db")
    cursor = conn.cursor()
    """Create a new entry"""
    cursor.execute(
        """

        INSERT INTO baseball 
        (team,W,L,"W-L%",GB,year,League) 
        VALUES ("Durham Bulls", 100,40,.743,8,2018,"MLB")
        """
    )
    conn.commit()
    conn.close()
    return "New row inserted successfully"

def read_query():
    """Query the database for the top 20 rows of the baseball table"""
    conn = sqlite3.connect("baseball.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM baseball LIMIT 20")
    print("Top 20 rows of the Baseball table")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("Success")

def update_query(wins,losses,team_name):
    """Update the records included within the Ubertrips database"""
    conn = sqlite3.connect("baseball.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE baseball SET W=?, L=? \
    WHERE team = ? AND year=2018" , \
    (wins, losses, team_name))
    print("Data Update")
    conn.commit()
    conn.close()
    print("Updated successfully")

def delete_query():
    """Delete the record containing the provided team name and year"""
    conn = sqlite3.connect("baseball.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM baseball WHERE team = ? AND year = ?",\
                    ("Atlanta Braves", 2018))
    deleted = cursor.fetchall()
    conn.commit()
    print("Deleting data:")
    print(deleted)
    conn.close()
    print("Deleted successfully")

if __name__ == "__main__":
    create_query()
    read_query()
    update_query(80,63,"Boston Red Sox")
    delete_query()

