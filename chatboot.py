# libreria para la creacion de la ia
from nltk.chat.util import Chat, reflections
import webscraaping as wb
import json

# datos para el entrenamiento del chatbot
mis_reflexions = {}
pares = []


def initdatares():

    global mis_reflexions
    global pares

    mis_reflexions = {
        "ir": "fui",
        "hola": "hey",
        "caido": "cayo",
        "cayo": "caido"
    }

    pares = [
        # [
        #    r"(.*) caido (.*) hosting (.*)|(.*) cayo (.*) hosting (.*)",
        #    ["Sentimos ese fallo, para reiniciarlo, entra en CPANEL y selecciona reiniciar", ]
        # ],
        # [
        #    r"(.*) cuando (.*) pagar (.*) factura (.*)",
        #    ["Hay que pagarla el dia 15 de cada mes por tarjeta de crédito", ]
        # ],
        # [
        #    r"(.*) ampliar el servicio",
        #    ["Para ampliar el servicio, contacta con facturacion", ]
        # ],
        [
            r"(.*) alquiler (.*)|(.*) alquilar (.*)|(.*) alquileres (.*)",
            ["Tenemos algunos de estos inmuebles de alquiler", ]
        ],
        [
            r"hola|hey|buenas",
            ["Hola", "Que tal", ]
        ],
        [
            r"(.*)publicar(.*)inmueble(.*)|(.*)publica(.*)inmueble(.*)",
            ["Publica tus anuncios totalmente gratis e indefinidamente en Casas360. Si tienes más de 100 anuncios, podemos ayudarte a importarlos masivamente. Ingrese aqui: https://casas360.pe/p/publica-tu-inmueble", ]
        ],
        [
            r"(.*)redes sociales(.*)|(.*)redes(.*)",
            ["faceboo: https://fb.me/Casas360.org"]
        ],
        [
            r"(.*)estas(.*)|(.*)sientes(.*)|(.*)que tal(.*)",
            ["No lo se soy un bot, y no entiendo los sentimientos"]
        ],
        [
            r"(.*)quien(.*)creado(.*)|(.*)quien(.*)creo(.*)",
            ["Fui creado hoy", ]
        ],
        [
            r"finalizar|adios",
            ["Chao", "Fue bueno hablar contigo"]
        ],
    ]

# metodo para sacer un resultado del chatbot


def conversacionbot(messeg):
    chat = Chat(pares, mis_reflexions)
    # chat.converse()
    # Ingresar los datos para que de una respuesta el bot segun lo aprendido
    respont = chat.respond(str(messeg))
    meseg = str(respont)
    resul = {}  # captara el mensaje en forma de json
    rejson = ''  # captara el mensaje en forma de string o cadena

    if ((meseg == 'None') or (meseg == '') or (meseg == None)):

        resul['messeg'] = 'Lo siento no entiendo, quisas sea porque no fui programada para tener conversaciones, solo ayudar.'
        print('Lo siento no entiendo, quisas sea porque no fui programada para tener conversaciones, solo ayudar.')

    elif (meseg == 'Tenemos algunos de estos inmuebles de alquiler'):

        rejson = wb.inmuebleALQUILER()
        resul = json.loads(rejson)
        resul['messeg'] = 'Tenemos algunos de estos inmuebles'
        print('Tenemos algunos de estos inmuebles')

    else:

        resul['messeg'] = meseg
        print(meseg)
    # return json.dumps(resul)


while (True):
    cont = input("yo: ")
    conversacionbot(cont)
