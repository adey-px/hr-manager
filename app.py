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
        # check if user has been added to employees in db by admin user
        existing_employee = mongo.db.employees.find_one(
                {"email": request.form.get("email").lower()})
        # check if user has already registered as an eligible employee
        existing_user = mongo.db.users.find_one({"email": request.form.get(
            "email").lower()})
        
        if existing_user:
            flash("This employee has already registered. Go login or try again!")
            return redirect(url_for("register"))

        else:
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")
                                
            if password == confirm_password:
                valid_password = generate_password_hash(password)

            else:
                flash("Passwords do not match. Please try again.")
                return redirect(url_for("register"))

        if existing_employee:
            register = {
                "full_name": request.form.get("full_name").lower(),
                "email": request.form.get("email").lower(),
                "password": valid_password
                }
            mongo.db.users.insert_one(register)

        else:
            flash("Hey! What is going on? You are not eligible to register.")
            return redirect(url_for("register"))
    
        # Put the new user into session cookie
        session["user"] = request.form.get("email").lower()
        flash("Hey! Congratulations. You have registered successfully")
        return redirect(url_for("register", email=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if the user is still existing as an employee in db
        existing_employee = mongo.db.employees.find_one(
                {"email": request.form.get("email").lower()})
        # Check if user's email input exists in registered users in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_employee:

            if existing_user:
                # Check the user input password if it matches hashed password in mongo db
                # Then if both credentials are correct, put the user in a session with his email
                correct_password = check_password_hash(existing_user["password"], request.form.get("password"))
            
                if correct_password:
                    session["user"] = request.form.get("email").lower()
                    flash("Welcome, {}".format(request.form.get("email")))
                    return redirect(url_for("dashboard", email=session["user"]))

                else:
                    # If incorrect or invalid password, redirect user back login page to retry
                    flash("Incorrect username and/or password. Try again!")
                    return redirect(url_for("login"))

            else:
                # If user input email does not exist in the db, redirect back to login page to retry
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        
        else:
            flash("Hey! friend, you are not authorized to use this portal.")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    # To log out user, remove or clear active session cookies
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        employee = mongo.db.employees.find_one(
            {"email": request.form.get("email").lower()})

        if employee:
            flash("This employee already existed. Access denied!")

        else:
            new_employee = {
                "department": request.form.get("department"),
                "first_name": request.form.get("first_name"),
                "last_name": request.form.get("last_name"),
                "email": request.form.get("email").lower(),
                "mobile": request.form.get("mobile"),
                "address": request.form.get("address"),
                "gender": request.form.get("gender"),
                "employment_date": request.form.get("employment_date"),
                "duties": request.form.get("duties")
            }
            mongo.db.employees.insert_one(new_employee)
            flash("New employee added successfully")
            return redirect(url_for('add_employee'))
    return render_template("add_employee.html")


@app.route("/dashboard")
def dashboard():
    item = mongo.db.employees.find()
    return render_template("dashboard.html", employees=item)


@app.route("/get_employee")
def get_employee():
    return render_template("get_employee.html")


@app.route("/manage_employee")
def manage_employee():
    return render_template("manage_employee.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
