from Flask import Flask

APP=Flask(_name_)

@app.rout("/")
def index():return "hello world"
