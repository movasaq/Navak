import datetime

from flask import render_template
from flask import request

from navak import app
from navak.extensions import db


@app.route("/")
def index_view():
    return render_template("index.html")


@app.errorhandler(401)
def error_401(e):
    content = {
        "ip": request.remote_addr,
        "time": datetime.datetime.now(),
    }
    return render_template("errors/401.html", content=content)


@app.errorhandler(404)
def error_404(e):
    content = {
        "ip": request.remote_addr,
        "time": datetime.datetime.now(),
    }
    return render_template("errors/404.html", content=content)


@app.route("/setup")
def setup():
    # load all roles to db
    from navak_config.utils import load_roles as load_roles
    roles = load_roles()

    import navak_auth.models as models
    for each in roles:
        print(each)

        role = models.Role()
        role.RoleName = each["role-en"]
        role.RoleDescription = each["role-fa"]
        role.id = each["role-id"]

        db.session.add(role)
        db.session.commit()
    return "OK"
