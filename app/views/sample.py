from flask import Blueprint #ファイル野パスを指定する為に必ず必要
from flask import request, redirect, g, url_for, render_template, flash, session
from flask_wtf import csrf #セキュリティチェックの為必ず必要
from flask_paginate import Pagination, get_page_parameter #ページネーションを行う場合は必要
from app.func.mail import send_mail #メールを送信する場合は必要
from app.models import Entry, User #モデルを利用する場合は必要
from app.validations.sample.oracle import OracleIndexForm, OracleCreateForm, OracleUpdateForm, OracleDeleteForm
from app.validations.sample.mysql import MySqlCreateForm, MySqlUpdateForm,MySqlDeleteForm, MySqlIndexForm
from app.validations.sample.mail import MailIndexForm
from app.validations.sample.web import WebIndexForm
from app.validations.sample.index import SampleIndexForm
import mojimoji
import logging

USER_STATUS_LIST=[(0, '選択無し'), (1, '新規登録')]
ENTRY_STATUS_LIST=[(0, '選択無し'), (1, '新規登録'), (99, '取込済')]

ORACLE_PATH='/sample/oracle/'
MYSQL_PATH='/sample/mysql/'
MAIL_PATH='/sample/mail/'
WEB_PATH='/sample/web/'

ROWS_PER_PAGE=5

# sample.pyを呼び出す為の記述
app = Blueprint('sample', __name__, url_prefix='/sample')
# 設定ファイルから読み込んでいるので記述の必要なし
#app.secret_key = 'uhsession'

logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template("/sample/index.html")


@app.route('/oracle/', methods = ['GET','POST'])
def oracle_index():

    form = OracleIndexForm()

    if request.method == 'GET':
        entries = Entry.select_status(0)
        return render_template(ORACLE_PATH + 'index.html', form=form, entries=entries, entry_status_list=ENTRY_STATUS_LIST)

    form = OracleIndexForm(request.form)

    if request.method == 'POST' and form.validate():
        if request.form['status'] != '0':
            entries = Entry.select_status(request.form['status'])
        else:
            entries = Entry.select_status(0)
        return render_template(ORACLE_PATH + 'index.html', form=form, entries=entries, entry_status_list=ENTRY_STATUS_LIST)

    return render_template(ORACLE_PATH + 'index.html', form=form, entry_status_list=ENTRY_STATUS_LIST)

@app.route('/oracle/create', methods = ['GET','POST'])
def oracle_create():

    logger.debug("start oracle_create")
    form = OracleCreateForm()

    if request.method == 'GET':
        logger.debug("start oracle_create GET")
        return render_template(ORACLE_PATH + '/create.html',form=form)

    logger.debug("start oracle_create POST")
    form = OracleCreateForm(request.form)

    if request.method == 'POST' and form.validate():
        session['username'] = request.form['username']
        session['email'] =  request.form['email']

        #logger.debug("UT_ENTRYTEMP insert")
        entry = Entry.dict()
        entry['UNAME'] = session['username']
        entry['UKANA'] = mojimoji.zen_to_han(session['username'])
        entry['UEMAIL'] = session['email']

        if Entry.insert(entry):
            flash("登録できました。","success")
        else:
            flash("登録できませんでした。","danger")

        return redirect("/sample/oracle/")

    return render_template(ORACLE_PATH + 'create.html',form=form)


@app.route('/oracle/update/<int:id>', methods = ['GET','POST'])
def oracle_update(id):

    logger.debug("start oracle_update")
    form = OracleUpdateForm()

    if request.method == 'GET':
        entry = Entry.select_id(id)
        #プルダウン/ラジオボタンは最初に設定しないとフォームがクリアされてしまう
        form.status.default = int(entry.USTATUS)
        form.sex.default = int(entry.USEX)
        print(form.status.default)
        form.process()
        form.entryno.data = entry.UENTRYNO
        form.username.data = entry.UNAME
        form.userkana.data = entry.UKANA
        form.email.data = entry.UEMAIL
        return render_template(ORACLE_PATH + 'update.html',form=form, entry=entry)

    logger.debug("start oracle_update POST")
    form = OracleUpdateForm(request.form)

    if request.method == 'POST' and form.validate():

        logger.debug("--- oracle_update POST  ---")
        #logger.debug("UT_ENTRYTEMP insert")
        entry = Entry.dict()
        entry['UENTRYNO'] = id
        entry['UNAME'] = request.form['username']
        entry['UKANA'] = mojimoji.zen_to_han(request.form['username'])
        entry['UEMAIL'] = request.form['email']
        entry['USEX'] = request.form['sex']
        entry['USTATUS'] = request.form['status']
        print(request.form['status'])
        logger.debug("--- oracle_update entry data  ---")

        if Entry.update(entry) and form.validate():
            flash("更新できました。","success")
        else:
            flash("更新できませんでした。","danger")

        return redirect("/sample/oracle/")

    return render_template(ORACLE_PATH + 'update.html',form=form)


