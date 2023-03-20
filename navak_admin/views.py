import os.path

from flask import (render_template, request, send_from_directory)

from navak_admin import admin
from navak_auth import models as UserModel
from navak_auth.utils import admin_login_required
import navak_admin.forms as AdminForms
import navak_config.config as config


@admin.route("/private/static/<path:path>")
@admin_login_required
def private_static(path):
    """
        this view serve static file only for admins that login to there accounts
    :param path:
    :return: static file
    """
    if os.path.exists(os.path.join(config.ADMIN_PRIVATE_STATIC, path)):
        return send_from_directory(config.ADMIN_PRIVATE_STATIC, path)
    else:
        return "File Not Found", 404


@admin.route("/")
@admin_login_required
def index_view():
    content = {
        "page": "dashboard"
    }
    return render_template("admin/index.html", content=content)


@admin.route("/manage/users/")
@admin_login_required
def manage_users():
    page = request.args.get(key="page", default=1, type=int)
    all_users = UserModel.User.query.paginate(page=page, per_page=10)
    content = {
        "page": "manage-users",
        "users": all_users,
        "current_page": page,
    }
    return render_template("admin/manage-users.html", content=content)


@admin.route("/manage/users/add/")
@admin_login_required
def add_new_user():
    """
        this view return html page for adding new user to app
    :return:
    """
    content = {
        "page": "manage-users"
    }
    UserForm = AdminForms.AddNewUserForm()
    EmployeeForm = AdminForms.AddNewEmployeeForm()
    return render_template("admin/AddNewUser.html", content=content, UserForm=UserForm, EmployeeForm=EmployeeForm)

@admin.route("/setting")
@admin_login_required
def setting():
    content = {
        "page": "setting"
    }
    return render_template("admin/setting.html", content=content)
