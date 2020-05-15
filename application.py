from flask.app import Flask

@app.rout("/")
def index():return "hello world!"
