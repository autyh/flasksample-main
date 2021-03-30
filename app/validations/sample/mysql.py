from wtforms import Form, BooleanField, StringField, PasswordField, RadioField, TextField, SelectField, IntegerField, HiddenField, validators
from flask_wtf import FlaskForm


class MySqlCreateForm(FlaskForm):
    username = StringField('名前', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=4, max=60, message='4文字以上60文字以内で入力してください。')])

    email = StringField('メールアドレス', validators=[
                validators.DataRequired(message='必須項目です。'),
                validators.Length(min=6, max=35, message='6文字以上35文字以内で入力してください。'),
                validators.Email(message='正しいメールアドレスを入力してください。')
                ])

    confirm = BooleanField('確認しました', validators=[validators.DataRequired(message='必須項目です。')])


class MySqlUpdateForm(FlaskForm):

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

    customerid = StringField('口座ID', validators=[
                validators.Length(min=6, max=35, message='6文字以上35文字以内で入力してください。')
                ])

    depositamount = IntegerField('入金額')

    sex = RadioField('性別', choices=[(0, '回答しない'), (1, '男性'), (2, '女性'), (3, 'その他')])

    confirm = BooleanField('確認しました', validators=[validators.DataRequired(message='必須項目です。')])

    status = SelectField('ステータス', choices=[(1, '新規登録'), (2, 'ID作成済'), (3, '入金済')])


class MySqlDeleteForm(FlaskForm):

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

    customerid = StringField('口座ID', validators=[
                validators.Length(min=6, max=35, message='6文字以上35文字以内で入力してください。')
                ])

    depositamount = IntegerField('入金額')

    sex = RadioField('性別', choices=[(0, '回答しない'), (1, '男性'), (2, '女性'), (3, 'その他')])

    confirm = BooleanField('確認しました', validators=[validators.DataRequired(message='必須項目です。')])

    status = SelectField('ステータス', choices=[(1, '新規登録'), (2, 'ID作成済'), (3, '入金済')])


class MySqlIndexForm(FlaskForm):
    status = SelectField('ステータス', choices=[(0, '選択無し'), (1, '新規登録'), (2, 'ID作成済'), (3, '入金済')])
