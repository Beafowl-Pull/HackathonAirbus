#!/usr/bin/env python3

import json

def login(login, password):
    with open('users.json', 'r') as f:
        users = json.load(f)
    for user in users:
        if user['login'] == login and user['password'] == password:
            return True
    return False

def register(login, password):
    with open('users.json', 'r') as f:
        users = json.load(f)
    for user in users:
        if user['login'] == login:
            return False
    users.append({'login': login, 'password': password})
    with open('users.json', 'w') as f:
        json.dump(users, f)
    return True