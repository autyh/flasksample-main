from wtforms import Form, StringField, PasswordField, BooleanField, validators
from flask_wtf import FlaskForm

class WebIndexForm(FlaskForm):
    staffcd = StringField('担当者コード', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=60, message='4文字以上60文字以内で入力してください。')])

    password = PasswordField('パスワード', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=35, message='4文字以上35文字以内で入力してください。')])
