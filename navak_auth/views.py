from navak_auth import auth
from navak_auth.utils import employee_login_required
from flask import (session, abort, render_template)
from navak_auth.forms import EmployeeLoginForm

@auth.route("/employee/login/")
def employee_login_view():
    """
        This view return login form for employees
    :return: Html
    """
    form=EmployeeLoginForm()
    return render_template("auth/login.html", form=form)


@auth.route("/login/")
def login_view():
    return "other users login index"