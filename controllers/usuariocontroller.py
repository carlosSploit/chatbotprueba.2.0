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
    models = classusuariosmodels({})

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

    # def getread(self, code):
    #     aux = classusuaruarioscontroller({})
    #     auxmodel = classusuariosmodels({})
    #     usser = auxmodel.read(code)
    #     aux = classusuaruarioscontroller(usser)
    #     return aux

    def getlist(self):
        return self.models.getlist()
    # insercion de un nuevo usuario
    # se tendra de ingresar un nombre
    # retorna el nuevo codigo del chatbot

    def create(self):
        return self.models.create()

    # lee el chatbot segun su codigo
    def read(self, code):
        return self.models.read(code)

    # implementar actualizacion del chatbot segun su codigo y el contenido
    def update(self, code, jsonax):
        self.models.update(code, jsonax)

    # eliminar metodo con codigo del chatbot
    def delect(self, code):
        self.models.delect(code)
    pass
