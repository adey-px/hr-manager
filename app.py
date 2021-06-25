import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Home page route
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# About HRP page route
@app.route("/about_hrp")
def about_hrp():
    return render_template("about_hrp.html")


# Careers page route
@app.route("/careers")
def careers():
    return render_template("careers.html")


# Adverts page route
@app.route("/adverts")
def adverts():
    return render_template("adverts.html")


# Job Application page route
@app.route("/jobs_apply")
def jobs_apply():
    return render_template("jobs_apply.html")

# Application Status page route
@app.route("/apply_status")
def apply_status():
    return render_template("apply_status.html")


# Help Desk page route
@app.route("/help_desk")
def help_desk():
    return render_template("help_desk.html")


# Corporate page route
@app.route("/corporate")
def corporate():
    return render_template("corporate.html")


# Messaging page route
@app.route("/message")
def message():
    dbmessage = list(mongo.db.messages.find().sort("date"))
    return render_template("message.html", messages=dbmessage)


# Delete message route
@app.route("/delete_message/<message_id>")
def delete_message(message_id):
    # Use .remove on message by their id
    mongo.db.messages.remove({"_id": ObjectId(message_id)})
    return redirect(url_for("message"))


# Notification page route
@app.route("/notification", methods=["GET", "POST"])
def notification():
    if request.method == "POST":
        today = date.today()

        sender = mongo.db.users.find_one(
            {"email": session["user"]})["email"]

        notice = {
            "date": today.strftime("%B %d, %Y"),
            "sender": sender,
            "subject": request.form.get("subject"),
            "message": request.form.get("message")
        }
        mongo.db.notifications.insert_one(notice)
        flash("Your message has been sent to all employees")
        return redirect(url_for('notification'))
    return render_template("notification.html")


# Register page route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user has been added to employees in db by admin
        existing_employee = mongo.db.employees.find_one(
                {"email": request.form.get("email").lower()})

        # check if user has already registered as an eligible employee
        existing_user = mongo.db.users.find_one({"email": request.form.get(
            "email").lower()})

        if existing_user:
            flash("This employee has registered. Go login or try again!")
            return redirect(url_for("register"))

        else:
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")

            # Use comparison to generate a variable named password
            # store it in another variable named valid_password
            # NB: If a string is passed into (), it bcomes default password
            if password == confirm_password:
                valid_password = generate_password_hash(password)

            else:
                # If both password inputs from Register form do not match
                flash("Passwords do not match. Please try again.")
                return redirect(url_for("register"))

        # Create a variable register to insert an Array of the Register form inputs
        # Pass in the variable named password generated above
        # NB: the variable password stands for both password inputs from the form
        if existing_employee:
            register = {
                "full_name": request.form.get("full_name").lower(),
                "email": request.form.get("email").lower(),
                "password": valid_password
                }
            mongo.db.users.insert_one(register)

        else:
            # If user is not an existing employee
            flash("Caution! You are not eligible to register.")
            return redirect(url_for("register"))

        # If all conditions are satisfied, put the new user into session cookie
        session["user"] = request.form.get("email").lower()
        flash("Hey! Congratulations. You have registered successfully")
        return redirect(url_for("register", email=session["user"]))
    return render_template("register.html")


# Login page route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if user is still existing in employees' coll in db
        existing_employee = mongo.db.employees.find_one(
                {"email": request.form.get("email").lower()})

        # Check if user's email input exists in registered users in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_employee:

            if existing_user:
                # Check user input password if it matches hashed password in db
                correct_password = check_password_hash(
                    existing_user["password"], request.form.get("password"))

                # If both conditions are satisfied, put the user in a session
                if correct_password:
                    session["user"] = request.form.get("email").lower()
                    return redirect(url_for("dashboard", email=session["user"]))

                else:
                    # If incorrect or invalid password, redirect user back
                    flash("Incorrect username and/or password, try again!")
                    return redirect(url_for("login"))

            else:
                # If user input email does not exist in the db, redirect back
                flash("Incorrect username and/or password, try again!")
                return redirect(url_for("login"))

        else:
            # If user is not a recognized employee
            flash("Incorrect or unathourized username and/or password.")
            return redirect(url_for("login"))
    return render_template("login.html")


# Change Password page route
@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    if request.method == "POST":
        # Get logged in user from db thru their active session
        # Note that user is identified by their email in the db
        user = mongo.db.users.find_one({"email": session["user"]})

        # Also get logged in user password from db thru their active session
        user_password = mongo.db.users.find_one(
            {"email": session["user"]})["password"]

        # Compare user password in db with value in form input as old password
        match_password = check_password_hash(
            user_password, request.form.get("oldpass"))

        if match_password:
            # Create a variable to get new password from form input
            new_password = request.form.get("newpass")

            # Update the old password with the new_password thru user id in db
            mongo.db.users.update_one({"_id": ObjectId(user["_id"])
            }, {"$set": {"password": generate_password_hash(new_password)}})
            flash("Your password has been updated successfully")
            return redirect(url_for("change_password"))
        else:
            flash("Whoops! Your password did not match existing record")
            return redirect(url_for("change_password"))

    return render_template("password.html")


# Logout page route
@app.route("/logout")
def logout():
    # To log out user, remove or clear active session cookies
    session.clear()
    flash("You have logged out of your current sesion")
    return redirect(url_for("login"))


# New employee page route
@app.route("/new_employee", methods=["GET", "POST"])
def new_employee():
    if request.method == "POST":
        # Check if employee already exists in db by their form input email
        employee = mongo.db.employees.find_one(
            {"email": request.form.get("email").lower()})

        if employee:
            flash("This employee already exists, access denied!")

        else:
            # Create a dictionary to get form inputs to insert in db
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
            flash("New employee record added successfully")
            return redirect(url_for('new_employee'))

    # Variable to get list of departments into form select options
    depa = list(mongo.db.departments.find().sort("department", 1))
    return render_template("new_employee.html", dpt=depa)


