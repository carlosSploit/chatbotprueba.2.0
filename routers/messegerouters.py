
from flask import Blueprint, request
from controllers.messegecontroller import classmessegecontroller
import json

# inicializamos el blueprint
messegeapirouters = Blueprint('messegeapirouters', __name__)


@messegeapirouters.route('/app/mess/list/<code>', methods=["GET"])
def apimlist(code):
    control = classmessegecontroller({})
    resul = control.getlist(code)
    return json.dumps(resul)


@messegeapirouters.route('/app/mess/<code>', methods=["POST"])
def apiminsert(code):
    control = classmessegecontroller({})
    control.insert(code, request.json)
    objjson = {
        "resul": "se inserto correctamente"}
    return objjson


@messegeapirouters.route('/app/mess/<code>', methods=["PUT"])
def apimupdate(code):
    control = classmessegecontroller({})
    control.update(code, request.json)
    objjson = {
        "resul": "se actualizo correctamente"}
    return objjson


@messegeapirouters.route('/app/mess/<code>/<codemes>', methods=["DELETE"])
def apimdelect(code, codemes):
    control = classmessegecontroller({})
    control.delect(code, codemes)
    objjson = {
        "resul": "eliminado correctamente"}
    return json.dumps(objjson)


# @messegeapirouters.route('/app/user/', methods=["GET"])
# def apilist():
#     control = classusuaruarioscontroller({})
#     resul = control.getlist()
#     return json.dumps(resul)
