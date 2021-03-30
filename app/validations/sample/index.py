from wtforms import Form, BooleanField, StringField, PasswordField, RadioField, TextField, SelectField, IntegerField, HiddenField, validators
from flask_wtf import FlaskForm

class SampleIndexForm(FlaskForm):
    status = SelectField('ステータス', choices=[(0, '選択無し'), (1, '新規登録'), (99, '取込済')])
