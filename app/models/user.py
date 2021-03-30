from datetime import datetime
from dateutil import relativedelta
from app.lib.db import db, ma
import logging
import sys

logger = logging.getLogger(__name__)

class User(db.Model):
    __bind_key__ = 'mysql_bind'
    __tablename__ = 'UET_ENTRY'

    UENTRYNO = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UENTRYDIV = db.Column(db.Integer, nullable=False)
    UENTRYSOURCEDIV= db.Column(db.Integer, nullable=True)
    USTATUS = db.Column(db.Integer, nullable=False)
    UENTRYDATE = db.Column(db.Date(), nullable=True)
    UENDDATE = db.Column(db.Date(), nullable=True)
    UTHANKYOUMAILEDATE = db.Column(db.Date(), nullable=True)
    UNOTICECANCELDATE = db.Column(db.Date(), nullable=True)
    UACCOUNTDELDATE = db.Column(db.Date, nullable=True)
    UACCOUNTTYPE = db.Column(db.Integer, nullable=True)
    UNAME = db.Column(db.String(200), nullable=False)
    UKANA = db.Column(db.String(400), nullable=False)
    UBIRTHDAY = db.Column(db.Date, nullable=True)
    USEX= db.Column(db.Integer, nullable=True)
    UTELHOME = db.Column(db.String(15), nullable=False)
    UEMAIL = db.Column(db.String(300), nullable=False)
    UUPDATEDATE = db.Column(db.DateTime, nullable=True)
    UOPERATOR= db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.UENTRYNO

    def dict():
        return {'UENTRYNO':None, 'UENTRYDIV':None, 'UENTRYSOURCEDIV':None, 'USTATUS':None, 'UENTRYDATE':None, 'UENDDATE':None,'UTHANKYOUMAILEDATE':None,
                'UNOTICECANCELDATE':None, 'UACCOUNTDELDATE':None, 'UACCOUNTTYPE':None, 'UNAME':None, 'UKANA':None,  'UBIRTHDAY':None,
                'USEX':None, 'UTELHOME':None, 'UEMAIL':None, 'UUPDATEDATE':None }


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
            user_list =  db.session.query(User).filter(User.USTATUS == status).all()
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
                UENTRYDIV = 5,
                UENTRYSOURCEDIV = 1,
                USTATUS = 1,
                UENTRYDATE = datetime.now(),
                UENDDATE = user['UENTRYDATE'],
                UTHANKYOUMAILEDATE = user['UTHANKYOUMAILEDATE'],
                UNOTICECANCELDATE = user['UNOTICECANCELDATE'],
                UACCOUNTDELDATE = user['UACCOUNTDELDATE'],
                UACCOUNTTYPE = 0,
                UNAME = user['UNAME'],
                UKANA = user['UKANA'],
                UBIRTHDAY = user['UBIRTHDAY'],
                USEX = 0,
                UTELHOME = "",
                UEMAIL = user['UEMAIL'],
                UUPDATEDATE = datetime.now(),
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
            user = db.session.query(User).filter(User.UENTRYNO==id).first()
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- User select_id exception message:{0}".format(e.with_traceback(tb)))

        logger.debug("--- User select_id end   ---")
        return user


    def update(user):

        logger.debug("--- User update start ---")
        result = False

        try:

            update_user = db.session.query(User).filter(User.UENTRYNO==user['UENTRYNO']).first()

            if user['UENTRYDIV'] != None:
                update_user.UENTRYDIV =  user['UENTRYDIV']

            if user['UENTRYSOURCEDIV'] != None:
                update_user.UENTRYSOURCEDIV =  user['UENTRYSOURCEDIV']

            if user['UENTRYSOURCEDIV'] != None:
                update_user.UENTRYSOURCEDIV = user['UENTRYSOURCEDIV']

            if user['UENTRYDATE'] != None:
                update_user.UENTRYDATE = user['UENTRYDATE']

            if user['UENDDATE'] != None:
                update_user.UENDDATE = user['UENDDATE']

            if user['UTHANKYOUMAILEDATE'] != None:
                update_user.UTHANKYOUMAILEDATE = user['UTHANKYOUMAILEDATE']

            if user['UNOTICECANCELDATE'] != None:
                update_user.UNOTICECANCELDATE = user['UNOTICECANCELDATE']

            if user['UACCOUNTDELDATE'] != None:
                update_user.UACCOUNTDELDATE = user['UACCOUNTDELDATE']

            if user['UACCOUNTTYPE'] != None:
                update_user.UACCOUNTTYPE = user['UACCOUNTTYPE']

            if user['UNAME'] != None:
                update_user.UNAME = user['UNAME']

            if user['UKANA'] != None:
                update_user.UKANA = user['UKANA']

            if user['UBIRTHDAY'] != None:
                update_user.UBIRTHDAY = user['UBIRTHDAY']

            if user['USEX'] != None:
                update_user.USEX = user['USEX']

            if user['UTELHOME'] != None:
                update_user.UTELHOME = user['UTELHOME']

            if user['UEMAIL'] != None:
                update_user.UEMAIL = user['UEMAIL']

            if user['USTATUS'] != None:
                update_user.USTATUS = user['USTATUS']

            update_user.UUPDATEDATE = datetime.now()

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
            delete_user = db.session.query(User).filter(User.UENTRYNO==id).first()

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
