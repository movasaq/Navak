from navak import app
from navak_auth import models as UserModel


@app.template_filter("RoleName")
def RoleName(Role_id: int):
    """
        this template filter take a role id
        and return name of that role id
    :param Role id:
    :return: Role Name
    """
    if not (RoleDB := UserModel.Role.query.filter(UserModel.Role.id == Role_id).first()):
        return "NULL"
    else:
        return RoleDB.RoleName
