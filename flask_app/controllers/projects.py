from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
# from models.production import Product

from flask_app import app
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")