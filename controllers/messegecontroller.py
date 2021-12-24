from controllers.palabraclabcontroller import classpalabraclabcontroller
from models.messegemodels import classmessegemodels

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# datos de aprendisaje predefinico
# misaprendis = {
#     "id": 45464,
#     "input": "Que metodos se pueden utilizar para publicar",
#     "inputpalclab": {
#         "tipo": 1,
#         "palabras": [
#             "metodos", "publicar"
#         ]
#     },
#     "ouputs": "Tenemos el metodo particular o profecional"
# }


class classmessegecontroller:
    id = 4564
    imput = "Que metodos se pueden utilizar para publicar"
    ouputs = "Tenemos el metodo particular o profecional"
    inputpalclab = classpalabraclabcontroller({})
    models = classmessegemodels({})

    # costructor de mensajes
    def __init__(self, json):
        # Si existe la variable, inicializa la de la clase
        if("id" in json):
            self.id = json["id"]
        if("imput" in json):
            self.imput = json["imput"]
        if("ouputs" in json):
            self.ouputs = json["ouputs"]
        if("inputpalclab" in json):
            self.inputpalclab = classpalabraclabcontroller(
                json["inputpalclab"])

    # getterts

    def getid(self):
        return self.id

    def getimput(self):
        return self.imput

    def getouputs(self):
        return self.ouputs

    def getinputpalclab(self):
        return self.inputpalclab

    def getobjettojson(self):
        return {
            "id": self.getid(),
            "input": self.getimput(),
            "inputpalclab": self.getinputpalclab(),
            "ouputs": self.getouputs()
        }

    def getlist(self, code):
        return self.models.getlist(code)

    # insercion de un mensaje
    # teniendo en cuenta la lista de mensajes anterior

    def insert(self, code, jsonprar):
        self.models.insert(code, jsonprar)

    # actualizacion de un mensaje
    # teniendo en cuenta la lista de mensajes anterior

    def update(self, code, jsonprar):
        self.models.update(code, jsonprar)
        # se elimina el emnsaje pasando el code del chatbot y de codemeess de los mensajes

    def delect(self, code, codemess):
        self.models.delect(code, codemess)
        # listar datos

        # def getlist(self):
        #     #obj = messegemodels()
        #     lis_messge_controller = []
        #     for a in range(len(messegetuplas)):
        #         lis_messge_controller.append(
        #             classmessegecontroller(messegetuplas[a]))
        #     return lis_messge_controller

    pass


# obj = classmessegecontroller({
#     "id": 45464,
#     "input": "Que metodos se pueden utilizar para publicar",
#     "inputpalclab": {
#         "tipo": 1,
#         "palabras": [
#             "metodos", "publicar"
#         ]
#     },
#     "ouputs": "Tenemos el metodo particular o profecional"
# })

# print(len(obj.getlist()))
