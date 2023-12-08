import pathlib
import sqlite3
import pandas as pd


path = pathlib.Path().cwd() # use pathlib to get current working directory


def create_database(db_name, filename, table_name):
    file_path = path / filename  # create a path to the data file

    con = sqlite3.connect(db_name)# create a connection to the database
    cursor = con.cursor()# create a cursor

    students = pd.read_csv(file_path) # read in the data 
    students.to_sql(table_name, con, index = False, if_exists = 'replace' )# insert the data into the specified table 

    results = cursor.execute(f'SELECT * FROM {table_name} ').fetchall() # execute a select statement as f-string and print results to verify insertion
    print (results)
    
    con.commit # commit the changes to the database
    con.close# close the connection


if __name__=="__main__":
    db_name = "database.db"
    filename = "goals.csv"
    table_name = "goal_table"
    create_database(db_name, filename, table_name)