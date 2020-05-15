from flask import flask

APP=flask(_name_)

@app.rout("/")
def index():return "hello world"