##
## EPITECH PROJECT, 2019
## WEB_epytodo_2019
## File description:
## models.py
##

import pymysql as sql

def connect_to_db() :
    try:
        connect = sql.connect(host ="127.0.0.1", unix_socket = None, user = "root", passwd = "", db = "epytodo")
        cursor = connect.cursor()
    except Exception :
        print ("internal error")
        return ("error")
    return {'connect': connect, 'cursor': cursor}

def close_connect(connect, cursor):
        cursor.close()
        connect.close(connect)


def task_in_db(cursor, command, name_of_the_task):
        result = ""

        try :
            cursor.execute(command, (name_of_the_task))
            result = cursor.fetchall()
        except Exception:
            return ("error")
        return (result)


def del_task_in_db(cursor, command, name_of_the_task):
        try :
            cursor.execute(command, (name_of_the_task))
        except Exception:
            return ("error")
        return ("success")

def sign_in(cursor, command, username, passwd) :
    try:
        cursor.execute(command, username, passwd)
    except Exception:
        return("error")
    return ("success")

def register(cursor, command, username, passwd, email) :
    try:
        cursor.execute(command, (username, passwd, email))
    except Exception:
        return ("error")
    return ("success")

def add_task(cursor, command, task, begin, end ,status) :
    try:
        cursor.execute(command, (task, begin, end, status))
    except Exception:
        return ("error")
    return ("success")