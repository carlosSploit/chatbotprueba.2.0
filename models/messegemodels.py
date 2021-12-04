#from controllers.messegecontroller import classmessegecontroller
import json
import uuid
from datetime import datetime
#from ..models.messegeiten import messegemodels
# tipo stade palabras clabe
# 1 -> secuencia  -> metodos - publicar
# 2 -> conbinaciones -> metodos - pubicar / publicar - metodo
# 3 -> no-dependientes -> metodos / publicar
# donde:
# - : contenido entre palabras
# / : otra frace
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class classusuariosmodels:
    conexion = 0

    def __init__(self, json):
        self.conexion = 0

    def getlist(self):
        f = open("data/datasetjson.json", "r")
        c = f.read()
        js = json.loads(c)
        f.close()
        return js
    # insercion de un nuevo usuario
    # retorna el nuevo codigo del chatbot

    def create(self):
        auxchatbot = self.getlist()
        objinsert = {
            "userchatbot": 454646,
            "fechecreate": "01-11-2021",
            "itemmessege": []
        }
        objinsert["userchatbot"] = str(uuid.uuid4())
        objinsert["fechecreate"] = datetime.today().strftime('%Y-%m-%d')
        auxchatbot.append(objinsert)
        # metodo de remplao y imprecion de la data
        jsstring = json.dumps(auxchatbot, indent=4)
        # guardamos en archivo
        fa = open("data/datasetjson.json", "w")
        fa.write(jsstring)
        fa.close()

    # lee el chatbot segun su codigo
    def read(self, code):
        usser = self.getlist()
        for a in range(len(usser)):
            if usser[a]["userchatbot"] == code:
                return usser[a]
        return {}
    pass

    # implementar actualizacion del chatbot segun su codigo y el contenido
    def update(self, code, jsonax):
        # lista de usuarios
        usser = self.getlist()
        listaux = []
        for a in range(len(usser)):
            if not (usser[a]["userchatbot"] == code):
                # intercambia el contenido, con el nuebo contenido
                listaux.append(usser[a])
        listaux.append(jsonax)  # se inserta el nuevo json
        # trasforma de json a string
        jsstring = json.dumps(listaux, indent=4)
        print(jsstring)
        # guardamos en archivo
        fa = open("data/datasetjson.json", "w")
        fa.write(jsstring)
        fa.close()
    pass


class classmessegemodels:
    conexion = 0
    objcontrol = classusuariosmodels({})

    def __init__(self, json):
        self.conexion = 0
    # listar mensajes

    def getlist(self, code):
        f = open("data/datasetjson.json", "r")
        c = f.read()
        js = json.loads(c)
        for a in range(len(js)):
            if js[a]["userchatbot"] == code:
                return js[a]["itemmessege"]
        return []
    # insercion de un mensaje
    # teniendo en cuenta la lista de mensajes anterior

    def insert(self, code, jsonprar):
        objusuar = classusuariosmodels({})
        auxchatbot = objusuar.read(code)
        # se captura los datos
        listmesse = auxchatbot["itemmessege"]
        # se inserta el nuebo mensaje
        jsonprar["id"] = len(listmesse) + 1
        jsonprar["inputpalclab"]["idmessege"] = len(listmesse) + 1
        listmesse.append(jsonprar)
        # se remplaza la lista anteriorde mensajes con la nueva
        auxchatbot["itemmessege"] = listmesse
        # INSERTAR LO INGRESADO EN LA LISTA GENERAL E EDITARLO
        listuser = objusuar.getlist()
        listgeneric = []
        for a in range(len(listuser)):
            if not(listuser[a]["userchatbot"] == code):
                listgeneric.append(listuser[a])
        listgeneric.append(auxchatbot)
        # metodo de remplao y imprecion de la data
        jsstring = json.dumps(listgeneric, indent=4)
        # guardamos en archivo
        fa = open("data/datasetjson.json", "w")
        fa.write(jsstring)
        fa.close
    pass


obj = classusuariosmodels({})
print(obj.getlist())
# obj.create()
# obj.getlist()
obj.update("73290d7a-445d-442e-8038-cc2cfe3b2510", {
    "userchatbot": "73290d7a-445d-442e-8038-cc2cfe3b2510",
    "fechecreate": "2021-12-03",
    "itemmessege": [
        {
            "id": 3,
            "input": "Quiero una rica y sabrosa pinga que sea muy venosa",
            "inputpalclab": {
                "idmessege": 3,
                "tipo": 1,
                "palabras": [
                    "pinga",
                    "venosa"
                ]
            },
            "ouputs": "Si te gusta aqui tengo una entre las piernas"
        },
        {
            "id": 1,
            "input": "Quiero una rica y sabrosa pinga que sea muy venosa",
            "inputpalclab": {
                "idmessege": 3,
                "tipo": 1,
                "palabras": [
                    "pinga",
                    "venosa"
                ]
            },
            "ouputs": "Si te gusta aqui tengo una entre las piernas"
        },
        {
            "id": 3,
            "input": "Quiero una rica y sabrosa pinga que sea muy venosa",
            "inputpalclab": {
                "idmessege": 3,
                "tipo": 1,
                "palabras": [
                    "pinga",
                    "venosa"
                ]
            },
            "ouputs": "Si te gusta aqui tengo una entre las piernas"
        }
    ]
})
# print(obj.getlist())
# obj.insert(454646, {'id': 0, 'input': 'Quiero una rica y sabrosa pinga que sea muy venosa', 'inputpalclab': {
#     'idmessege': 0, 'tipo': 1, 'palabras': ['pinga', 'venosa']}, 'ouputs': 'Si te gusta aqui tengo una entre las piernas'})
# print(obj.getlist())
