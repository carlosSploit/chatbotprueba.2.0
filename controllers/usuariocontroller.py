# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# objeto usuario chatbot, sirbe para tener un control
# de los mensajes teniendo en cuenta el chatbot en si
# [
#     {
#         "userchatbot": 454646, -> codigo del api de chatbot
#         "fechecreate": "01-11-2021", -> fecha de la creacion del nodo
#         "itemmessege": messegetuplas -> mesajes que presenta el chatbot
#     }
# ]
from controllers.messegecontroller import classmessegecontroller
from models.messegemodels import classusuariosmodels


class classusuaruarioscontroller:
    userchatbot = 4564
    fechecreate = "01-11-2021"
    itemmessege = []

    # costructor de mensajes
    def __init__(self, json):
        # Si existe la variable, inicializa la de la clase
        if("userchatbot" in json):
            self.userchatbot = json["userchatbot"]
        if("fechecreate" in json):
            self.fechecreate = json["fechecreate"]
        # se recorren todos los mensajes y ejecuta la funcion
        if("itemmessege" in json):
            for item in range(len(json["itemmessege"])):
                self.itemmessege.append(
                    classmessegecontroller(json["itemmessege"][item]))

    # getterts

    def getuserchatbot(self):
        return self.userchatbot

    def getfechecreate(self):
        return self.fechecreate

    def getitemmessege(self):
        return self.itemmessege

    def getread(self, code):
        aux = classusuaruarioscontroller({})
        auxmodel = classusuariosmodels({})
        usser = auxmodel.read(code)
        aux = classusuaruarioscontroller(usser)
        return aux

    pass
