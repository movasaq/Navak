from navak_auth import auth
from navak_auth.utils import employee_login_required
from flask import (session, abort, render_template)

@auth.route("/employee/login/")
def employee_login_view():
    return render_template("")


@auth.route("/login/")
def login_view():
    return "other users login index"