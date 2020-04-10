##
## EPITECH PROJECT, 2019
## epytodo_bootstrap_2019
## File description:
## views.py
##

from app import app
from flask import render_template
from flask import jsonify
import controller
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home():
    return render_template("index.html", title = "TITOUAN", myContent = " My SUPER content !! ")

@app.route ('/signout', methods=['POST'])
def sign_out_user():
    return render_template("index.html")

@app.route ('/user', methods=['GET'])
def user():
    return render_template("index.html")
@app.route('/register', methods=['POST'])
def Register_user():
    username =""
    passwd = ""
    email = ""

    route_add_user(username, passwd, email)
