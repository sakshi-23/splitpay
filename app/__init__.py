import os
import sys

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')


@app.route("/")
def index():
    return render_template('login.html')


@app.route("/profile")
def profile():
    return render_template('profile.html')


@app.route("/transactions")
def transactions():
    return render_template('transactions.html')



   
@app.errorhandler(404)
def not_found(error):
    return "TODO: 404 page", error


from app.data.models import mod_data as dataModule
app.register_blueprint(dataModule)