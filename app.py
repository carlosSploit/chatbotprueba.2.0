# importaciones de metodos para web scraping
#import webscraaping

# librerias para la creacion de la api
from flask import Flask
from flask import request
import chatboot as ctt
import json
import gmaiApi

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


@app.route('/app/chatbot/correo', methods=["GET", "POST"])
def enviarmesseg():
    if (request.method == 'POST'):

        Mandarmensaje(request.form['messeg'], request.form['nombre'],
                      request.form['numero'], request.form['correo'])

    return 'realizado'


if __name__ == '__main__':
    app.run()
