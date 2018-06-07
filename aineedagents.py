import os
from flask import Flask,flash, redirect, render_template, request, session, abort
from random import randint
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
@app.route("/")
def index():
    return render_template(
    'index.html',**locals())

@app.route('/')

def root():
	return app.send_static_file('aineedagents.html')

f _name_ == "_main_":
    app.run(host='0.0.0.0')
