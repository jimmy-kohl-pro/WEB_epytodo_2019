##
## EPITECH PROJECT, 2019
## epytodo_bootstrap_2019
## File description:
## __init__.py
##

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views