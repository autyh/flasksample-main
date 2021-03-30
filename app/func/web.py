from app.lib.web import web
import logging

logger = logging.getLogger(__name__)

#APIを叩く
def getapires(uhapi, params):
    res = requests.post(url, params=params)
    return res

#ディクショナリにレスポンスを入れる
def mkdictfromres(res_text, dict):
    root = ET.fromstring(res_text)
    for child in root:
        for ch in child:
            dict[ch.tag] = ch.text
    return

#APIを叩き、セッションにデータを格納し、ステータスコードを返す
def getstatus(uhapi, params):
    res = getapires(uhapi, params)
    mkdictfromres(res.text, session)

    status = int(session['STATUS'])

    return status
