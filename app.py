# importaciones de metodos para web scraping
#import webscraaping

# librerias para la creacion de la api
from flask import Flask
from flask import request
from flask import render_template
import chatboot as ctt
import json
import gmaiApi as gm
from chatbotaprend import chatbotApren
#import ssl
# *********************************Api***************************************

# inicialisando la plataforma de flast
app = Flask(__name__, template_folder='plantillas')
ca = chatbotApren()
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
    resul = ''
    y = json.loads(ctt.conversacionbot(emi))
    if (y['messeg'] == 'none'):
        y['messeg'] = str(ca.converc(emi))
        resul = json.dumps(y)
    else:
        resul = json.dumps(y)
    return resul


@app.route('/app/', methods=["GET", "POST"])
def prueba():
    return json.dumps({"mensaje": request.args.get('mesg'), "meseje2": request.args.get('mesg2')})


@app.route('/app/correo', methods=["GET"])
def enviarmesseg():
    gm.Mandandomesseg(request.args.get('messeg'),
                      request.args.get('nombre'), request.args.get('numero'), request.args.get('correo'))
    return json.dumps({"mensaje": "la peticion fue enviada con exito"})


@app.route('/app/avatar', methods=["GET"])
def renderavatar():
    return render_template('botsape.html')


if __name__ == '__main__':
    # mail.init_app(app)
    # if server_name and ':' in server_name:
    #    host, port = server_name.split(":")
    #    port = int(port)
    # else:
    #context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    #context.load_cert_chain('server.cer', 'server.key')
    ca.init()
    #port = 443
    #host = "192.168.0.7"
    #app.run(host=host, port=port, ssl_context=context)
    app.run()
