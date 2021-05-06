import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
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

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user has been added to employees by admin user
        existing_employee = mongo.db.employees.find_one(
                {"email": request.form.get("email").lower()})
        # check if user has already registered as an employee
        existing_user = mongo.db.users.find_one({"email": request.form.get(
            "email").lower()})
        
        if existing_employee:
            register = {
                "full_name": request.form.get("full_name").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
                "confirm_password": generate_password_hash(
                    request.form.get("confirm_password"))
                }

        else:
            flash("You are not eligible to register. Please contact Admin.")

        if existing_user:
            flash("This employee has already registered. Login or Try again")
            return redirect(url_for("register"))

        password = generate_password_hash(
                 request.form.get("password"))
        confirm_password = generate_password_hash(
                 request.form.get("confirm_password"))
                                
        if password == confirm_password:
            mongo.db.users.insert_one(register)

        else:
            flash("Passwords do not match. Please try again.")
            return redirect(url_for("register"))
 
        # Put the new user into session cookie
        session["user"] = request.form.get("email").lower()
        flash("You have registered successfully")
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html",)


@app.route("/get_employee")
def get_employee():
    item = mongo.db.employees.find()
    return render_template("dashboard.html", employees=item)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")), debug=True)
