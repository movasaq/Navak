from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length


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
