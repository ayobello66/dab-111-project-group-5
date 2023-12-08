from flask import Flask, render_template
import sqlite3
import pathlib 
import pandas as pd 

base_path = pathlib.Path().cwd()
db_name = 'database.db'
db_path = base_path/ db_name


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/data')
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    run = cursor.execute('SELECT * FROM goal_table').fetchall()
    con.close
    return render_template('data_table_fillin.html', goal_table = run )
if __name__ == '__main__':
    app.run(debug = True)