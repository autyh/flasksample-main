import requests
from flask import current_app

class WebRequest(object):

    codes = requests.codes

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('API_URL', ':memory:')

    def get(self, apiid, params, cookies):

        if cookies != None:
            return requests.get(current_app.config['API_URL'] + apiid, data=params, cookies=cookies)
        else:
            return requests.get(current_app.config['API_URL'] + apiid, data=params)

    def post(self, apiid, params, cookies):

        if cookies != None:
            res = requests.post(current_app.config['API_URL'] + apiid, data=params, cookies=cookies)
        else:
            res = requests.post(current_app.config['API_URL'] + apiid, data=params)

        return  res


web = WebRequest()

def init_web(app):
    web.init_app(app)
