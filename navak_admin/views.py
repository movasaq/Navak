from flask import (render_template)

from navak_admin import admin
from navak_auth import models as UserModel
from navak_auth.utils import admin_login_required


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
    all_users = UserModel.User.query.all()
    content = {
        "page": "manage-users",
        "users": all_users,
    }
    return render_template("admin/manage-users.html", content=content)


@admin.route("/setting")
@admin_login_required
def setting():
    content = {
        "page": "setting"
    }
    return render_template("admin/setting.html", content=content)
