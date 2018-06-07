import os
from flask import Flask,flash, redirect, render_template, request, session, abort
from random import randint
	
app = Flask(_name_)
@app.route("/")
def index():
    return render_template(
    'aineedagents.html',name = name)

@app.route('/')

def root():
	return app.send_static_file('aineedagents.html')

if _name_ == "_main_":
    app.run(host='0.0.0.0')


