##
## EPITECH PROJECT, 2019
## WEB_epytodo_2019
## File description:
## controller.py
##

from app import app, models
from flask import render_template, jsonify, request, g, session, Blueprint, redirect, url_for, flash, json
import pymysql as sql

def check_login():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = session.get('username')

def need_login(title_u):
    user_id = session.get('user_id')
    msg = {}

    if user_id is None:
        g.user = None
        msg['error'] = "you must be logged in"
        flash(json.loads(json.dumps(msg)))
        return redirect(url_for('route_home'))
    else:
        g.user = session.get('username')
        return render_template("index.html", title = title_u)

def register_user():
    command_register =  "INSERT INTO `user` (`username`, `password`) VALUES (%s, %s)"
    msg = {}
    try:
        username = str(request.form["key1"])
        password = str(request.form["key2"])
        db_tools = models.connect_to_db()
        command_check = "SELECT * FROM `user` WHERE `username` = %s"
        user = models.get_data(db_tools, command_check, username)
        if user is None:
            models.register(db_tools, command_register, username, password)
            msg['result'] = "account created"
        else:
            msg['error'] = "account already exists"
    except Exception:
        msg['error'] = "internal error"
    flash(json.loads(json.dumps(msg)))

def sign_in_user():
    msg = {}
    username = str(request.form["username"])
    password = str(request.form["password"])
    db_tools = models.connect_to_db()
    command = "SELECT * FROM `user` WHERE `username` = %s"
    user = models.get_data(db_tools, command, username)
    if user is None or user[2] != password:
        msg['error'] = "login or password does not match"
    else:
        session.clear()
        session['user_id'] = user[0]
        session['username'] = user[1]
        msg['result'] = "signin successful"
    flash(json.loads(json.dumps(msg)))

def sign_out():
    user_id = session.get('user_id')
    msg = {}

    if user_id is None:
        g.user = None
        msg['error'] = "you must be logged in"
    else:
        session.clear()
        g.user = None
        msg['result'] = "signout successful"
    flash(json.loads(json.dumps(msg)))

def user_profile(username):
    result = ""

    try :
        db_tools = models.connect_to_db()
        db_tools.cursor.execute(username)
        result = db_tools.cursor.fetchall()
        models.close_connect(db_tools.connect, db_tools.cursor)
    except Exception :
        print ("internal error")
    return jsonify(result)

def delete_task_user(name_of_the_task) :
    command =  "DELETE INTO `task` WHERE `task_id` = %s"
    try:
        db_tools = models.connect_to_db()
        models.del_task_in_db(db_tools, command, name_of_the_task)
    except Exception :
        print ("internal error")
        return ("error")
    print ("task deleted")
    return ("success")

def route_add_task(nameof_task, begin, end, status):
    command =  "INSERT INTO `task` (`nameof_task`, `begin`, `end`, `status`) " + " VALUES (%s, %s, %s, %s) "

    try:
        db_tools = models.connect_to_db()
        models.add_task(db_tools, command, nameof_task, begin, end ,status)
    except Exception :
        print ("internal error")
        return ("error")
    print ("new task added")
    return ("success")

def list_user_tasks() :
    result = ""

    try :
        db_tools = models.connect_to_db()
        result = models.list_tasks(db_tools, result)
    except Exception :
        print ("internal error")
        return ("error")
    return jsonify(result)

def show_task(name_of_the_task) :
    result = ""
    command = "SELECT * FROM `task` where `nameof_task` = %s"

    try:
        db_tools = models.connect_to_db()
        result = models.task_in_db(db_tools, command, name_of_the_task)
    except Exception:
        print ("internal error")
        return ("error")
    return jsonify(result)