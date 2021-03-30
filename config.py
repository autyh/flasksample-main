import os
import socket

base_dir = os.path.dirname(os.path.realpath(__file__))

class BaseConfig(object):
    ENV = None
    Testing = False

class DevelopmentConfig(BaseConfig):
    host = socket.gethostname()
    localhost = socket.gethostbyname(host)

    ENV = 'development'
    # runsever Setting
    SERVER_IP=localhost
    SERVER_PORT=8000
    # Session Setting
    SECRET_KEY = 'your secret key'
    # Log Setting
    LOGFILE = "log/development.log"
    DEBUG = True
