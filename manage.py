import logging
import os
from app import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager, Server


config = {
    'development': 'config.DevelopmentConfig',
}

env = os.environ.get('FLASK_ENV', 'development')
app = create_app(config[env])
logger = logging.getLogger(__name__)

manager = Manager(app)
#manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host=app.config['SERVER_IP'], port=os.environ.get('FLASK_RUN_PORT', app.config['SERVER_PORT'])))

logger.info("start run server")

if __name__ == "__main__":
    manager.run()
