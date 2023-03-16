from navak_auth import auth
from navak_auth.utils import employee_login_required
from flask import (session, abort, render_template, redirect, url_for, flash)
from navak_auth.forms import EmployeeLoginForm

@auth.route("/employee/login/")
def employee_login_view():
    """
        This view return login form for employees
    :return: Html
    """
    form=EmployeeLoginForm()
    return render_template("auth/login.html", form=form)

@auth.route("/employee/login/", methods=["POST"])
def employee_login_post():
    """
        this view take a post request for login Employees to there panel
    :return: Html
    """
    form = EmployeeLoginForm()
    if form.validate():
        pass
    else:
        flash("برخی موارد مقدار دهی نشده اند")
        return redirect(url_for("auth.employee_login_view"))

@auth.route("/login/")
def login_view():
    return "other users login index"