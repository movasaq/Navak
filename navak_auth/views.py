from flask import (session, render_template, redirect, url_for, flash, request)

from navak_auth import auth
from navak_auth.forms import LoginForm
from navak_employee.models import Employee
from navak_config.config import LOGIN_PATHS_MATTERIAL

@auth.route("/login/", methods=["POST"])
def login_post():
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

        if form.usergroup not in LOGIN_PATHS_MATTERIAL[0]:
            flash("گروه انتخاب کاربر نادرست است", "danger")
            return redirect(request.referrer)

        # get user group and redirect user to panel
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
    """Users Login"""
    form = LoginForm()
    return render_template("auth/login.html", form=form)
