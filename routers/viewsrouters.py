from flask import Blueprint
from flask import render_template
# inicializamos el blueprint
viewrouters = Blueprint('viewrouters', __name__)


@viewrouters.route("/account")
def accountList():
    return "list of accounts"


@viewrouters.route('/app/avatar', methods=["GET"])
def renderavatar():
    return render_template('botsape.html')
