from flask import (session, render_template, redirect, url_for, flash, request)

from navak_auth import auth
from navak_auth.forms import LoginForm
from navak_auth.models import User
from navak_config.config import LOGIN_PATHS_MATTERIAL
from navak_employee.models import Employee


@auth.route("/login/", methods=["POST"])
def login_post():
    """
        this view take a post request for login Employees to there panel
    :return: Html
    """
    form = LoginForm()

    if form.validate():
        # check user select valid login path
        if form.usergroup.data not in LOGIN_PATHS_MATTERIAL[0]:
            flash("گروه انتخابی کاربر نادرست است", "danger")
            return redirect(request.referrer)

        # check user type is in ["admin", "engineer", "office", "gard"]
        if form.usergroup.data != "employee":
            if not (user_db := User.query.filter(User.username == form.username.data).first()):
                flash("کاربری با نام کاربری وارد شده یافت نشد", "danger")
                return redirect(request.referrer)

            if not user_db.check_password(form.password.data):
                flash("اعتبار سنجی نادرست است", "danger")
                return redirect(request.referrer)

            if form.usergroup.data == "admin":
                session["login"] = True
                session["account-id"] = user_db.id
                session.permanent = True
                return redirect(url_for('admin.index_view'))

        # if user select employee group type
        else:
            if not (Employee_db := Employee.query.filter(Employee.UserName == form.username.data).first()):
                flash("کاربری با نام کاربری وارد شده یافت نشد", "danger")
                return redirect(request.referrer)

            if not Employee_db.check_password(form.password.data):
                flash("اعتبار سنجی نادرست است", "danger")
                return redirect(request.referrer)

        # otherwise redirect user to login page
        return redirect(request.referrer)

    # if form is not validate
    else:
        flash("برخی موارد مقدار دهی نشده اند")
        return redirect(url_for("auth.employee_login_view"))


@auth.route("/login/")
def login_view():
    """Users Login"""
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@auth.route("/logout/")
def logout_view():
    """logout users"""
    session.clear()
    return redirect(url_for("index_view"))
