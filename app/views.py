##
## EPITECH PROJECT, 2019
## epytodo_bootstrap_2019
## File description:
## views.py
##

from app import app, controller
from flask import render_template,request,redirect,url_for
from flask import jsonify
import pymysql as sql

@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def route_home():
    controller.check_login()
    return render_template("index.html", title = "BebouDoList")

@app.route('/register', methods=['POST'])
def view_register():
    controller.register_user()
    return redirect(url_for('route_home'))

@app.route ('/signin', methods=['POST'])
def view_sign_in():
    controller.sign_in_user()
    return redirect(url_for('route_home'))

@app.route ('/signout', methods=['POST'])
def view_sign_out_user():
    controller.sign_out()
    return redirect(url_for('route_home'))

@app.route ('/user', methods=['GET'])
def view_user():
    # controller.user_profile
    return controller.need_login("User Profile")

@app.route ('/user/task', methods=['GET'])
def list_tasks_route():
    # controller.list_user_tasks()
    return controller.need_login("Task list")

@app.route ('/user/task/<int:id>', methods=['GET'])
def id_task_route(id):
    # controller.show_task(id)
    return controller.need_login("Task {}".format(id))

@app.route ('/user/task/del/<int:id>', methods=['POST'])
def view_delete_task(id):
    # controller.delete_task_user(id)
    return controller.need_login("Delete task {}".format(id))

@app.route('/user/task/add', methods=['POST'])
def task_add_route():
    # controller.route_add_task()
    return controller.need_login("Add Task")