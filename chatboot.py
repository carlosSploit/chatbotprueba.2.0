# libreria para la creacion de la ia
from nltk.chat.util import Chat, reflections
import webscraaping as wb
import json
import copy
from controllers.messegecontroller import messegecontroller

# datos para el entrenamiento del chatbot
mis_reflexions = {}
pares = []
#obj = messegecontroller({})


def initdatares():

    global mis_reflexions
    global pares

    mis_reflexions = {
        "ir": "fui",
        "hola": "hey",
        "caido": "cayo",
        "cayo": "caido"
    }

    # tipo stade palabras clabe
    # 1 -> secuencia  -> metodos - publicar
    # 2 -> conbinaciones -> metodos - pubicar / publicar - metodo
    # 3 -> no-dependientes -> metodos / publicar
    # donde:
    # - : contenido entre palabras
    # / : otra frace
    # nota:
    # Considerar que en cada palabra, abra una palabra antes y una palabra despues
    # de la palabra bace
    # #
    # datos de aprendisaje predefinico
    # misaprendis = {
    #     "id": 45464,
    #     "input": "Que metodos se pueden utilizar para publicar",
    #     "inputpalclab": {
    #         "tipo": 1,
    #         "palabras": [
    #             "metodos", "publicar"
    #         ]
    #     },
    #     "ouputs": "Tenemos el metodo particular o profecional"
    # }

    pares = [
        messegecontroller({
            "id": 45464,
            "input": "Que metodos se pueden utilizar para publicar",
            "inputpalclab": {
                "tipo": 1,
                "palabras": [
                    "metodos", "publicar"
                ]
            },
            "ouputs": "Tenemos el metodo particular o profecional"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 2,
                "palabras": [
                    "publicar", "particular"
                ]
            },
            "ouputs": "Propietarios que desean vender o alquilar un inmueble. Mas informacion aqui : https://gojom.pe/p/publica-tu-inmueble-particular"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 2,
                "palabras": [
                    "publicar", "profecional"
                ]
            },
            "ouputs": "Inmobiliarias, corredores, agentes. Mas informacion aqui : https://gojom.pe/p/publica-tu-inmueble-profesional"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "problema", "duda", "consula"
                ]
            },
            "ouputs": "Rellena el siguiente formulario"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "mas favoritos", "mas comprados",
                ]
            },
            "ouputs": "Rellena el siguiente formulario"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "mas recomendado", "recomiendas", "recomendarme", "recomendarme"
                ]
            },
            "ouputs": "Te recomiento estos inmuebles"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "comprar", "comprando"
                ]
            },
            "ouputs": "Tenemos algunos de estos inmuebles de compra"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 1,
                "palabras": [
                    "Cual", "libro favorito"
                ]
            },
            "ouputs": "No puedo lee"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "alquiler", "alquilar", "alquileres"
                ]
            },
            "ouputs": "Tenemos algunos de estos inmuebles de alquiler"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "hola", "hey", "buenas"
                ]
            },
            "ouputs": "Hola. ¿Cuál es tu pregunta?"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 2,
                "palabras": [
                    "publicar", "inmueble"
                ]
            },
            "ouputs": "Publica tus anuncios totalmente gratis e indefinidamente en Casas360. Si tienes más de 100 anuncios, podemos ayudarte a importarlos masivamente. Ingrese aqui: https://casas360.pe/p/publica-tu-inmueble"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "redes sociale", "redes"
                ]
            },
            "ouputs": "faceboo: https://www.facebook.com/GoJom.pe"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "pagina empresarial", "pagina"
                ]
            },
            "ouputs": "empresa: https://gojom.pe/"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "estas", "sientes", "que tal"
                ]
            },
            "ouputs": "No lo se soy un bot, y no entiendo los sentimientos"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 2,
                "palabras": [
                    "quien", "creado", "creo"
                ]
            },
            "ouputs": "No lo se soy un bot, y no entiendo los sentimientos"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 3,
                "palabras": [
                    "finalizar", "adios"
                ]
            },
            "ouputs": "Fue bueno hablar contigo"
        }),
        messegecontroller({
            "id": 45464,
            "input": "default",
            "inputpalclab": {
                "tipo": 2,
                "palabras": [
                    "finalizar", "adios"
                ]
            },
            "ouputs": "Fue bueno hablar contigo"
        }),
    ]

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 1 -> secuencia  -> metodos - publicar
# messege : mensaje ingresado
# list_pal : lista de palabras clabe
# index : indice donde empieza la busqueda
# contac : contador de palabras - index list palabra
# resul : respuesta esperada en memoria


