## SQLite Lab - Advanced Operations

## Table of Contents

- [Purpose](#purpose)
- [Additional Requirements](#Requirements)
- [Data](#data)
- [Upload_Process](#Upload_Process)
- [Query](#query)
- [Contributing](#contributing)
- [License](#license)


## Purpose:

* In this project, I have established a connection to Databricks, have prepared multiple tables, and have undertaken a join and sort operation in combination. I have then logged this SQL operation and its result in a markdown file. The purpose is ultimately to conduct ETL operations to load data into an external database, then source that data to conduct operations and retrieve results.

## Requirements:

* To conduct this process of connecting to an external database, we need to install a couple dependencies: Databricks SQL connector and Python DotEnv.

## Data:

* While I mimicked the Miniproject 5 in terms of CRUD methods, I chose to review a new domain of data: MLB records.
* Specifically, I chose to perform operations using two related sets of data.
* The first includes the records of MLB teams across five separate years, with each team's record for a given year assigned a separate record.
* The second involves the name of the team, the salary for the team, and its winning percentage, expressed as a whole number from 1-100.

## Upload_Process

* Firstly, I extracted the data from the github links which contained both csv files using the extract.py file. Following extraction, these datasets were then assigned to the Data folder within the project.
* To load the data to Databricks, I prepared two load functions, one for each dataset. These ultimately were stored in the same database, but involved writing two different tables: Baseball and Mlb-baseball-1.
* To connect properly, I make use of the server hostname, Databricks HTTP path, and Databricks key. These are stored in a .env file within the project, and are cited in establishing a connection.
* For the first dataset, I filtered out the dataset slightly- due to the presence of a hyphen, one column, "W-L%" was giving errors, so I removed this column from the table.
* Ultimately, a For loop is used to insert each row of the dataset into the database.
* If the data exists already, the data is not pushed; otherwise, it is pushed to the database environment, and the connection is closed.

## Query

* In my query file, I prepared three different types of SQL operations: join, aggregation, and sort.
* In my join method, while I have prepared three different queries, for the purpose of this exercise, I have written my complex query in this method. Therefore, by calling join, I am executing the query titled "test-query".
* Ultimately, the data from the mlb-baseball-1 table is joined to the right of the baseball table by using a common variable, team name, which exists in both datasets.
* Aggregation counts the number of instances of a provided team within the baseball dataset. In this event, I set up the function to count the instances of the team "Arizona Diamondbacks" within the team name.
* The sort_db function sorts a database along a provided column. In this case, I specified that the mlb-baseball-1 table should be sorted according to winning percentage.
* For each of these functions, I have included a log_query function which records the SQL query, as well as the output upon executing the query.
* These functions are ultimately called in the \`main.py\` file.

## Test_Query_and_Expected_Results 

* The test query which is ultimately executed when running join involves a combination of operations. Specifically, in this query, I would like to order the teams from highest to lowest salary, and average the winning percentage to ultimately understand if payroll may impact winning.
* To do so, the test query joins the mlb-baseball-1 columns to the right of the baseball columns, and matches along team name. All results are subsequently grouped by team, and only the team, average salary, and average winning are reported.
* Below are the top five teams in terms of salary.
| state                  | Salary              | Winning_Pct           |
|-------------------     |---------------------|-----------------------|
| New York Yankees       | 7789235             | 52%                   |
| Los Angeles            | 4851538             | 52%                   |
| Philadelphia Phillies  | 2056721             | 45%                   |
| Boston Red Sox         | 490463              | 59%                   |
| Detroit Tigers         | 520111              | 57%                   |


* What insights or new knowledge did you gain from querying the SQLite database?
* How can SQLite and SQL help make data analysis more efficient? What are the limitations?
* What AI assistant did you use and how did it compare to others you've tried? What are its strengths and weaknesses?
* 
* If you could enhance this lab, what would you add or change? What other data would be interesting to load and query?

##### Challenge Exercises

* Add more transformations to the data before loading it into SQLite. Ideas: join with another dataset, aggregate by categories, normalize columns.
* Write a query to find correlated fields in the data. Print the query results nicely formatted.
* Create a second table in the SQLite database and write a join query with the two tables.
* Build a simple Flask web app that runs queries on demand and displays results.
* Containerize the application using Docker so the database and queries can be portable






[query result here](query_log.md)


