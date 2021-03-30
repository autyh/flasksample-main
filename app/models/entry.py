from datetime import datetime
from dateutil import relativedelta
from app.lib.db import db, ma
import logging
import sys

logger = logging.getLogger(__name__)


class  Entry(db.Model):
    __tablename__ = 'T_ENTRYTEMP'

    ENTRYNO = db.Column(db.Integer, primary_key=True)
    ENTRYDIV = db.Column(db.Integer, nullable=False)
    ENTRYSOURCEDIV = db.Column(db.Integer, nullable=False)
    STATUS = db.Column(db.Integer, nullable=False)
    PRIORITY = db.Column(db.Integer, nullable=False)
    ENTRYDATE  = db.Column(db.DateTime())
    ENDDATE  = db.Column(db.DateTime())
    THANKYOUMAILEDATE  = db.Column(db.DateTime())
    ACCOUNTTYPE = db.Column(db.Integer, nullable=False)
    NAME = db.Column(db.String(200), nullable=False)
    KANA = db.Column(db.String(400), nullable=False)
    BIRTHDAY = db.Column(db.DateTime())
    SEX = db.Column(db.Integer, nullable=False)
    EMAIL= db.Column(db.String(300), nullable=False)
    POSSIBLERISKINV = db.Column(db.Integer, nullable=False)
    UPDATEDATE= db.Column(db.DateTime())
    UPDATECOUNT = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Entry %r>' % self.UENTRYNO

    def dict():
       return {'ENTRYDIV':None, 'ENTRYSOURCEDIV':None, 'PRIORITY':None, 'NAME':None, 'KANA':None, 'EMAIL':None,
               'BIRTHDAY':None, 'ENTRYDATE':None, 'ACCOUNTTYPE':None, 'STATUS':None, 'ENDDATE':None, 'THANKYOUMAILEDATE':None}

    def select_all():

        logger.debug("--- Entry select_all start ---")

        # select * from users
        entry_list = db.session.query(Entry).all()

        logger.debug("--- Entry select_all end   ---")

        return entry_list


    def select_status(status):

        logger.debug("--- Entry select_status start ---")

        if int(status) > 0:
            # select * from entrys
            entry_list = db.session.query(Entry).filter(Entry.STATUS == int(status), Entry.UENTRYDIV == 5).all()
        else:
            entry_list = db.session.query(Entry).filter(Entry.ENTRYDIV == 5).all()


        if entry_list == None:
            return []
        else:
            return entry_list

        logger.debug("--- Entry select_status end   ---")


    def insert(entry):

        logger.debug("--- Entry insert start ---")
        result = False

        try:

            now_date = datetime.now()
            #birthday_date = now_date - relativedelta.relativedelta(years=20)
            sql = "Select SEQ_ENTRYNO.NEXTVAL from dual"
            res = db.session.execute(sql)

            for r in res:
                seqno = r[0]

            logger.debug("--- Entry insert get seqno ---")

            record = Entry(
                ENTRYNO = seqno,
                ENTRYDIV = 5,
                ENTRYSOURCEDIV = 1,
                STATUS = 1,
                PRIORITY = 1,
                ENTRYDATE = now_date,
                ENDDATE = now_date,
                THANKYOUMAILEDATE = now_date,
                ACCOUNTTYPE = 1,
                NAME = entry['UNAME'],
                KANA = '',
                BIRTHDAY = now_date,
                SEX = 0,
                EMAIL = entry['UEMAIL'],
                POSSIBLERISKINV = 1,
                UPDATEDATE = now_date,
                UPDATECOUNT = 0,
                )

            logger.debug("--- Entry insert add record ---")
            # insert into entrys(name, address, tel, mail) values(...)
            db.session.add(record)
            db.session.commit()
            result = True
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- Entry insert exception message:{0}".format(e.with_traceback(tb)))
            db.session.rollback()

        logger.debug("--- Entry insert end   ---")
        return result


    def select_id(id):

        logger.debug("--- Entry select_id start ---")

        try:
            entry = db.session.query(Entry).filter(Entry.ENTRYNO==id).first()
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- Entry select_id exception message:{0}".format(e.with_traceback(tb)))

        logger.debug("--- Entry select_id end   ---")
        return entry

    def update(entry):

        logger.debug("--- Entry update start ---")
        result = False

        try:

            update_entry = db.session.query(Entry).filter(Entry.ENTRYNO==entry['ENTRYNO']).first()

            if entry['ENTRYDIV'] != None:
                update_entry.ENTRYDIV =  entry['ENTRYDIV']

            if entry['ENTRYSOURCEDIV'] != None:
                update_entry.UENTRYSOURCEDIV =  entry['ENTRYSOURCEDIV']

            if entry['STATUS'] != None:
                update_entry.USTATUS = entry['STATUS']

            if entry['PRIORITY'] != None:
                update_entry.USTATUS = entry['PRIORITY']

            if entry['ENTRYDATE'] != None:
                update_entry.UENTRYDATE = entry['ENTRYDATE']

            if entry['ENDDATE'] != None:
                update_entry.UENDDATE = entry['ENDDATE']

            if entry['THANKYOUMAILEDATE'] != None:
                update_entry.UTHANKYOUMAILEDATE = entry['THANKYOUMAILEDATE']

            if entry['ACCOUNTTYPE'] != None:
                update_entry.UACCOUNTTYPE = entry['ACCOUNTTYPE']

            if entry['NAME'] != None:
                update_entry.UNAME = entry['NAME']

            if entry['KANA'] != None:
                update_entry.UKANA = entry['KANA']

            if entry['BIRTHDAY'] != None:
                update_entry.UBIRTHDAY = entry['BIRTHDAY']

            if entry['SEX'] != None:
                update_entry.USEX = entry['SEX']

            if entry['EMAIL'] != None:
                update_entry.UEMAIL = entry['EMAIL']

            update_entry.UUPDATEDATE = datetime.now()

            logger.debug("--- Entry update update_entry ---")
            # insert into entrys(name, address, tel, mail) values(...)
            db.session.add(update_entry)
            db.session.commit()
            result = True
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- Entry update exception message:{0}".format(e.with_traceback(tb)))
            db.session.rollback()

        logger.debug("--- Entry update end   ---")
        return result


    def delete(id):

        logger.debug("--- Entry update start ---")
        result = False

        try:
            delete_entry = db.session.query(Entry).filter(Entry.ENTRYNO==id).first()

            logger.debug("--- Entry delete delete record ---")
            # insert into entrys(name, address, tel, mail) values(...)
            db.session.delete(delete_entry)
            db.session.commit()
            result = True
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- Entry delete exception message:{0}".format(e.with_traceback(tb)))
            db.session.rollback()

        logger.debug("--- Entry delete end   ---")
        return result