def parse_secuencia(messege, list_pal, contac, index, resul):
    list_mes = messege.split(" ")
    if (contac == len(list_pal)):
        # print("Entro we")
        resul = 1
    else:
        if (index < len(list_mes)):
            # print("contac : {}".format(contac),
            #       "list_pal len : {}".format(len(list_pal)), "palabra : {}", list_mes[index])
            # comprueba la primera palabra
            if(list_pal[contac] == list_mes[index]):
                contac = contac + 1

            if ((len(list_mes) - 1) == index and contac == 0):
                resul = 0
            index = index + 1
            # en caso que se sume el contador se llamara al metodo, pero
            # este retornara siempre algo
            resul = parse_secuencia(messege, list_pal, contac, index, resul)
    return resul


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 2 -> conbinaciones -> metodos - pubicar / publicar - metodo

# genera la convinaciones de palabras en un array


def combinations(lisconbinations, target, data):
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        if(len(new_target) != 1):
            lisconbinations.append(new_target)
        # print(new_target)
        combinations(lisconbinations,
                     new_target,
                     new_data)
    return invert_itens_list(lisconbinations)

# Invierte las conbinaciones del anterior array para aumentar las posibilidades
# considerando iten por iten [["carlos","arturo"]] => [["arturo","carlos"]]


def invert_itens_list(lisconbinations):
    lista_Aux = []
    for a in range(len(lisconbinations)):
        lista_Aux.append(lisconbinations[a])
        lista_Aux.append(inver_array(lisconbinations[a]))
    return lista_Aux


def inver_array(list_iten):
    lista_Aux = []
    for a in range(len(list_iten)):
        lista_Aux.append(list_iten[(len(list_iten) - 1)-a])
    return lista_Aux

# generar combinaciones de palabras y parciarlos: (.*) casa (.*) papa (.*) | (.*) casa (.*) papa (.*)


def parse_conbinaciones(nessege, list_pal):
    resul = 0
    # lista de combinaciones con palabras
    list_conbi_pal = combinations([], [], list_pal)
    for a in range(len(list_conbi_pal)):
        if (resul != 1):
            resul = parse_secuencia(nessege, list_conbi_pal[a], 0, 0, 0)
            # print(resul, ": resultado combinacion")
        # if((len(list_conbi_pal) - 1) != a):
        #     cadena = cadena + "|"
    return resul
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 3 -> no-dependientes -> metodos / publicar

# compara una lista de palabras con otra y compara si existe


def parse_no_dependientes(messege, list_pal):
    resul = 0
    list_mess_pal = messege.split(" ")
    for a in range(len(list_mess_pal)):
        if list_mess_pal[a] in list_pal:
            resul = 1
    return resul
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# generador de inputs


def analitic_datos_meeseg(messege, json):
    itemanalisis = {
        "analizado": 0,
        "resultado": ""
    }
    # tipo de respueta de analisis
    # palabras cables
    lis_pal_clabe = (json.getinputpalclab().getpalabra())
    # tipo de combinacion de palabras clabe
    idinttipo = (json.getinputpalclab().gettipo())

    if(idinttipo == 1):
        resul = parse_secuencia(messege,
                                lis_pal_clabe, 0, 0, 0)
        itemanalisis["analizado"] = resul
        itemanalisis["resultado"] = json.getouputs()
    if(idinttipo == 2):
        resul = parse_conbinaciones(messege,
                                    lis_pal_clabe)
        itemanalisis["analizado"] = resul
        itemanalisis["resultado"] = json.getouputs()

    if(idinttipo == 3):
        resul = parse_no_dependientes(messege,
                                      lis_pal_clabe)
        itemanalisis["analizado"] = resul
        itemanalisis["resultado"] = json.getouputs()
    return itemanalisis
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# recorre todas las palabras clave y verifica
# la cantidad de porcentaje que se tiene, segun el filtro
# messege : mensaje esperado
# listanalitic : lista de analisis realizado por cantidad
# json : el iten a analizar
# index : index que se encuentra la tupla a analizar


