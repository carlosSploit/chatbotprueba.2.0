from flask import Blueprint
import json
import chatboot as ctt

# inicializamos el blueprint
chatbotrouters = Blueprint('chatbotrouters', __name__)


@chatbotrouters.route("/app/chatbot/")
def accountList():
    return "list of accounts"


@chatbotrouters.route('/app/chatbot/<code>/<emi>', methods=["GET", "POST"])
def messegchatbot(code, emi):
    # ctt.conversacionbot(emi)
    # conversacionBOT(emi)
    # ctt.initdatares(code)
    ctt.initdatares(code)
    resul = ''
    y = json.loads(ctt.conversacionbot(emi))
    # if (y['messeg'] == 'none'):
    #     y['messeg'] = str(ca.converc(emi))
    #     resul = json.dumps(y)
    # else:
    #     resul = json.dumps(y)
    # return resul
    return json.dumps(y)
    # return json.dumps({"codigo": code, "meseje": emi})
