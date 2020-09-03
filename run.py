#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## epytodo_bootstrap_2019
## File description:
## run.py
##

from app import app

if __name__ == '__main__':
    app.secret_key = 'bonjour'
    app.run()