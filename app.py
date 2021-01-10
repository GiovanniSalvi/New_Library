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


@app.route("/book_add/<new_book>", methods=["GET"])
def book_add(new_book):
    new_book = mongo.db.BooksData.find_one({"_id": ObjectId(new_book)})
    return render_template("book_add.html", new_book=new_book)


@app.route("/search_task", methods=["GET", "POST"])
def search_task():
    if request.method == "POST":
        existing_book = mongo.db.BooksData.find_one(
            {"Title": request.form.get("search_title")})
        if existing_book:
            flash("book found")
            return redirect(url_for("search_task"))
        
        else:
            flash("Book does not exist in the database")
            return redirect(url_for("search_task"))
        archive = mongo.db.BooksData.insert_one()

    return render_template("rent_book.html", archive=archive.inserted_Id)


@app.route("/rent_book/<archive>", methods=["GET"])
def rent_book(archive):
    archive = mongo.db.BooksData.find_one({"_id": ObjectId(archive)})
    return render_template("rent_book.html", archive=archive)


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        existing_title = mongo.db.BooksData.find_one(
            {"Title": request.form.get("search_title")})
        
        if existing_title:
            flash("Book already exists in the database")
            return redirect(url_for("add_task"))
       
        add = {
            "Title": request.form.get("Title"),
            "Author": request.form.get("Author"),
            "Genre": request.form.get("Genre"),
            "Year": request.form.get("Year"),
            "Country": request.form.get("Country"),
            "Location": request.form.get("Location"),
            "Status": "Available"
        }
        new_book = mongo.db.BooksData.insert_one(add)

        flash("Book Successfully Added")
        return redirect(url_for("book_add", new_book=new_book.inserted_id))

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
            flash("User already exists")
            return redirect(url_for("register"))

        register = {
            "First": request.form.get("First"),
            "Last": request.form.get("Last"),
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





