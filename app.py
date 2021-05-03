import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
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
        #check if user is already being added to employees in db by admin user
        existing_employee = mongo.db.employees.find_one({"email": request.form.get(
            "email").lower()})
        existing_user = mongo.db.users.find_one({"email": request.form.get(
            "email").lower()})
 
        if existing_user:
            flash("This employee already registered, please login or try again")
            return redirect(url_for("register"))
 
        register = {
            "full_name": request.form.get("full_name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                 request.form.get("password")),
            "confirm_password": generate_password_hash(
                 request.form.get("confirm_password"))
            }
        mongo.db.users.insert_one(register)
 
        #Put the new user into session cookie
        session["user"] = request.form.get("email").lower()
        flash("You have registered successfully")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
