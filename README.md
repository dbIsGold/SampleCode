# The Repo contains some Sample Code for SQL and Python
_The main diectory contains 3 pdf files_
1. **SqlSample.pdf**  - Sample SQL Code and Db schema . You can find more details on the query below in the details for **SQL** subdirectory. The PDF also contains the output generated by these queries. these queries were run on opensource postgres database.
2. **TicTacToe-PythonCode-ToPlayGame.pdf** - The python source code to play a game of Tic-Tac-Toe with your computer. The PDF also contains sample of Output of a few games. You can find more about the source code and the output generated in the sub directory **Python**
3. **DB-talking-To-Other-Dbs.pdf** - Contains a small disciption of some of the methods I have used to connect databases where data flows between one db to another.

### SQL - Sample SQLs and everything to run them
1. Install postgres database by downloading appropriate verison for your operating-system from _https://www.postgresql.org/download/_
2. Create schema and load the data used in the query by using the script **create_load.sql**
3. Run various Queries;</br>
     a. **query1-join.sql** - Example of multi query join and where clause</br>
     b. **query2-groupbyHaving.sql** - The query is an example of group-by, having and order-by clause</br>
     c. **query3-windowFunction.sql** - This query showcases the powerful fnctionality of windows function where it generates a running total of revenue over a period</br>

### Python - Sample Python Code with a fun game of Tic-Tac-Toe
_You can play a game of tic-tac-toe with your computer where the computer picks a spot between 1-9 randomly to place a O. You, however, can enter the spot where you want to place your X_
1. Install Python for your OS https://www.python.org/downloads/ (I installed version 3.12)
2. Download the code **TicTacToe.py**
3. Change directory to the directory where the .py is placed and issue command _python ./TicTacToe.py
4. **OR** install VsCode, Jupyter or any other IDE and run the file directly from the IDE
