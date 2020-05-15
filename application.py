from flask.app import Flask

APP=Flask(__name__)

@app.rout("/")
def index():return "hello world!"
