import os.path

import sqlalchemy.exc as sqlalchemy_except
from flask import (render_template, request, send_from_directory, redirect, flash, url_for)

import navak_admin.forms as AdminForms
import navak_config.config as config
from navak.extensions import db
from navak.utils import validate_date, validate_phone
from navak_admin import admin
from navak_auth import models as UserModel
from navak_auth.utils import admin_login_required
from navak_employee import models as EmployeeModel


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


@admin.route("/manage/users/add/employee/", methods=["POST"])
@admin_login_required
def add_new_employee():
    """
        this view take a post request for create a new employee
    :return:
    """
    content = {
        "page": "manage-users"
    }
    EmployeeForm = AdminForms.AddNewEmployeeForm(request.form)

    if not EmployeeForm.validate():
        print(EmployeeForm.errors)
        flash("برخی موارد مقدار دهی نشده اند", "danger")
        return redirect(url_for("admin.add_new_user"))

    if EmployeeForm.validate():

        employee = EmployeeModel.Employee()

        # validate all dates in form
        if not (birthday := validate_date(EmployeeForm.BirthDay.data)):
            flash("تاریخ تولد با فرمت درست وارد نشده است", "danger")
            return redirect(url_for("admin.add_new_user"))

        if not (start_contract := validate_date(EmployeeForm.StartContract.data)):
            flash("تاریخ شروع قرارداد با فرمت درست وارد نشده است", "danger")
            return redirect(url_for("admin.add_new_user"))

        if not (end_contract := validate_date(EmployeeForm.EndContract.data)):
            flash("تایخ پایان قرارداد با فرمت درست وارد نشده است", "danger")
            return redirect(url_for("admin.add_new_user"))

        if not (phonenumber := validate_phone(EmployeeForm.PhoneNumber.data)):
            flash("تایخ پایان قرارداد با فرمت درست وارد نشده است", "danger")
            return redirect(url_for("admin.add_new_user"))

        if not (emergencyPhone := validate_phone(EmployeeForm.EmergencyPhone.data)):
            flash("تایخ پایان قرارداد با فرمت درست وارد نشده است", "danger")
            return redirect(url_for("admin.add_new_user"))

        if not (workposition := EmployeeModel.WorkPosition.query.filter(
                EmployeeModel.WorkPosition.Name == EmployeeForm.WorkPosition.data).first()):
            flash("موقعیت شغلی به درستی وارد نشده است", "danger")
            print(EmployeeForm.WorkPosition.data)
            return redirect(url_for("admin.add_new_user"))

        if not (education := EmployeeModel.Education.query.filter(
                EmployeeModel.Education.Name == EmployeeForm.Education.data).first()):
            flash("تحصیلات به درستی وارد نشده است", "danger")
            print(EmployeeForm.Education.data)
            return redirect(url_for("admin.add_new_user"))

        print(end_contract, start_contract)

        employee.set_public_key()

        employee.UserName = EmployeeForm.username.data.strip()
        employee.set_password(EmployeeForm.password.data.strip())
        employee.Active = True if EmployeeForm.Active.data == "active" else False
        employee.Address = EmployeeForm.Address.data.strip()
        employee.BaseSalary = EmployeeForm.BaseSalary.data
        employee.BirthDay = birthday
        employee.StaffCode = EmployeeForm.StaffCode.data
        employee.StartContract = start_contract
        employee.EndContract = end_contract
        employee.BirthLocation = EmployeeForm.BirthDayLocation.data
        employee.ContractType = EmployeeForm.ContractType.data
        employee.EmergencyPhone = emergencyPhone
        employee.Married = True if EmployeeForm.Marid.data == "marid" else False
        employee.Children = EmployeeForm.Children.data if EmployeeForm.Children.data else 0
        employee.FatherName = EmployeeForm.FatherName.data
        employee.FirstName = EmployeeForm.FirstName.data
        employee.LastName = EmployeeForm.LastName.data
        employee.PhoneNumber = phonenumber
        employee.MeliCode = EmployeeForm.MeliCode.data
        employee.WorkPosition = workposition.id
        employee.Education = education.id
        employee.calculate_vacation_hour()
        print(employee.BaseSalary)

        # check this field should be unique
        # username - phone - staff code - melicode
        if (EmployeeModel.Employee.query.filter(EmployeeModel.Employee.UserName == employee.UserName).first()):
            flash("کاربری با نام کابری وارد شده وجود دارد", "success")
            return redirect(url_for('admin.add_new_user'))

        if (EmployeeModel.Employee.query.filter(EmployeeModel.Employee.PhoneNumber == employee.PhoneNumber).first()):
            flash("کاربری با شماره تلفن وارد شده وجود دارد", "success")
            return redirect(url_for('admin.add_new_user'))

        if (EmployeeModel.Employee.query.filter(EmployeeModel.Employee.StaffCode == employee.StaffCode).first()):
            flash("کاربری با شماره کارمندی وارد شده وجود دارد", "success")
            return redirect(url_for('admin.add_new_user'))

        if (EmployeeModel.Employee.query.filter(EmployeeModel.Employee.MeliCode == employee.MeliCode).first()):
            flash("کاربری با شماره ملی وارد شده وجود دارد", "success")
            return redirect(url_for('admin.add_new_user'))

        db.session.add(employee)
        db.session.commit()
        try:
            pass
        except sqlalchemy_except.IntegrityError:
            db.session.rollback()
            flash("خطایی رخ داد بعدا دوباره امتحان کنید", "danger")
            return redirect(url_for('admin.add_new_user'))

        else:
            flash("کارمند با موفقیت اضافه گردید", "success")
            return redirect(url_for('admin.add_new_user'))


@admin.route("/setting")
@admin_login_required
def setting():
    content = {
        "page": "setting"
    }
    return render_template("admin/setting.html", content=content)
