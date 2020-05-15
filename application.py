from flask.app import flask

APP=Flask(_name_)

@app.rout("/")
def index():return "hello world!"
