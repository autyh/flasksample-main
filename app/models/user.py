from datetime import datetime
from dateutil import relativedelta
from app.lib.db import db, ma
import logging
import sys

logger = logging.getLogger(__name__)

class User(db.Model):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'ET_ENTRY'

    ENTRYNO = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ENTRYDIV = db.Column(db.Integer, nullable=False)
    ENTRYSOURCEDIV= db.Column(db.Integer, nullable=True)
    STATUS = db.Column(db.Integer, nullable=False)
    ENTRYDATE = db.Column(db.Date(), nullable=True)
    ENDDATE = db.Column(db.Date(), nullable=True)
    THANKYOUMAILEDATE = db.Column(db.Date(), nullable=True)
    NOTICECANCELDATE = db.Column(db.Date(), nullable=True)
    ACCOUNTDELDATE = db.Column(db.Date, nullable=True)
    ACCOUNTTYPE = db.Column(db.Integer, nullable=True)
    NAME = db.Column(db.String(200), nullable=False)
    KANA = db.Column(db.String(400), nullable=False)
    BIRTHDAY = db.Column(db.Date, nullable=True)
    SEX= db.Column(db.Integer, nullable=True)
    TELHOME = db.Column(db.String(15), nullable=False)
    EMAIL = db.Column(db.String(300), nullable=False)
    UPDATEDATE = db.Column(db.DateTime, nullable=True)
    OPERATOR= db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.ENTRYNO

    def dict():
        return {'ENTRYNO':None, 'ENTRYDIV':None, 'ENTRYSOURCEDIV':None, 'STATUS':None, 'ENTRYDATE':None, 'ENDDATE':None,'THANKYOUMAILEDATE':None,
                'NOTICECANCELDATE':None, 'ACCOUNTDELDATE':None, 'ACCOUNTTYPE':None, 'NAME':None, 'KANA':None,  'BIRTHDAY':None,
                'SEX':None, 'TELHOME':None, 'EMAIL':None, 'UPDATEDATE':None }


    def select_all():

        logger.debug("--- User select_all start ---")

        try:
            user_list = db.session.query(User).all()
        except Exception as e:
            user_list = list()
            tb = sys.exc_info()[2]
            logger.error("--- User select_all exception message:{0}".format(e.with_traceback(tb)))

        logger.debug("--- User select_all end   ---")
        return user_list

    def select_status(status):

        logger.debug("--- User select_status start ---")

        try:
            user_list =  db.session.query(User).filter(User.STATUS == status).all()
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- User select_status exception message:{0}".format(e.with_traceback(tb)))

        logger.debug("--- User select_status end   ---")
        return user_list


    def insert(user):

        logger.debug("--- User insert start ---")
        result = False

        try:
            record = User(
                ENTRYDIV = 5,
                ENTRYSOURCEDIV = 1,
                STATUS = 1,
                ENTRYDATE = datetime.now(),
                ENDDATE = user['UENTRYDATE'],
                THANKYOUMAILEDATE = user['UTHANKYOUMAILEDATE'],
                NOTICECANCELDATE = user['UNOTICECANCELDATE'],
                ACCOUNTDELDATE = user['UACCOUNTDELDATE'],
                ACCOUNTTYPE = 0,
                NAME = user['UNAME'],
                KANA = user['UKANA'],
                BIRTHDAY = user['UBIRTHDAY'],
                SEX = 0,
                TELHOME = "",
                EMAIL = user['UEMAIL'],
                UPDATEDATE = datetime.now(),
            )

            logger.debug("--- User insert add record ---")
            # insert into users(name, address, tel, mail) values(...)
            db.session.add(record)
            db.session.commit()
            result = True
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- User insert exception message:{0}".format(e.with_traceback(tb)))
            db.session.rollback()

        logger.debug("--- User insert end   ---")
        return result

    def select_id(id):

        logger.debug("--- User select_id start ---")

        try:
            user = db.session.query(User).filter(User.ENTRYNO==id).first()
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- User select_id exception message:{0}".format(e.with_traceback(tb)))

        logger.debug("--- User select_id end   ---")
        return user


    def update(user):

        logger.debug("--- User update start ---")
        result = False

        try:

            update_user = db.session.query(User).filter(User.ENTRYNO==user['ENTRYNO']).first()

            if user['ENTRYDIV'] != None:
                update_user.UENTRYDIV =  user['ENTRYDIV']

            if user['ENTRYSOURCEDIV'] != None:
                update_user.UENTRYSOURCEDIV =  user['ENTRYSOURCEDIV']

            if user['ENTRYSOURCEDIV'] != None:
                update_user.UENTRYSOURCEDIV = user['ENTRYSOURCEDIV']

            if user['ENTRYDATE'] != None:
                update_user.UENTRYDATE = user['ENTRYDATE']

            if user['ENDDATE'] != None:
                update_user.UENDDATE = user['ENDDATE']

            if user['THANKYOUMAILEDATE'] != None:
                update_user.UTHANKYOUMAILEDATE = user['THANKYOUMAILEDATE']

            if user['NOTICECANCELDATE'] != None:
                update_user.UNOTICECANCELDATE = user['NOTICECANCELDATE']

            if user['ACCOUNTDELDATE'] != None:
                update_user.UACCOUNTDELDATE = user['ACCOUNTDELDATE']

            if user['ACCOUNTTYPE'] != None:
                update_user.UACCOUNTTYPE = user['ACCOUNTTYPE']

            if user['NAME'] != None:
                update_user.UNAME = user['NAME']

            if user['KANA'] != None:
                update_user.UKANA = user['KANA']

            if user['BIRTHDAY'] != None:
                update_user.UBIRTHDAY = user['BIRTHDAY']

            if user['SEX'] != None:
                update_user.USEX = user['SEX']

            if user['TELHOME'] != None:
                update_user.UTELHOME = user['TELHOME']

            if user['EMAIL'] != None:
                update_user.UEMAIL = user['EMAIL']

            if user['STATUS'] != None:
                update_user.USTATUS = user['STATUS']

            update_user.UPDATEDATE = datetime.now()

            logger.debug("--- User update update_user ---")
            # insert into users(name, address, tel, mail) values(...)
            db.session.add(update_user)
            db.session.commit()
            result = True
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- User update exception message:{0}".format(e.with_traceback(tb)))
            db.session.rollback()

        logger.debug("--- User update end   ---")
        return result


    def delete(id):

        logger.debug("--- User update start ---")
        result = False

        try:
            delete_user = db.session.query(User).filter(User.ENTRYNO==id).first()

            logger.debug("--- User delete delete record ---")
            # insert into users(name, address, tel, mail) values(...)
            db.session.delete(delete_user)
            db.session.commit()
            result = True
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- User delete exception message:{0}".format(e.with_traceback(tb)))
            db.session.rollback()

        logger.debug("--- User delete end   ---")
        return result
