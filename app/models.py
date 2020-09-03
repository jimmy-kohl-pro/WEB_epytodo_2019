##
## EPITECH PROJECT, 2019
## WEB_epytodo_2019
## File description:
## models.py
##

from app import app
import pymysql as sql

class connect_to_db() :
    def __init__(self):
        try:
            self.connect = sql.connect(host = app.config['DATABASE_HOST'], unix_socket = app.config['DATABASE_SOCK'],
                                    user = app.config['DATABASE_USER'], passwd = app.config['DATABASE_PASS'],
                                    db = app.config['DATABASE_NAME'])
            self.cursor = self.connect.cursor()
        except Exception :
            print ("internal error")

def get_data(db_tools, command, data):
    db_tools.cursor.execute(command, (data))
    result = db_tools.cursor.fetchone()
    return result

def close_connect(connect, cursor):
    cursor.close()
    connect.close(connect)

def task_in_db(db_tools, command, name_of_the_task):
    result = ""
    try :
        db_tools.cursor.execute(command, (name_of_the_task))
        result = db_tools.cursor.fetchone()
    except Exception:
        return ("error")
    return (result)


def del_task_in_db(db_tools, command, name_of_the_task):
    try :
        db_tools.cursor.execute(command, (name_of_the_task))
        db_tools.connect.commit()
    except Exception:
        return ("error")
    return ("success")

def sign_in(db_tools, command, username, passwd) :
    try:
        db_tools.cursor.execute(command, username, passwd)
        db_tools.connect.commit()
    except Exception:
        return("error")
    return ("success")

def register(db_tools, command, username, passwd) :
    try:
        db_tools.cursor.execute(command, (username, passwd))
        db_tools.connect.commit()
    except Exception:
        return ("error")
    return ("success")

def add_task(db_tools, command, task, begin, end ,status) :
    try:
        db_tools.cursor.execute(command, (task, begin, end, status))
        db_tools.connect.commit()
    except Exception:
        return ("error")
    return ("success")

def list_tasks(db_tools, result):
    try:
        db_tools.cursor.execute("SELECT * FROM `task`")
        db_tools.connect.commit()
        result = db_tools.cursor.fetchall()
    except Exception:
        return ("error")
    return (result)