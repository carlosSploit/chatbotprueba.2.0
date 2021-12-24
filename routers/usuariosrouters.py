
from flask import Blueprint
from controllers.usuariocontroller import classusuaruarioscontroller
import json

# inicializamos el blueprint
usuariosapirouters = Blueprint('usuariosapirouters', __name__)


@usuariosapirouters.route('/app/user', methods=["GET"])
def apiulist():
    control = classusuaruarioscontroller({})
    resul = control.getlist()
    return json.dumps(resul)


@usuariosapirouters.route('/app/user/<code>', methods=["GET"])
def apiuread(code):
    control = classusuaruarioscontroller({})
    resul = control.read(code)
    return json.dumps(resul)


@usuariosapirouters.route('/app/user/create', methods=["GET"])
def apiucreate():
    control = classusuaruarioscontroller({})
    resul = control.create()
    objjson = {
        "codechatbotapi": resul}
    return json.dumps(objjson)


@usuariosapirouters.route('/app/user/<code>', methods=["DELETE"])
def apiudelect(code):
    control = classusuaruarioscontroller({})
    control.delect(code)
    objjson = {
        "resul": "eliminado correctamente"}
    return json.dumps(objjson)


# @usuariosapirouters.route('/app/user/', methods=["GET"])
# def apilist():
#     control = classusuaruarioscontroller({})
#     resul = control.getlist()
#     return json.dumps(resul)
