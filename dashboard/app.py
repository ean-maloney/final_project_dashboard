import os
from flask import(
    Flask, render_template, jsonify, request, redirect
)

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

## Based on https://pythonbasics.org/flask-sqlalchemy/
class schools(db.Model):
    unitid = db.Column(db.integer)
    school = db.Column(db.String(100))
    lat = db.Column(db.String(10))
    lon = db.Column(db.String(10))
    region = db.Column(db.String(3))
    nearest_mlb = db.Column(db.String(50))
    nearest_mlb_dist = db.Column(db.String(5))
    nearest_nba = db.Column(db.String(50))
    nearest_nba_dist = db.Column(db.String(50))



### Import class object?? ###

@app.route("/")
def home():
    return render_template("index.html", value = schools.query.all())

if __name__ == "__main__":
    app.run()    