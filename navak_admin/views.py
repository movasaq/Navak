from flask import (render_template, request)

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
    page = request.args.get(key="page", default=1, type=int)
    all_users = UserModel.User.query.paginate(page=page, per_page=10)
    content = {
        "page": "manage-users",
        "users": all_users,
        "current_page": page,
    }
    return render_template("admin/manage-users.html", content=content)


@admin.route("/setting")
@admin_login_required
def setting():
    content = {
        "page": "setting"
    }
    return render_template("admin/setting.html", content=content)
