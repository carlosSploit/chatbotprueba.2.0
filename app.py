# importaciones de metodos para web scraping
#import webscraaping

# librerias para la creacion de la api
from flask import Flask
from flask import request
from flask_mail import Mail
import chatboot as ctt
import json
import gmaiApi as gm
# *********************************Api***************************************

app = Flask(__name__)  # inicialisando la plataforma de flast
# app.config.from_object(DevelopmentConfig)
#mail = Mail()
#mail.port = 587
#mail.username = 'arturo14212000@gmail.com'
#mail.password = '@123456789987654321'
#mail.use_ssl = False
#mail.use_tls = True
#mail.server = 'smtp.gmail.com'

ctt.initdatares()

#server_name = app.config['SERVER_NAME']


@app.route('/', methods=["GET", "POST"])
def messeg():
    return "la aplicacion esta funcionando muy bien"


@app.route('/app/chatbot/<emi>', methods=["GET", "POST"])
def messegchatbot(emi):
    # ctt.conversacionbot(emi)
    # conversacionBOT(emi)
    return ctt.conversacionbot(emi)


@app.route('/app/', methods=["GET", "POST"])
def prueba():
    return json.dumps({"mensaje": request.args.get('mesg'), "meseje2": request.args.get('mesg2')})


@app.route('/app/correo', methods=["GET"])
def enviarmesseg():
    gm.Mandandomesseg(request.args.get('messeg'),
                      request.args.get('nombre'), request.args.get('numero'), request.args.get('correo'))
    return json.dumps({"mensaje": "la peticion fue enviada con exito"})


if __name__ == '__main__':
    # mail.init_app(app)
    # if server_name and ':' in server_name:
    #    host, port = server_name.split(":")
    #    port = int(port)
    # else:
    #    port = 5000
    #    host = "localhost"
    #app.run(host=host, port=port)
    app.run()
