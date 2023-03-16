from navak import app
from flask import render_template
import datetime
from flask import request

@app.route("/")
def index_view():
    return render_template("index.html")




@app.errorhandler(401)
def error_401(e):
    content = {
        "ip" : request.remote_addr,
        "time": datetime.datetime.now(),
    }
    return render_template("errors/401.html", content=content)

@app.errorhandler(404)
def error_404(e):
    content = {
        "ip" : request.remote_addr,
        "time": datetime.datetime.now(),
    }
    return render_template("errors/404.html", content=content)