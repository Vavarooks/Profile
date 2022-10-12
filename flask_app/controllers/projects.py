from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from models.production import Product

from flask_app import app
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    all_projects = Product.get_all();
    return render_template("index.html", all_projects = all_projects)

@app.route("/create", methods = "POST")
def create():
    data = {
        "name" : request.form["name"],
        "name" : request.form["name"],
        "name" : request.form["name"]
    }
    Product.save(data)
    return redirect("/submit")

@app.route("/submit")
def submit():
    all_projects = Product.get_all();
    return render_template("form.html", all_projects = all_projects)