@app.route('/oracle/delete/<int:id>', methods = ['GET','POST'])
def oracle_delete(id):

    logger.debug("start oracle_delete")
    form = OracleDeleteForm()

    if request.method == 'GET':
        entry = Entry.select_id(id)
        #プルダウン/ラジオボタンは最初に設定しないとフォームがクリアされてしまう
        form.status.default = int(entry.USTATUS)
        form.sex.default = int(entry.USEX)
        print(form.status.default)
        form.process()
        form.entryno.data = entry.UENTRYNO
        form.username.data = entry.UNAME
        form.userkana.data = entry.UKANA
        form.email.data = entry.UEMAIL

        return render_template('/sample/oracle/delete.html', form=form, entry=entry)

    logger.debug("start oracle_delete POST")
    form = OracleDeleteForm(request.form)

    if request.method == 'POST':

        if Entry.delete(id):
            flash("削除できました。","success")
        else:
            flash("削除できませんでした。","danger")

        return redirect(ORACLE_PATH)

    return render_template(ORACLE_PATH + 'delete.html', form=form)


@app.route('/mysql/', methods = ['GET','POST'])
def mysql_index():

    form = MySqlIndexForm()
    page = request.args.get(get_page_parameter(), type=int, default=1) #pagination manager

    if request.method == 'GET':
        logger.debug("check session input status")
        if 'inputstatus' in session and session['inputstatus'] != '0':
            # if get search value that set form items
            logger.debug("GET session inputstatus:" + session['inputstatus'] )
            form.status.default = int(session['inputstatus'])
            form.process()
            selectusers = User.select_status(session['inputstatus'])
        else:
            selectusers = User.select_all()

        users = selectusers[(page - 1)*ROWS_PER_PAGE: page*ROWS_PER_PAGE] # get display rows from selectuser by par page
        pagination = Pagination(page=page, per_page=ROWS_PER_PAGE, total=len(selectusers), css_framework='bootstrap4') # create pagination link

        return render_template(MYSQL_PATH + 'index.html', form=form, pagination=pagination, users=users, user_status_list=USER_STATUS_LIST)

    form = MySqlIndexForm(request.form)

    if request.method == 'POST' and form.validate():
        if request.form['status'] != '0':

            logger.debug("POST session inputstatus:" + session['inputstatus'] )
            session['inputstatus'] = request.form['status']
            selectusers = User.select_status(session['inputstatus'])
        else:
            session['inputstatus'] = '0'
            selectusers = User.select_all()

        users = selectusers[(page - 1)*ROWS_PER_PAGE: page*ROWS_PER_PAGE]

        pagination = Pagination(page=page, per_page=ROWS_PER_PAGE, total=len(selectusers), css_framework='bootstrap4')

        return render_template(MYSQL_PATH + 'index.html', form=form, pagination=pagination, users=users, user_status_list=USER_STATUS_LIST)

    return render_template(MYSQL_PATH + 'index.html', form=form, pagination=pagination, user_status_list=USER_STATUS_LIST)

@app.route('/mysql/create', methods = ['GET','POST'])
def mysql_create():

    logger.debug("start mysql_create")
    form = MySqlCreateForm()

    if request.method == 'GET':
        logger.debug("start mysql_create GET")
        return render_template(MYSQL_PATH + 'create.html',form=form)

    logger.debug("start mysql_create POST")
    form = MySqlCreateForm(request.form)

    if request.method == 'POST' and form.validate():
        session['username'] = request.form['username']
        session['email'] =  request.form['email']

        #logger.debug("UT_ENTRYTEMP insert")
        user = User.dict()
        user['UNAME'] = session['username']
        user['UKANA'] = mojimoji.zen_to_han(session['username'])
        user['UEMAIL'] = session['email']

        if User.insert(user):
            flash("登録できました。","success")
        else:
            flash("登録できませんでした。","danger")

        return redirect(MYSQL_PATH)

    return render_template(MYSQL_PATH + 'create.html',form=form)

