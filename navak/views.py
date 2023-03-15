from navak import app
from flask import render_template


@app.route("/")
def index_view():
    return render_template("index.html")
