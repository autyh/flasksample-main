import re
import dns.resolver
import socket
import smtplib
import logging
import sys
from app.lib.mail import mail
from flask import current_app
from flask_mail import Message

logger = logging.getLogger(__name__)

def send_mail(template, rcptcmd=None):

    try:

        message = template.splitlines()

        logger.debug('!!!!!! current_app.config[MAIL_SERVER]:' + current_app.config['MAIL_SERVER'])
        logger.debug('!!!!!! current_app.config[MAIL_PORT]:' + str(current_app.config['MAIL_PORT']))
        logger.debug('!!!!!! current_app.config[MAIL_USERNAME]:' + current_app.config['MAIL_USERNAME'])
        logger.debug('!!!!!! current_app.config[MAIL_PORT]:' + str(current_app.config['MAIL_PASSWORD']))

        subject = message[0].replace('subject:','')
        mail_from =  message[1].replace('from:','')
        mail_to = message[2].replace('to:','')
        mail_body = ''

        for num in range(3, len(message)):
            mail_body += message[num] + '\n'

            msg = Message(subject=subject,
                          sender=mail_from,
                          recipients=[mail_to],
                          rcpt_options=rcptcmd
                          )

            msg.body = mail_body

        mail.send(msg)
        result = True

    except Exception as e:
        tb = sys.exc_info()[2]
        logger.error("--- User update exception message:{0}".format(e.with_traceback(tb)))
        result = False

    return result


def mail_check(template, mail_address):

    # メールアドレス構文チェック
    match = re.match('[A-Za-z0-9._+]+@[A-Za-z]+.[A-Za-z]', mail_address)
    if match == None:
        logger.debug('email Syntax error')
        status = 1
        return status

    # ドメインチェック
    mail_domain = re.search("(.*)(@)(.*)", mail_address).group(3) # ドメイン部分の取り出し
    try:
        records  = dns.resolver.query(mail_domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
    except Exception as e:
        logger.debug('None of DNS query names exist')
        status = 2
        return status

    # メールアドレス存在チェック
"""
    local_host = socket.gethostname()

    #server = smtplib.SMTP(host=current_app.config['MAIL_SERVER'], port=current_app.config['MAIL_PORT'], timeout=5)
    server = smtplib.SMTP(timeout=5)
    server.set_debuglevel(0)

    try:
        server.connect(mxRecord)
        server.helo(local_host)
        server.mail('test@example.com')
        code, message = server.rcpt(str(mail_address))
        server.quit()

        if code == 250:
            status = 0
            return status
        else:
            logger.debug('Address does not exists')
            status = 3
            return status

    except Exception as e:
        logger.debug(e)
        status = 4
        return status
"""
