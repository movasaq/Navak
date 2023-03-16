from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import Length, DataRequired, InputRequired


class EmployeeLoginForm(FlaskForm):
    """
        Login Form Only for Employees Login
    """

    username = StringField(
        validators=[
            InputRequired(message="وارد کردن داده در این فیلد الزامی است"),
            DataRequired(message="وارد کردن داده در این فیلد الزامی است"),
            Length(max=64, min=6, message="حداکثر طول نام کاربری 64 کاراکتر و حداقل 6 کاراکتر است")
        ]
    )

    password = PasswordField(
        validators=[
            InputRequired(message="وارد کردن داده در این فیلد الزامی است"),
            DataRequired(message="وارد کردن داده در این فیلد الزامی است"),
            Length(max=64, min=6, message="حداکثر طول گذرواژه 64 کاراکتر و حداقل 6 کاراکتر است")
        ]
    )

    submit = SubmitField()
