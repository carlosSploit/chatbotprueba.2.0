# importaciones de metodos para web scraping
#import webscraaping

# librerias para la creacion de la api
from flask import Flask
from flask import request
import json

# *********************************Api***************************************


app = Flask(__name__)  # inicialisando la plataforma de flast


@app.route('/', methods=["GET", "POST"])
def messeg():
    return "la aplicacion esta funcionando muy bien"


@app.route('/app/chatbot/<emi>', methods=["GET", "POST"])
def messegchatbot(emi):
    # conversacionBOT(emi)
    return "Tedaria una respuesnta pero aun no estoy conectado a la data"


app.run(debug=True)
