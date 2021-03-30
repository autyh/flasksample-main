from flask import Blueprint
from flask import render_template
from flask_wtf.csrf import CSRFProtect, CSRFError
import logging

app = Blueprint('errors', __name__)
logger = logging.getLogger(__name__)

@app.app_errorhandler(404)
def not_found_error(e):
    logger.info("not_found_error ocuured")
    return render_template('errors/404.html')


@app.app_errorhandler(400)
def bad_request_error(e):
    logger.info("bad_request_error ocuured")
    return render_template('errors/400.html')


@app.app_errorhandler(500)
def internal_server_error(e):
    logger.error("app_errorhandler ocuured")
    return render_template('errors/500.html')


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('errors/csrf_error.html')
