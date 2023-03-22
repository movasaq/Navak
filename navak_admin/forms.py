from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Length

from navak_admin.utils import get_all_education, get_all_work_position


class AddNewUserForm(FlaskForm):
    username = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=6, max=64)
        ]
    )

    password = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=6, max=102)
        ]
    )
    fullname = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=6, max=102)
        ]
    )
    active = RadioField(
        choices=[("inactive", "غیرفعال"), ("active", "فعال")],
        validators=[
            DataRequired(),
            InputRequired(),
        ]
    )
    usertag = StringField()

    submit = SubmitField()


class AddNewEmployeeForm(FlaskForm):
    username = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=6, max=64)
        ]
    )

    password = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=6, max=102)
        ]
    )
    FirstName = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=1, max=64)
        ]
    )
    LastName = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=1, max=64)
        ]
    )
    FatherName = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=6, max=64)
        ]
    )
    BirthDay = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
        ]
    )
    MeliCode = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=1, max=32)
        ]
    )
    BirthDayLocation = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=1, max=64)
        ]
    )
    PhoneNumber = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=11, max=11)
        ]
    )
    EmergencyPhone = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=11, max=11)
        ]
    )

    Address = TextAreaField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=1, max=256)
        ]
    )

    Education = SelectField(
        choices=get_all_education(),
        validators=[
            DataRequired(),
            InputRequired()
        ]
    )

    StaffCode = IntegerField(
        validators=[
            DataRequired(),
            InputRequired(),
        ]
    )

    ContractType = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
            Length(min=1, max=64)
        ]
    )
    StartContract = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
        ]
    )
    EndContract = StringField(
        validators=[
            DataRequired(),
            InputRequired(),
        ]
    )

    WorkPosition = SelectField(
        choices=get_all_work_position(),
        validators=[
            DataRequired(),
            InputRequired()
        ]
    )

    Marid = RadioField(
        choices=[("marid", "متاهل"), ("bachelor", "مجرد")],
        validators=[
            DataRequired(),
            InputRequired(),
        ]
    )
    Children = IntegerField()
    BaseSalary = IntegerField(
        validators=[
            DataRequired(),
            InputRequired(),
        ]
    )

    Active = RadioField(
        choices=[("inactive", "غیرفعال"), ("active", "فعال")],
        validators=[
            DataRequired(),
            InputRequired(),
        ]
    )

    submit = SubmitField()
