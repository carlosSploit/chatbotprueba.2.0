# importaciones de metodos para web scraping
#import webscraaping

# librerias para la creacion de la api
from flask import Flask
# imports routers -------------------------------
from routers.chatbotrouters import chatbotrouters
from routers.viewsrouters import viewrouters
from routers.apigmailrouters import apirestgmail
from routers.usuariosrouters import usuariosapirouters
from routers.messegerouters import messegeapirouters
#################################################
import chatbotaprend as ca
import ssl
# *********************************Api***************************************

# inicialisando la plataforma de flast
app = Flask(__name__, template_folder='plantillas')
ca.init()

#server_name = app.config['SERVER_NAME']


@app.route('/', methods=["GET", "POST"])
def messeg():
    return "la aplicacion esta funcionando muy bien"


# routeres --------------------------------------------
#app.register_blueprint(chatbotrouters, url_prefix='/accounts')
app.register_blueprint(messegeapirouters)
app.register_blueprint(usuariosapirouters)
app.register_blueprint(chatbotrouters)
app.register_blueprint(viewrouters)
app.register_blueprint(apirestgmail)

if __name__ == '__main__':
    # mail.init_app(app)
    # if server_name and ':' in server_name:
    #    host, port = server_name.split(":")
    #    port = int(port)
    # else:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('server.cer', 'server.key')
    port = 443
    host = "192.168.0.7"
    # app.run(host=host, port=port, ssl_context=context)
    app.run(host=host, port=port)
    app.run()
