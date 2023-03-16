from flask import (session, render_template, redirect, url_for, flash, request)

from navak_auth import auth
from navak_auth.forms import LoginForm
from navak_employee.models import Employee


@auth.route("/employee/login/")
def employee_login_view():
    """
        This view return login form for employees
    :return: Html
    """
    form = LoginForm()
    return render_template("auth/EmployeeLogin.html", form=form)

@auth.route("/employee/login/", methods=["POST"])
def employee_login_post():
    """
        this view take a post request for login Employees to there panel
    :return: Html
    """
    form = LoginForm()
    if form.validate():

        if not (Employee_db := Employee.query.filter(Employee.UserName == form.username.data).first()):
            flash("کاربری با نام کاربری وارد شده یافت نشد", "danger")
            return redirect(request.referrer)

        if not Employee_db.check_password(form.password.data):
            flash("اعتبار سنجی نادرست است", "danger")
            return redirect(request.referrer)

        # save user credential in session
        session["login"] = True
        session["account-id"] = Employee_db.id
        session.permanent = True
        return "redirect user to employee panel"

    else:
        flash("برخی موارد مقدار دهی نشده اند")
        return redirect(url_for("auth.employee_login_view"))


@auth.route("/login/")
def login_view():
    """Other Users Login"""
    form = LoginForm()
    return render_template("auth/login.html", form=form)
