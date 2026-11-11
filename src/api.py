from flask import Flask 
import sqlite3

app = Flask(__name__)
db = "profiles.db"
conn = sqlite3.connect(db)
cur = conn.cursor()

# giving the index of the profile, the max range and min range 
@app.route("/add_profile")
def add_profile:


# giving the index of the profile remove the profile
@app.route("/remove_profile")
def remove_profile:


# giving the index of the profile, the max range and min range
@app.route("/update_profile")
def update_profile:


# return number of profile and corresponding max range and min range
@app.route("")