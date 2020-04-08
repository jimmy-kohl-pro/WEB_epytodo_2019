##
## EPITECH PROJECT, 2019
## WEB_epytodo_2019
## File description:
## controller.py
##

from app import app
from flask import render_template
from flask import jsonify
import pymysql as sql

@app.route('/register', methods=['POST'])
def route_add_user(username, passwd, email):
    sql =  "Insert into Logins (user_id, username, password) " + " values (%s, %s, %s) "

    try:
        connect = sql.connect(host ="127.0.0.1", unix_socket = None, user = "root", passwd = "", db = "epytodo")
        cursor = connect.cursor()
        cursor.execute(sql, (username, passwd, email))
        connection.close(connect)
    except Exception :
        print ("error : internal error")
        return ("error")
    print ("account created")
    return ("success")

@app.route ('/user')
def route_all_users (username):
    result = ""
    try :
        connect = sql.connect(host ="127.0.0.1", unix_socket = None, user = "root", passwd = "", db = "epytodo")
        cursor = connect.cursor()
        cursor.execute(username)
        result = cursor.fetchall()
        cursor.close()
        connect.close()
    except Exception :
        print ("internal error")
    return jsonify(result)

@app.route ('/signin', methods=['POST'])
def sign_in_user() :
    try:
        connect = sql.connect(host ="127.0.0.1", unix_socket = None, user = "root", passwd = "", db = "epytodo")
        cursor = connect.cursor()
        cursor.execute(request.form['user'])
        result = cursor.fetchall()
    except Exception :
        print ("internal error")
    return jsonify(result)

@app.route ('/user/task/del/id', methods=['POST'])
def sign_in_user(name_of_the_task) :
    sql =  "DELETE INTO Tasks WHERE (task) " + " values (%s) "

    try:
        connect = sql.connect(host ="127.0.0.1", unix_socket = None, user = "root", passwd = "", db = "epytodo")
        cursor.execute(sql, (task))
        connection.close(connect)
    except Exception :
        print ("error : internal error")
        return ("error")
    print ("task deleted")
    return ("success")

@app.route('/task/add', methods=['POST'])
def route_add_task(task, begin, end, status):
    sql =  "INSERT INTO Tasks (task, begin, end, status) " + " values (%s, %s, %s, %s) "

    try:
        connect = sql.connect(host ="127.0.0.1", unix_socket = None, user = "root", passwd = "", db = "epytodo")
        cursor.execute(sql, (task, begin, end, status))
        connection.close(connect)
    except Exception :
        print ("error : internal error")
        return ("error")
    print ("new task added")
    return ("success")

@app.route ('/user/task', methods=['GET'])
def list_user_tasks() :
    result = ""
    try :
        connect = sql.connect(host ="127.0.0.1", unix_socket = None, user = "root", passwd = "", db = "epytodo")
        cursor = connect.cursor()
        cursor.execute()
        result = cursor.fetchall()
    except Exception :
        print ("error : internal error")
        return ("error")
    return jsonify(result)
@app.route ('/user/task/id', methods=['GET'])
def show_task(name_of_the_task) :
    result = ""
    sql = "SELECT (task) FROM TASKS" + "values %s"

    try:
        connect = sql.connect(host ="127.0.0.1", unix_socket = None, user = "root", passwd = "", db = "epytodo")
        cursor = connect.cursor(connect)
        cursor.execute(sql, (name_of_the_task))
        result = cursor.fetchall()
    except Exception:
        print ("error : internal error")
        return ("error")
    return jsonify(result)