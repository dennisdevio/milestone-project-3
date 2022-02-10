import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# GET REVIEWS FROM DATABASE
@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)

# SIGNUP FUNCTION
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if user exists in database
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            flash('Username not available')
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash('Sign up complete!')
        return redirect(url_for("profile"))

    return render_template("signup.html")

# LOGIN FUNCTION
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if user exists in database
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            # make sure hashed password matches users input
            if check_password_hash(
                user_exists["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}!".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))

            else:
                # invalid password match
                flash("Username and/or Password is incorrect")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Username and/or Password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")

# SESSION FUNCTION FOR USER ACCOUNTS
@app.route("/profile", methods=["GET", "POST"])
def profile():
    # retreive the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))

# LOGOUT FUNCTION
@app.route("/logout")
def logout():
    # remove user's session cookies
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))

# ADD REVIEW FUNCTION
@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "book_name": request.form.get("book_name"),
            "review_name": request.form.get("review_name"),
            "review_description": request.form.get("review_description"),
            "added_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_reviews"))

    books = mongo.db.books.find().sort("title", 1)
    return render_template("add_review.html", books=books)

# EDIT REVIEW FUNCTION
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "book_name": request.form.get("book_name"),
            "review_name": request.form.get("review_name"),
            "review_description": request.form.get("review_description"),
            "added_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    books = mongo.db.books.find().sort("title", 1)
    return render_template("edit_review.html", review=review, books=books)

# DELETE REVIEW FUNCTION
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Task deleted")
    return redirect(url_for("get_reviews"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)