@app.route('/mysql/update/<int:id>', methods = ['GET','POST'])
def mysql_update(id):

    logger.debug("start mysql_update")
    form = MySqlUpdateForm()

    if request.method == 'GET':
        user = User.select_id(id)
        #プルダウン/ラジオボタンは最初に設定しないとフォームがクリアされてしまう
        form.status.default = int(user.USTATUS)
        form.sex.default = int(user.USEX)
        print(form.status.default)
        form.process()
        form.entryno.data = user.UENTRYNO
        form.username.data = user.UNAME
        form.userkana.data = user.UKANA
        form.email.data = user.UEMAIL
        return render_template(MYSQL_PATH + 'update.html',form=form, user=user)

    logger.debug("start mysql_update POST")
    form = MySqlUpdateForm(request.form)

    if request.method == 'POST' and form.validate():

        logger.debug("--- mysql_update POST  ---")
        #logger.debug("UT_ENTRYTEMP insert")
        user = User.dict()
        user['UENTRYNO'] = id
        user['UNAME'] = request.form['username']
        user['UKANA'] = mojimoji.zen_to_han(request.form['username'])
        user['UEMAIL'] = request.form['email']
        user['USEX'] = request.form['sex']
        user['USTATUS'] = request.form['status']
        print(request.form['status'])
        logger.debug("--- mysql_update user data  ---")

        if User.update(user) and form.validate():
            flash("更新できました。","success")
        else:
            flash("更新できませんでした。","danger")

        return redirect(MYSQL_PATH)
    else:
        user = User.select_id(id)
        #プルダウン/ラジオボタンは最初に設定しないとフォームがクリアされてしまう
        form.status.default = int(user.USTATUS)
        form.sex.default = int(user.USEX)
        print(form.status.default)
        form.process()
        form.entryno.data = user.UENTRYNO
        form.username.data = user.UNAME
        form.userkana.data = user.UKANA
        form.email.data = user.UEMAIL

    return render_template(MYSQL_PATH + 'update.html',form=form, user=user)

@app.route('/mysql/delete/<int:id>', methods = ['GET','POST'])
def mysql_delete(id):

    logger.debug("start mysql_delete")
    form = MySqlDeleteForm()

    if request.method == 'GET':
        user = User.select_id(id)
        #プルダウン/ラジオボタンは最初に設定しないとフォームがクリアされてしまう
        form.status.default = int(user.USTATUS)
        form.sex.default = int(user.USEX)
        print(form.status.default)
        form.process()
        form.entryno.data = user.UENTRYNO
        form.username.data = user.UNAME
        form.userkana.data = user.UKANA
        form.email.data = user.UEMAIL
        return render_template(MYSQL_PATH + 'delete.html', form=form, user=user)

    logger.debug("start mysql_delete POST")
    form = MySqlDeleteForm(request.form)

    if request.method == 'POST':
        if User.delete(id):
            flash("削除できました。","success")
        else:
            flash("削除できませんでした。","danger")

        return redirect(MYSQL_PATH)

    return render_template(MYSQL_PATH + 'delete.html', form=form)


@app.route('/mail/', methods = ['GET','POST'])
def mail_index():

    logger.debug("start mail_index")
    form = MailIndexForm()

    if request.method == 'GET':
        logger.debug("start mail_index GET")
        return render_template(MAIL_PATH + 'index.html',form=form)

    logger.debug("start mail_index POST")
    form = MailIndexForm(request.form)

    if request.method == 'POST' and form.validate():
        # sample log output
        # sample mail send
        name = request.form['nickname']
        to = request.form['email']

        # mail 送信
        template = render_template('/mail/entry.txt', to=to, name=name)

        if send_mail(template):
            flash("送信できました。","success")
        else:
            flash("送信できませんでした。","danger")

        return redirect(MAIL_PATH)

    return render_template(MAIL_PATH + 'index.html',form=form)


@app.route('/web/', methods = ['GET','POST'])
def web_index():

    logger.debug("start web_index")
    form = WebIndexForm()

    if request.method == 'GET':
        logger.debug("start web_index GET")
        return render_template(WEB_PATH + 'index.html', form=form)

    form = WebIndexForm(request.form)
    logger.debug("start web_index POST")

    if request.method == 'POST':
        # sample log output
        # sample mail send

        return redirect(WEB_PATH)

    return render_template(WEB_PATH + 'index.html', form=form)