# Dashboard page route
@app.route("/dashboard/<email>", methods=["GET", "POST"])
def dashboard(email):
    # Firstly get each employee from db by their email identifier
    dash = mongo.db.employees.find_one({"email": email})

    # Get all notices from HR inside notifications collection in db
    notice = mongo.db.notifications.find()

    # Get user/employee individual detail into their active session
    # Variable employ is applied in dashboard.html to get individual info
    if "user" in session:
        return render_template("dashboard.html", employ=dash, notices=notice)


# Employee message route in dashboard page
@app.route("/emp_message/<email>", methods=["GET", "POST"])
def emp_message(email):
    # Get user/employee email & full name from db thru their session
    # This is bcos email & name of sender should show in message sent
    user_email = mongo.db.users.find_one(
            {"email": session["user"]})["email"]
    
    user_name = mongo.db.users.find_one(
            {"email": session["user"]})["full_name"]
    
    today = date.today()

    # Get form input message along with date & email of sender
    if request.method == "POST":
        messa = {
            "date": today.strftime("%B %d, %Y"),
            "email": user_email,
            "name": user_name,
            "message": request.form.get("mess")
        }
        mongo.db.messages.insert_one(messa)
        flash("Your message has been sent successfully")
        # Pass route thr email since dashboard temp is rendered thr it
        return redirect(url_for("dashboard", email=user_email))
    return render_template("dashboard.html", email=user_email)


# Get employee page route
@app.route("/get_employee", methods=["GET", "POST"])
def get_employee():
    # Ge each user/employee from db & sort by their first name
    emplo = list(mongo.db.employees.find().sort("first_name", 1))
    # Variable staff is exported to get_employee.html
    return render_template("get_employee.html", staff=emplo)


# Manage employee page route
@app.route("/manage_employee")
def manage_employee():
    # Get list of all departments from db and also list of all employees
    # To display employees by their departments wc are both db collections
    employk = list(mongo.db.departments.find())
    alice = list(mongo.db.employees.find())
    # Variables depo & staff are exported to manage_employee.html
    return render_template(
        "manage_employee.html", depo=employk, staff=alice)


# Employee search route
@app.route("/search", methods=["GET", "POST"])
def search():
    # Create variable to get input from search form
    query = request.form.get("query")
    # Pass thru variables employk & alice for manage_employee temp
    # Perform text search of employee within list of departments
    employk = list(mongo.db.departments.find({"$text": {"$search": query}}))
    alice = list(mongo.db.employees.find())
    return render_template("manage_employee.html", depo=employk, staff=alice)


# Edit employee page route
@app.route("/edit_employee/<employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):
    if request.method == "POST":
        # Dictionary from new employment template form
        edit = {
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
        # Use .update on employee id and pass in the dictionary
        mongo.db.employees.update({"_id": ObjectId(employee_id)}, edit)
        flash("Employee Record Updated Successfully")
        return redirect(url_for('manage_employee'))

    # Get employee thru their id from db & get list of departments
    edica = mongo.db.employees.find_one({"_id": ObjectId(employee_id)})
    depa = list(mongo.db.departments.find().sort("department", 1))
    return render_template("edit_employee.html", edico=edica, dpt=depa)


# Delete employee route
@app.route("/delete_employee/<employee_id>")
def delete_employee(employee_id):
    # Use .remove on employee by their id
    mongo.db.employees.remove({"_id": ObjectId(employee_id)})
    flash("Employee Deleted Successfully")
    return redirect(url_for("manage_employee"))


# All departments page route
@app.route("/all_departments")
def all_departments():
    # Get all departments from db and sort alphabetically
    dpt = mongo.db.departments.find().sort("department", 1)
    return render_template("all_departments.html", ment=dpt)


# New department page route
@app.route("/new_department", methods=["GET", "POST"])
def new_department():
    if request.method == "POST":
        # Check if department already exists in db
        existing_department = mongo.db.departments.find_one(
            {"department": request.form.get("department_name").capitalize()})

        if existing_department:
            flash("Whoops! This department already exists.")
            return redirect(url_for("new_department"))

        else:
            # Create new department thru a dictionary and insert into db
            department = {
                "department": request.form.get("department_name").capitalize()
            }
            mongo.db.departments.insert_one(department)
            flash("Bravo! You have just created a new Department")
            return redirect(url_for("new_department"))
    return render_template("new_department.html")


# Edit department page route
@app.route("/edit_department/<item_id>", methods=["GET", "POST"])
def edit_department(item_id):
    if request.method == "POST":
        # Create a dictionary to get department name from form input
        edit = {
            "department": request.form.get("department_name")
        }
        # Use .update method on department id and pass in dictionary variable
        mongo.db.departments.update({"_id": ObjectId(item_id)}, edit)
        flash("Department Updated Successfully")
        return redirect(url_for("all_departments"))

    # Get department by their id from db and route thru the variable
    edica = mongo.db.departments.find_one({"_id": ObjectId(item_id)})
    return render_template("edit_department.html", edico=edica)


# Delete department route
@app.route("/delete_department/<item_id>")
def delete_department(item_id):
    # Use .remove method to delete department
    mongo.db.departments.remove({"_id": ObjectId(item_id)})
    flash("Department Deleted Successfully")
    return redirect(url_for("all_departments"))


# Game page route
@app.route("/game")
def game():
    return render_template("game.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
