import os
from flask import(
    Flask, render_template, request, redirect, session
)
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

#Initialize app
app = Flask(__name__)

#Query code
username = 'godenmyqjrmzoe'
password = '673e2f643ed4ddbe58c111219261e6872457e45e34e34c617efa029f10429c0f'
host = 'ec2-54-83-137-206.compute-1.amazonaws.com'
db = 'dc995n2umb789o'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}/{db}')

#adapted from: https://stackoverflow.com/questions/52644035/how-to-show-a-pandas-dataframe-into-a-existing-flask-html-table
@app.route("/", methods=("POST", "GET"))
def home():
    if request.method == "POST":
       # getting input with name = school_name in HTML form
       school = request.form.get("school_name")
       df = pd.read_sql_query(f"select * from school_geo where institution_name ilike '%%{school}%%'", con=engine)
       return render_template("index.html", tables = [df.to_html(classes='data')], titles = df.columns.values)
    
    else:
        df = pd.Dataframe()
        return render_template("index.html", tables = [df.to_html(classes='data')], titles = df.columns.values)

    
if __name__ == "__main__":
    app.run()    