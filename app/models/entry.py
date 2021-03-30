from datetime import datetime
from dateutil import relativedelta
from app.lib.db import db, ma
import logging
import sys

logger = logging.getLogger(__name__)


class  Entry(db.Model):
    __tablename__ = 'UT_ENTRYTEMP'

    UENTRYNO = db.Column(db.Integer, primary_key=True)
    UENTRYDIV = db.Column(db.Integer, nullable=False)
    UENTRYSOURCEDIV = db.Column(db.Integer, nullable=False)
    USTATUS = db.Column(db.Integer, nullable=False)
    UPRIORITY = db.Column(db.Integer, nullable=False)
    UENTRYDATE  = db.Column(db.DateTime())
    UENDDATE  = db.Column(db.DateTime())
    UTHANKYOUMAILEDATE  = db.Column(db.DateTime())
    UACCOUNTTYPE = db.Column(db.Integer, nullable=False)
    UNAME = db.Column(db.String(200), nullable=False)
    UKANA = db.Column(db.String(400), nullable=False)
    UBIRTHDAY = db.Column(db.DateTime())
    USEX = db.Column(db.Integer, nullable=False)
    UEMAIL= db.Column(db.String(300), nullable=False)
    UPOSSIBLERISKINV = db.Column(db.Integer, nullable=False)
    UUPDATEDATE= db.Column(db.DateTime())
    UUPDATECOUNT = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Entry %r>' % self.UENTRYNO

    def dict():
       return {'UENTRYDIV':None, 'UENTRYSOURCEDIV':None, 'UPRIORITY':None, 'UNAME':None, 'UKANA':None, 'UEMAIL':None,
               'UBIRTHDAY':None, 'UENTRYDATE':None, 'UACCOUNTTYPE':None, 'USTATUS':None, 'UENDDATE':None, 'UTHANKYOUMAILEDATE':None}

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
            entry_list = db.session.query(Entry).filter(Entry.USTATUS == int(status), Entry.UENTRYDIV == 5).all()
        else:
            entry_list = db.session.query(Entry).filter(Entry.UENTRYDIV == 5).all()


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
            sql = "Select USEQ_ENTRYNO.NEXTVAL from dual"
            res = db.session.execute(sql)

            for r in res:
                seqno = r[0]

            logger.debug("--- Entry insert get seqno ---")

            record = Entry(
                UENTRYNO = seqno,
                UENTRYDIV = 5,
                UENTRYSOURCEDIV = 1,
                USTATUS = 1,
                UPRIORITY = 1,
                UENTRYDATE = now_date,
                UENDDATE = now_date,
                UTHANKYOUMAILEDATE = now_date,
                UACCOUNTTYPE = 1,
                UNAME = entry['UNAME'],
                UKANA = '',
                UBIRTHDAY = now_date,
                USEX = 0,
                UEMAIL = entry['UEMAIL'],
                UPOSSIBLERISKINV = 1,
                UUPDATEDATE = now_date,
                UUPDATECOUNT = 0,
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
            entry = db.session.query(Entry).filter(Entry.UENTRYNO==id).first()
        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error("--- Entry select_id exception message:{0}".format(e.with_traceback(tb)))

        logger.debug("--- Entry select_id end   ---")
        return entry

    def update(entry):

        logger.debug("--- Entry update start ---")
        result = False

        try:

            update_entry = db.session.query(Entry).filter(Entry.UENTRYNO==entry['UENTRYNO']).first()

            if entry['UENTRYDIV'] != None:
                update_entry.UENTRYDIV =  entry['UENTRYDIV']

            if entry['UENTRYSOURCEDIV'] != None:
                update_entry.UENTRYSOURCEDIV =  entry['UENTRYSOURCEDIV']

            if entry['USTATUS'] != None:
                update_entry.USTATUS = entry['USTATUS']

            if entry['UPRIORITY'] != None:
                update_entry.USTATUS = entry['UPRIORITY']

            if entry['UENTRYDATE'] != None:
                update_entry.UENTRYDATE = entry['UENTRYDATE']

            if entry['UENDDATE'] != None:
                update_entry.UENDDATE = entry['UENDDATE']

            if entry['UTHANKYOUMAILEDATE'] != None:
                update_entry.UTHANKYOUMAILEDATE = entry['UTHANKYOUMAILEDATE']

            if entry['UACCOUNTTYPE'] != None:
                update_entry.UACCOUNTTYPE = entry['UACCOUNTTYPE']

            if entry['UNAME'] != None:
                update_entry.UNAME = entry['UNAME']

            if entry['UKANA'] != None:
                update_entry.UKANA = entry['UKANA']

            if entry['UBIRTHDAY'] != None:
                update_entry.UBIRTHDAY = entry['UBIRTHDAY']

            if entry['USEX'] != None:
                update_entry.USEX = entry['USEX']

            if entry['UEMAIL'] != None:
                update_entry.UEMAIL = entry['UEMAIL']

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
            delete_entry = db.session.query(Entry).filter(Entry.UENTRYNO==id).first()

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