def conveter_list(messege, listanalitic, index):

    # agrega el promedio resultante
    # listanalitic.add(jsonres)
    # se envia a otro json a analisar con el mensaje
    if (len(pares) != index):
        # captura el json resultante y comprueba la probabilidad
        jsonres = analitic_datos_meeseg(messege, pares[index])
        listanalitic.append(jsonres)
        conveter_list(messege, listanalitic, index+1)
    return listanalitic


def converce(messege):
    # comprovacion de primer filtro
    # conpara si el mensaje es igual a uno de los inputs
    for a in range(len(pares)):
        if (pares[a].getimput() == messege):
            return pares[a].getouputs()

    # analiza todas las palabras clabes y comprueba el resultado
    lista_dat_palclabes = conveter_list(messege, [], 0)
    for a in range(len(lista_dat_palclabes)):
        if(lista_dat_palclabes[a]["analizado"] != 0):
            return lista_dat_palclabes[a]["resultado"]

# metodo para sacer un resultado del chatbot


# def conversacionbot(messeg):
    # chat = Chat(conveter_list(pares), mis_reflexions)
    # # chat.converse()
    # # Ingresar los datos para que de una respuesta el bot segun lo aprendido
    # respont = chat.respond(str(messeg))
    # meseg = str(respont)
    # resul = {}  # captara el mensaje en forma de json
    # rejson = ''  # captara el mensaje en forma de string o cadena

    # if ((meseg == 'None') or (meseg == '') or (meseg == None)):

    #     resul['messeg'] = 'none'

    # elif (meseg == 'Tenemos algunos de estos inmuebles de alquiler'):

    #     rejson = wb.inmuebleALQUILER(messeg)
    #     resul = json.loads(rejson)

    #     if (resul['messeg'] == 'none'):
    #         resul['messeg'] = 'Tenemos algunos de estos inmuebles'

    # elif (meseg == 'Tenemos algunos de estos inmuebles de compra'):

    #     rejson = wb.inmuebleCOMPRA(messeg)
    #     resul = json.loads(rejson)

    #     if (resul['messeg'] == 'none'):
    #         resul['messeg'] = 'Tenemos algunos de estos inmuebles'

    # elif (meseg == 'Te recomiendo estos inmuebles'):

    #     rejson = wb.inmuebleREC_FAV("R")
    #     resul = json.loads(rejson)
    #     resul['messeg'] = 'Te recomiendo estos inmuebles'

    # elif (meseg == 'Los mas comprados son estos inmuebles'):

    #     rejson = wb.inmuebleREC_FAV("F")
    #     resul = json.loads(rejson)
    #     resul['messeg'] = 'Los mas comprados son estos inmuebles'

    # elif (meseg.rfind('https://www.facebook.com/') > -1):

    #     resul = json.loads(wb.getposfacebookinterprice(meseg))

    # elif (meseg.rfind('https://gojom.pe/') > -1):

    #     resul = json.loads(wb.getposwebinterprice(meseg))

    # else:
    #     resul['messeg'] = meseg

    # return json.dumps(resul)


initdatares()
#print(conversacionbot("hola, que tal como estas"))
#print(conversacionbot("quiero alquilar un inmueble"))
# print(parse_secuencia("que metodo puedo usar para publicar un inmueble",
#       pares[0]["inputpalclab"]["palabras"], 0, 0, 0))
# chatbot 2.0
print(converce("hola que tal"))
