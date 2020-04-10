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
import models

def route_add_user(username, passwd, email):
    command =  "Insert into Logins (user_id, username, password) " + " values (%s, %s, %s) "
    db_tools =  {'connect': None, 'cursor': None}
    try:
        db_tools = connect_to_db()
        register(db_tools.cursor, command, username, passwd, email)
        close_connect(db_tools.connect, db_tools.cursor)
    except Exception :
        print ("internal error")
        return ("error")
    print ("account created")
    return ("success")

@app.route ('/user')
def route_all_users (username):
    result = ""
    db_tools = {'connect': None, 'cursor': None}
    try :
        db_tools = connect_to_db()
        db_tools.cursor.execute(username)
        result = cursor.fetchall()
        close_connect(db_tools.connect, db_tools.cursor)
    except Exception :
        print ("internal error")
    return jsonify(result)

@app.route ('/signin', methods=['POST'])
def sign_in_user() :
    result = ""
    db_tools = {'connect': None, 'cursor': None}
    try:
        db_tools = connect_to_db()
        sign_in(cursor, command, username, passwd, email)
        result = cursor.fetchall()
        close_connect(db_tools.connect, db_tools.cursor)
    except Exception :
        print ("internal error")
    return jsonify(result)

@app.route ('/user/task/del/id', methods=['POST'])
def delete_task_user(name_of_the_task) :
    command =  "DELETE INTO Tasks WHERE (task) " + " values (%s) "
    db_tools = {'connect': None, 'cursor': None}

    try:
        db_tools = connect_to_db()
        del_task_in_db(db_tools.cursor, command, name_of_the_task)
        close_connect(db_tools.connect, db_tools.cursor)
    except Exception :
        print ("error : internal error")
        return ("error")
    print ("task deleted")
    return ("success")

@app.route('/task/add', methods=['POST'])
def route_add_task(task, begin, end, status):
    command =  "INSERT INTO Tasks (task, begin, end, status) " + " values (%s, %s, %s, %s) "
    db_tools = {'connect': None, 'cursor': None}

    try:
        db_tools = connect_to_db()
        add_task(db_tools.cursor, command, task, begin, end ,status)
        close_connect(db_tools.connect, db_tools.cursor)
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
        cursor.close()
        connect.close(connect)
    except Exception :
        print ("error : internal error")
        return ("error")
    return jsonify(result)

@app.route ('/user/task/id', methods=['GET'])
def show_task(name_of_the_task) :
    result = ""
    command = "SELECT (task) FROM TASKS" + "values %s"
    db_tools = {'connect': None, 'cursor': None}

    try:
        db_tools = connect_to_db()
        result = task_in_db(db_tools.cursor, command, name_of_the_task)
        connect_close(db_tools.connect, db_tools.cursor)
    except Exception:
        print ("error : internal error")
        return ("error")
    return jsonify(result)