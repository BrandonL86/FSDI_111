from flask import Flask                 #from the flask module, import the Flask Class
from flask import render_template
# OOP - Object Oriented Paradigm
app = Flask(__name__)                   #Initialize the Flask class into app, now an object


@app.get("/")                           #Flask decorator that creates routes
def index():
    me = {                              #python dictionary (key and value pairs)
        "first_name": "Brandon",
        "last_name": "Lile",
        "hobbies": "Gaming",
        "is_active": True
    }
    return me                           # With Flask, returning a valid dictionary from a
                                        # view fuction will automatically convert it to JSON

@app.get("/about")
def about_me():
    return render_template("about.html")