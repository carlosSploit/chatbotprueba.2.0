from models.messegeiten import messegemodels

# tipo stade palabras clabe
# 1 -> secuencia  -> metodos - publicar
# 2 -> conbinaciones -> metodos - pubicar / publicar - metodo
# 3 -> no-dependientes -> metodos / publicar
# donde:
# - : contenido entre palabras
# / : otra frace
# nota:
# Considerar que en cada palabra, abra una palabra antes y una palabra despues
# de la palabra bace
# #

#     "inputpalclab": {
#         "tipo": 1,
#         "palabras": [
#             "metodos", "publicar"
#         ]
#     },


class palabraclabcontroller:
    id = 4564
    tipo = 1
    palabras = []

    # costructor de mensajes
    def __init__(self, json):
        # Si existe la variable, inicializa la de la clase
        if("id" in json):
            self.id = json["id"]
        if("tipo" in json):
            self.tipo = json["tipo"]
        if("palabras" in json):
            self.palabras = json["palabras"]

    # getterts

    def getid(self):
        return self.id

    def gettipo(self):
        return self.tipo

    def getpalabra(self):
        return self.palabras

    pass

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


class messegecontroller:
    id = 4564
    imput = "Que metodos se pueden utilizar para publicar"
    ouputs = "Tenemos el metodo particular o profecional"
    inputpalclab = palabraclabcontroller({})

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
            self.inputpalclab = palabraclabcontroller(json["inputpalclab"])

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

    @staticmethod
    def getlist(self):
        obj = messegemodels()
        return obj.getlist()

    pass


obj = messegecontroller({
    "id": 45464,
    "input": "Que metodos se pueden utilizar para publicar",
    "inputpalclab": {
        "tipo": 1,
        "palabras": [
            "metodos", "publicar"
        ]
    },
    "ouputs": "Tenemos el metodo particular o profecional"
})

print(obj.getlist())
