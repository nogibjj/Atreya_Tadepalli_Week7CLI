"""Query the database"""

import sqlite3
from databricks import sql
import os

def join():
    
    #Local connection syntax
    #baseball1=sqlite3.connect("baseball.db")
    with sql.connect(server_hostname = os.getenv("SERVER_HOSTNAME"),
                 http_path       = os.getenv("DATABRICKS_HTTPPATH"),
                 access_token    = os.getenv("DATABRICKS_KEY")) as baseball1:
        with baseball1.cursor() as baseball_cursor:

    #mlb=sqlite3.connect("baseball.db")
    #mlb_cursor=mlb.cursor()

            #For first database
            baseball_query = """
            SELECT b.team, b.W, b.L, b.League
            FROM baseball b
            ORDER BY b.team;
            """
            #baseball_cursor.execute(baseball_query)
            #baseball_results = baseball_cursor.fetchall()

            # For second database
            mlb_query = """
            SELECT s.Team, s.Salary, s.Winning
            FROM mlb_baseball_1 s;
            """
            #baseball_cursor.execute(mlb_query)

            #test query
            test_query = """
            SELECT baseball.team, 
            avg(mlb.Winning) AS winning_pct,
            avg(mlb.Salary) avg_payroll 
            FROM ids706_data_engineering.default.baseball AS baseball
            RIGHT JOIN ids706_data_engineering.default.mlb_baseball_1 AS mlb
            ON baseball.team = mlb.Team
            GROUP BY baseball.team
            ORDER BY avg_payroll DESC;
            """
            baseball_cursor.execute(test_query)
            # Fetch results
            test_results = baseball_cursor.fetchall()

    # Close connections
    baseball1.close()
    log_query(f"{test_query}",test_results)

    # Combine results
    #combined_results = []

    """for result in baseball_results:
        baseball_team, baseball_W,baseball_L, baseball_League= result
        mlb_info = [mlb1 for mlb1 in mlb_results if mlb1[0] == baseball_team]
        if mlb_info:
            mlb_Salary, mlb_Winning = mlb_info[0][1], mlb_info[0][2]
            combined_results.append((baseball_team,baseball_W,baseball_L\
                                     , baseball_League, mlb_Salary, mlb_Winning))
"""
    #print(combined_results)

    return "Success-1!"
    

def aggregation():
    #Databricks connection
    with sql.connect(server_hostname = os.getenv("SERVER_HOSTNAME"),
                 http_path= os.getenv("DATABRICKS_HTTPPATH"),
                 access_token = os.getenv("DATABRICKS_KEY")) as baseball_1:
        with baseball_1.cursor() as baseball_cursor:

    #For local use
    #baseball_1 = sqlite3.connect("baseball.db")
    #baseball_cursor = baseball_1.cursor()

    # Execute SQL query
            query = """
            SELECT team, COUNT(*) as original_count
            FROM baseball
            WHERE team="Arizona Diamondbacks"
            GROUP BY team;
            """
            baseball_cursor.execute(query)

            # Fetch result
            result = baseball_cursor.fetchall()

            # Close connection
            baseball_1.close()

            print(result)

    return result

def sort_db():
    

    #Databricks connection
    with sql.connect(server_hostname = os.getenv("SERVER_HOSTNAME"),
                 http_path       = os.getenv("DATABRICKS_HTTPPATH"),
                 access_token    = os.getenv("DATABRICKS_KEY")) as baseball_2:
        with baseball_2.cursor() as cursor:

    # Local connection to the database
    #mlb2 = sqlite3.connect("baseball.db")
    #cursor = mlb2.cursor()

    # Arrange teams by Winning percentage
            query = """
            SELECT team, Salary,Winning
            FROM mlb_baseball_1
            ORDER BY Winning DESC;
            """
            cursor.execute(query)

            # Fetch results
            results = cursor.fetchall()

            # Close connection
            baseball_2.close()

            print(results)

    return results


LOG_FILE = "query_log.md"

def log_query(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")
    

    
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
    return "Success"

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
    return "Updated successfully"

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
    return "Deleted successfully"

if __name__ == "__main__":
    create_query()
    read_query()
    update_query(80,63,"Boston Red Sox")
    delete_query()
    join()
    aggregation()
    sort_db()

