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
        role = models.Role()
        role.RoleName = each["role-en"]
        role.RoleDescription = each["role-fa"]
        role.id = each["role-id"]
        try:
            db.session.add(role)
            db.session.commit()
        except:
            db.session.rollback()

    UsrRole = models.Role.query.filter(models.Role.RoleName == "admin").first()

    usr = models.User()
    usr.username = "alisahrify"
    usr.set_password("123654")
    usr.FullName = "علی شریفی"
    usr.set_public_key()
    usr.UserRole = UsrRole.id
    usr.Active = True

    try:
        db.session.add(usr)
        db.session.commit()
    except:
        db.session.rollback()

    return "OK"
