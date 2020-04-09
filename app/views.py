##
## EPITECH PROJECT, 2019
## epytodo_bootstrap_2019
## File description:
## views.py
##

from app import app
from flask import render_template
from flask import jsonify
import pymysql as sql

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def route_home():
    return render_template("index.html", title = "TITOUAN", myContent = " My SUPER content !! ")

@app.route ('/signint', methods=['POST'])
def sign_in_user():
    return render_template("index.html")

@app.route ('/signout', methods=['POST'])
def sign_out_user():
    return render_template("index.html")

@app.route ('/user', methods=['GET'])
def user():
    return render_template("index.html")

@app.route ('/user/task', methods=['GET'])
def task_board():
    return render_template("index.html")

@app.route ('/user/task/id', methods=['GET'])
def task_board_view():
    return render_template("index.html")

@app.route ('/user/task/id', methods=['POST'])
def task_board_update():
    return render_template("index.html")

@app.route ('/user/task/add', methods=['POST'])
def task_board_add():
    return render_template("index.html")

@app.route ('/user/task/del/id', methods=['POST'])
def task_board_del():
    return render_template("index.html")
