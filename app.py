import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html", register=register)

@app.route("/search_task", methods=["GET", "POST"])
def search_task():
    return render_template("search_task.html")

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    return render_template("add_task.html")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    return render_template("remove.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.UsersData.find_one(
            {"Email": request.form.get("Email").lower()})
        
        if existing_user:
            flash("Email already exists")
            return redirect(url_for("register"))

        register = {
            "First": request.form.get("First").lower(),
            "Last": request.form.get("Last").lower(),
            "dob": request.form.get("dob").lower(),
            "Tel": request.form.get("Tel").lower(),
            "Postcode": request.form.get("Postcode").lower(),
            "Email": request.form.get("Email").lower()
            
        }
        mongo.db.UsersData.insert_one(register)
        
        flash("Registration Successful!")
        return redirect(url_for("home", register=register))
            
      

    return render_template("register.html")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORTA")),
            debug=True)





