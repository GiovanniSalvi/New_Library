import os
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def home():

    register = mongo.db.BooksData.find()
    return render_template("home.html", register=register)


@app.route("/user_list", methods=["GET", "POST"])
def user_list():

    users = mongo.db.UsersData.find()
    return render_template("user_list.html", users=users)


@app.route("/edit_task/<archive>", methods=["GET", "POST"])
def edit_task(archive):
    if request.method == "POST":
        book = mongo.db.BooksData.find_one({"_id": ObjectId(archive)})
        update = {
            "Title": request.form.get("Title").title(),
            "Author": request.form.get("Author").title(),
            "Genre": request.form.get("Genre").title(),
            "Year": request.form.get("Year"),
            "Country": request.form.get("Country").title(),
            "Location": request.form.get("Location"),
            "Status": book.get("Status"),
            "Price": request.form.get("Price"),
        }

        mongo.db.BooksData.update({"_id": ObjectId(archive)}, update)
        flash("Book updated")
        return redirect(url_for("home"))

    archive = mongo.db.BooksData.find_one({"_id": ObjectId(archive)})
    return render_template("edit_task.html", archive=archive)


@app.route("/book_add/<new_book>", methods=["GET"])
def book_add(new_book):

    new_book = mongo.db.BooksData.find_one({"_id": ObjectId(new_book)})
    return render_template("book_add.html", new_book=new_book)


@app.route("/home", methods=["GET", "POST"])
def search_book():
    if request.method == "POST":
        query = request.form.get("query")
        print('query:' + query)
        existing_book = list(mongo.db.BooksData.find(
            {"$text": {"$search": query}}
            ))
        if existing_book:
            return render_template("task.html", books=existing_book)

        else:
            flash("Book does not exist in the archive")
            return redirect(url_for("home"))

    return render_template("home.html")


@app.route("/user_list/user_details", methods=["GET", "POST"])
def search_user():
    if request.method == "POST":
        query = request.form.get("query")
        existing_user = list(mongo.db.UsersData.find(
            {"$text": {"$search": query}}
            ))
        if existing_user:
            return render_template(
                "user_details.html", existing_user=existing_user)
        else:
            flash("User does not exist in the database")
            return redirect(url_for("user_list"))

    return render_template("user_list.html")


@app.route("/task/<books>", methods=["GET"])
def task(books):
    return render_template("task.html", books=books)


@app.route("/user_details/<existing_user>", methods=["GET", "POST"])
def user_details(existing_user):
    if request.method == "POST":
        print(existing_user)
        try:
            mongo.db.UsersData.remove({"_id": ObjectId(existing_user)})
            print(existing_user)
            flash("User successful removed")
            return redirect(url_for("user_list"))
        except ValueError:
            flash("Removing user failed, try again")
            return redirect(url_for("user_list"))

    return render_template("user_details.html", existing_user=existing_user)


@app.route("/sell_book/<archive>", methods=["GET", "POST"])
def sell_book(archive):
    if request.method == "POST":
        existing_email = mongo.db.UsersData.find_one(
            {"Email": request.form.get("Email")}
        )
        book = mongo.db.BooksData.find_one({"_id": ObjectId(archive)})
        status = book.get("Status")
        if status == "Available":
            if existing_email:

                new_status = "Sold"
                submit = {
                    "Title": book.get("Title"),
                    "Author": book.get("Author"),
                    "Genre": book.get("Genre"),
                    "Year": book.get("Year"),
                    "Country": book.get("Country"),
                    "Location": book.get("Location"),
                    "Status": new_status,
                    "Price": book.get("Price"),
                }

                mongo.db.BooksData.update({"_id": ObjectId(archive)}, submit)
                return redirect(
                    url_for(
                        "book_selling", existing_email=existing_email.get(
                            "_id"))
                )
            else:
                flash("User not registered")
                return redirect(url_for("sell_book", archive=archive))
        else:
            flash(
                "Book is temporary ran out"
                )
            return redirect(url_for("sell_book", archive=archive))

    archive = mongo.db.BooksData.find_one({"_id": ObjectId(archive)})
    return render_template("sell_book.html", archive=archive)


@app.route("/book_selling/<existing_email>", methods=["GET"])
def book_selling(existing_email):
    existing_email = mongo.db.UsersData.find_one(
        {"_id": ObjectId(
            existing_email)})
    flash("Book bought by:")
    return render_template("book_selling.html", existing_email=existing_email)


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        existing_location = mongo.db.BooksData.find_one(
            {"Location": request.form.get("Location")}
        )
        existing_title = mongo.db.BooksData.find_one(
            {"Title": request.form.get("Title")}
        )
        if existing_title:
            flash("Book already exists")
            return redirect(url_for("add_task"))
        if existing_location:
            flash("Location already taken")
            return redirect(url_for("add_task"))
        else:

            add = {
                "Title": request.form.get("Title").title(),
                "Author": request.form.get("Author").title(),
                "Genre": request.form.get("Genre").title(),
                "Year": request.form.get("Year"),
                "Country": request.form.get("Country").title(),
                "Location": request.form.get("Location").title(),
                "Status": "Available",
                "Price": request.form.get("Price"),
            }
            new_book = mongo.db.BooksData.insert_one(add)

            flash("Book Successfully Added")
            return redirect(url_for("book_add", new_book=new_book.inserted_id))

    return render_template("add_task.html")


@app.route("/remove", methods=["GET", "POST"])
def remove():
    if request.method == "POST":
        query = request.form.get("query")
        existing_book = list(
            mongo.db.BooksData.find(
                {"$text": {"$search": query}}
                ))

        if existing_book:
            return render_template("remove_book.html", archive=existing_book)
        else:
            flash("Book not in stock")
            return redirect(url_for("remove"))
    return render_template("remove.html")


@app.route("/remove_book/<archive>", methods=["GET", "POST"])
def remove_book(archive):
    if request.method == "POST":
        try:
            mongo.db.BooksData.remove({"_id": ObjectId(archive)})
            flash("Book successful removed")
            return redirect(url_for("home"))
        except ValueError:
            flash("Removing book failed, try again")
            return redirect(url_for("remove"))

    return render_template("remove_book.html", archive=archive)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.UsersData.find_one(
            {"Email": request.form.get("Email").lower()}
        )

        if existing_user:
            flash("User already exists")
            return redirect(url_for("register"))

        register = {
            "First": request.form.get("First"),
            "Last": request.form.get("Last"),
            "dob": request.form.get("dob").lower(),
            "Tel": request.form.get("Tel").lower(),
            "Postcode": request.form.get("Postcode").lower(),
            "Email": request.form.get("Email").lower(),
        }
        mongo.db.UsersData.insert_one(register)

        flash("Registration Successful!")
        return redirect(url_for("home", register=register))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get(
            "IP"), port=int(
                os.environ.get(
                    "PORT")), debug=False)
