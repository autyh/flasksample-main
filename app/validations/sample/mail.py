from wtforms import Form, BooleanField, StringField, PasswordField, RadioField, TextField, SelectField, IntegerField, HiddenField, validators
from flask_wtf import FlaskForm

class MailIndexForm(FlaskForm):
    nickname = StringField('ニックネーム', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=60, message='4文字以上60文字以内で入力してください。')])

    email = StringField('メールアドレス', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=6, max=35, message='6文字以上35文字以内で入力してください。'),
                validators.Email(message='正しいメールアドレスを入力してください。')
                ])

    confirm = BooleanField('確認しました', validators=[validators.DataRequired(message='必須項目です。')])
