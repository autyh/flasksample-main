from flask import Blueprint
from flask import request, redirect, g, url_for, render_template, flash, session
from flask_wtf import csrf
from app.func.web import *
from app.validations.sample.web import WebIndexForm
import logging
from flask_paginate import Pagination, get_page_parameter #ページネーションを行う場合は必要

ROWS_PER_PAGE=5

app = Blueprint('index', __name__, url_prefix='/')
# 設定ファイルから読み込んでいるので記述の必要なし
#app.secret_key = 'uhsession'

logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logger.debug("start login POST")
    form = WebIndexForm()

    if request.method == 'GET':

        return render_template("/index.html", form=form)

    logger.debug("start login POST")
    form = WebIndexForm(request.form)

    if request.method == 'POST':
        return render_template('/index.html', form=form)

    return render_template('/index.html', form=form)
