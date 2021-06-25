# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"

# From orginal server.py
# from flask import Flask, render_template,request, redirect
# from user import User
# app = Flask(__name__)