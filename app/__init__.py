from flask import Flask
from app.lib.mail import init_mail
from app.lib.db import init_db
from app.views import error, index, sample
import logging.handlers

def create_app(config_file):

    logging.info("start create app")

    app = Flask(__name__)
    app.config.from_object(config_file)

    # log output
    #fh = logging.FileHandler(app.config['LOGFILE'])
    fh = logging.handlers.RotatingFileHandler(app.config['LOGFILE'], maxBytes=10000000, backupCount=30)
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)

    init_mail(app)
    init_db(app)

    # add views
    app.register_blueprint(error.app)
    app.register_blueprint(index.app)
    app.register_blueprint(sample.app)

    return app
