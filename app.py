# importaciones de metodos para web scraping
#import webscraaping

# librerias para la creacion de la api
from flask import Flask
from flask import request
import chatboot as ctt
import json
import gmaiApi as gm

# *********************************Api***************************************


app = Flask(__name__)  # inicialisando la plataforma de flast
ctt.initdatares()


@app.route('/', methods=["GET", "POST"])
def messeg():
    return "la aplicacion esta funcionando muy bien"


@app.route('/app/chatbot/<emi>', methods=["GET", "POST"])
def messegchatbot(emi):
    # ctt.conversacionbot(emi)
    # conversacionBOT(emi)
    return ctt.conversacionbot(emi)


@app.route('/app/correo', methods=["POST"])
def enviarmesseg():
    if (request.method == 'POST'):
        gm.Mandandomesseg('quiero comerme un culo de locos',
                          'carlos arturo guerrero castillo', '969280255', 'arturo14212000@gmail.com')

    return json.dumps({"mensaje": "la peticion fue enviada con exito"})


if __name__ == '__main__':
    app.run()
