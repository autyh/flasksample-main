from wtforms import Form, BooleanField, StringField, PasswordField, RadioField, TextField, SelectField, IntegerField, HiddenField, validators
from flask_wtf import FlaskForm

class OracleIndexForm(FlaskForm):
    status = SelectField('ステータス', choices=[(0, '選択無し'), (1, '新規登録'), (99, '取込済')])


class OracleCreateForm(FlaskForm):
    username = StringField('名前', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=60, message='4文字以上60文字以内で入力してください。')])

    email = StringField('メールアドレス', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=6, max=35, message='6文字以上35文字以内で入力してください。'),
                validators.Email(message='正しいメールアドレスを入力してください。')
                ])

    confirm = BooleanField('確認しました', validators=[validators.DataRequired(message='必須項目です。')])


class OracleUpdateForm(FlaskForm):

    entryno = HiddenField('No.')

    username = StringField('名前', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=60, message='4文字以上60文字以内で入力してください。')])

    userkana = StringField('カナ名', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=60, message='4文字以上60文字以内で入力してください。')])

    email = StringField('メールアドレス', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=6, max=35, message='6文字以上35文字以内で入力してください。'),
                validators.Email(message='正しいメールアドレスを入力してください。')
                ])

    sex = RadioField('性別', choices=[(0, '回答しない'), (1, '男性'), (2, '女性'), (3, 'その他')])

    status = SelectField('ステータス', choices=[(1, '新規登録'), (2, 'ID作成済'), (3, '入金済')])

    confirm = BooleanField('確認しました', validators=[validators.DataRequired(message='必須項目です。')])


class OracleDeleteForm(FlaskForm):

    entryno = HiddenField('No.')

    username = StringField('名前', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=60, message='4文字以上60文字以内で入力してください。')])

    userkana = StringField('カナ名', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=60, message='4文字以上60文字以内で入力してください。')])

    email = StringField('メールアドレス', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=6, max=35, message='6文字以上35文字以内で入力してください。'),
                validators.Email(message='正しいメールアドレスを入力してください。')
                ])

    sex = RadioField('性別', choices=[(0, '回答しない'), (1, '男性'), (2, '女性'), (3, 'その他')])

    status = SelectField('ステータス', choices=[(1, '新規登録'), (2, 'ID作成済'), (3, '入金済')])

    confirm = BooleanField('確認しました', validators=[validators.DataRequired(message='必須項目です。')])
