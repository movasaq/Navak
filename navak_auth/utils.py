from functools import wraps

from flask import session, abort

from navak_auth.models import User, Role
from navak_employee.models import Employee


def employee_login_required(func):
    """
        Decorator for
    :return: User Object from db
    """
    @wraps(func)
    def inner_func(*args, **kwargs):
        if not (account_id := session.get("account-id", None)):
            abort(401)

        employee_db = Employee.query.filter(Employee.id == account_id).first()
        if not employee_db:
            session.clear()
            abort(401)

        # check account is active
        if not employee_db.Active:
            session.clear()
            abort(401)

        return func(employee_db=employee_db, *args, **kwargs)
    return inner_func


def admin_login_required(func):
    """
        Decorator for admin

    :return: User Object from db
    """
    @wraps(func)
    def inner_func(*args, **kwargs):
        if not (account_id := session.get("account-id", None)):
            abort(401)

        if not (user_db := User.query.filter(User.id == account_id).first()):
            session.clear()
            abort(401)

        # check account is active
        if not user_db.Active:
            session.clear()
            abort(401)

        # get admin role object from db
        if not (role_db := Role.query.filter(Role.RoleName == "admin").first()):
            session.clear()
            abort(401)

        # check user have admin role
        if user_db.UserRole != role_db.id:
            session.clear()
            abort(401)

        return func(*args, **kwargs)
    return inner_func


def basic_login_required(func):
    """
        only check user have account id and its valid
    :return:
    """
    @wraps(func)
    def inner_func(*args, **kwargs):
        if not (account_id := session.get("account-id", None)):
            abort(401)

        if not (user_db := User.query.filter(User.id == account_id).first()):
            session.clear()
            abort(401)

        # check account is active
        if not user_db.Active:
            session.clear()
            abort(401)

        return func(*args, **kwargs)
    return inner_func
