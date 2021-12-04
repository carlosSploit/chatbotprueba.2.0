# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Considerar que en cada palabra, abra una palabra antes y una palabra despues
# de la palabra bace
# #

#     "inputpalclab": {
#         "tipo": 1,
#         "palabras": [
#             "metodos", "publicar"
#         ]
#     },

class classpalabraclabcontroller:
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

    def getobjettojson(self):
        return {
            "id": self.getid(),
            "tipo": self.gettipo(),
            "palabras": self.getpalabra(),
        }

    pass
