from flask.app import flask

APP=flask(__name__)

@app.rout("/")
def index():return "hello world!"
