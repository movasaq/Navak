from navak import app



@app.route("/")
def index_view():
    return "Hello world"