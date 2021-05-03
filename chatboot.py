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
            r"(.*) mas favoritos (.*)|(.*) mas comprados (.*)|(.*) mas (.*) comprados (.*)|(.*) mas (.*) comprados|(.*) mas comprados",
            ["Los mas comprados son estos inmuebles", ]
        ],
        [
            r"(.*) mas recomendado (.*)|(.*) recomiendas (.*)|(.*) recomendarme (.*)|(.*) recomendarme",
            ["Te recomiendo estos inmuebles", ]
        ],
        [
            r"(.*) comprar (.*)|(.*) comprando (.*)",
            ["Tenemos algunos de estos inmuebles de compra", ]
        ],
        [
            r"(.*) Cual (.*) libro favorito (.*)",
            ["No puedo leer", ]
        ],
        [
            r"(.*) alquiler (.*)|(.*) alquilar (.*)|(.*) alquileres (.*)",
            ["Tenemos algunos de estos inmuebles de alquiler", ]
        ],
        [
            r"hola|hey|buenas",
            ["Hola. ¿Cuál es tu pregunta?", "Que tal", ]
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
            ["No lo se soy un bot, y no entiendo los sentimientos",
                "Estoy bien, ¿y tú?", "También estoy bien."]
        ],
        [
            r"(.*)quien(.*)creado(.*)|(.*)quien(.*)creo(.*)",
            ["Fui creado por los estudiantes de la univercidad cesar vallejo", ]
        ],
        [
            r"finalizar|adios",
            ["Chao", "Fue bueno hablar contigo"]
        ],
        [
            r"(.*)contactarme(.*)|(.*)comunicarme(.*)ustedes(.*)",
            ["Central de ventas:   +51 984129585 \nHorario:   Lunes a Viernes de 09:00 am a 06:00 pm"]
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

    elif (meseg == 'Tenemos algunos de estos inmuebles de alquiler'):

        rejson = wb.inmuebleALQUILER(messeg)
        resul = json.loads(rejson)

        if (resul['messeg'] == 'none'):
            resul['messeg'] = 'Tenemos algunos de estos inmuebles'

    elif (meseg == 'Tenemos algunos de estos inmuebles de compra'):

        rejson = wb.inmuebleCOMPRA(messeg)
        resul = json.loads(rejson)

        if (resul['messeg'] == 'none'):
            resul['messeg'] = 'Tenemos algunos de estos inmuebles'

    elif (meseg == 'Te recomiendo estos inmuebles'):

        rejson = wb.inmuebleREC_FAV("R")
        resul = json.loads(rejson)
        resul['messeg'] = 'Te recomiendo estos inmuebles'

    elif (meseg == 'Los mas comprados son estos inmuebles'):

        rejson = wb.inmuebleREC_FAV("F")
        resul = json.loads(rejson)
        resul['messeg'] = 'Los mas comprados son estos inmuebles'

    else:
        resul['messeg'] = meseg

    return json.dumps(resul)
