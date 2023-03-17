import datetime
import os

from flask import render_template, send_from_directory, request

from navak import app
from navak.extensions import db
from navak_auth.utils import basic_login_required
from navak_config import config as config


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


@app.route("/login/public/static/<path:path>")
@basic_login_required
def login_public_static(path):
    """
    this view only serve static file to users that login to there account
    :return: static file
    """
    if os.path.exists(os.path.join(config.LOGIN_PUBLIC_STATIC, path)):
        return send_from_directory(config.LOGIN_PUBLIC_STATIC, path)
    else:
        return "File Not Found", 404


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
