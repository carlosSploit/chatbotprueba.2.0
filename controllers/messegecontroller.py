from controllers.palabraclabcontroller import classpalabraclabcontroller


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
