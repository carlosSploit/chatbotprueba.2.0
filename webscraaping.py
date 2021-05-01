# importaciones de metodos para web scraping

from bs4 import BeautifulSoup
import requests
import pandas as pd
import interpre as inte
import json

UrlPrincipal = 'https://gojom.pe/'
# ****************************Web Scraping******************************

# metodo para poder extraer los datos de los inmuebles recomendados y favoritos
# con el url https://casas360.pe/


def inmuebleImfoExtrac(StriUrl, urlgene):
    # escaneo de la pagina web
    url = StriUrl
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ____________recoleccion de datos del mejor y del no mejor_________________

    # extraccion de etiquetas de las paginas web
    # extraer el titulo del inmueble
    e = soup.find_all('h1', class_="title font-weight-bold")
    # extraer la ciudad donde se encuenta
    ec = soup.find_all('div', class_="content_direction")
    eD = soup.find_all('span', class_="currency-local")
    eE = soup.find_all('small')
    eI = soup.find_all('figure', class_="swiper-group")

    name = ''  # para mantenerlo el titulo del inmueble
    city = ''  # para mantenerlo la ciudad donde se encuenta
    money = ''  # para mantenerlo el precio
    Espe = {}  # para mantenerlo en un array de espesificaciones
    Img = {}  # para mantenerlo en un array de Imagines

    # _________________Titulo Y Redirecconamiento___________________
    # solo acepta 8 datos de muestreo
    for i in e:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
            name = i.text

    # __________________Ciudad________________
    for i in ec:
        # if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles') and not('de' in i.text)):
        city = i.text
    # __________________Dinero________________
    money = eD[1].text
    # __________________Espesif_________________
    contE = 0  # para contar cada una de las espesificaciones
    for i in eE[0].find_all('div', class_="mr-3 my-1 d-inline-flex"):
        con = i.text.split()
        Espe[con[1]] = con[0]

    # __________________Images_________________
    contI = 0
    for i in eI:
        if (contI <= 5):
            Img[contI] = i.find_all('img')[0]['data-original']
        contI = contI + 1

    x = {}
    x = {'depart': name, 'costo': money, 'result': city,
         'url': url, "img": Img, "espe": Espe, 'urlg': urlgene}

    return x


def inmuebleREC_FAV(tipdar):
    # escaneo de la pagina web
    global UrlPrincipal
    url = UrlPrincipal
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ____________recoleccion de datos del mejor y del no mejor_________________

    # extraccion de etiquetas de las paginas web
    eq = soup.find_all('a', target="_blank")
    #eqD = soup.find_all('span', class_="currency-local")
    #eqC = soup.find_all('div', class_="address col")

    departamentos = list()  # lista de los nombres del lugar (descripccion)
    departamentosR = list()  # lista de las redirecciones
    # departamentosD = list()  # lista de los costos
    # departamentosC = list()  # lista de las ciudades

    # _________________Titulo Y Redireccion___________________
    # solo acepta 8 datos de muestreo
    for i in eq:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE')):
            departamentos.append(i.text)
            redireccion = 'https://gojom.pe' + i['href']
            departamentosR.append(redireccion)

    # title
    mejor = departamentos[0:7]
    departamentos.reverse()
    favorit = departamentos[0:7]
    favorit.reverse()

    # redirecci
    mejorR = departamentosR[0:7]
    departamentosR.reverse()
    favoritR = departamentosR[0:7]
    favoritR.reverse()

    # __________________Dinero________________
    # for i in eqD:
    #    if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE')):
    #        departamentosD.append(i.text)
    #
    #mejorD = departamentosD[0:7]
    # departamentosD.reverse()
    #favoritD = departamentosD[0:7]
    # favoritD.reverse()
    # __________________Ciudad________________
    # for i in eqC:
    #    if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE')):
    #        departamentosC.append(i.text)

    #mejorC = departamentosC[0:7]
    # departamentosC.reverse()
    #favoritC = departamentosC[0:7]
    # favoritC.reverse()

    x = {}

    # ______________________IMPRECION___________________
    if (tipdar == 'R'):
        x = {'Recomend': {}}
        print('**********************RECOMENDADO***************************')
        for i in range(7):
            aux = inmuebleImfoExtrac(mejorR[i], url)
            if (aux['img'] != {}):
                x['Recomend'][i] = aux

            print('----------------------------------------------------------')
    elif (tipdar == 'F'):
        x = {'Favorit': {}}
        print('************************FAVORITOS****************************')
        for i in range(7):
            aux = inmuebleImfoExtrac(favoritR[i], url)
            if (aux['img'] != {}):
                x['Favorit'][i] = aux

            print('----------------------------------------------------------')

    return json.dumps(x)

# metodo para poder extraer los datos de los inmuebles para comprar
# con el url https://casas360.pe/alquiler/inmueble?o=mas-baratos


def inmuebleCOMPRA(messeg):
    # escaneo de la pagina web
    global UrlPrincipal
    url = UrlPrincipal + 'compra/' + \
        inte.resulParatDat(messeg)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ____________recoleccion de datos del mejor y del no mejor_________________

    # extraccion de etiquetas de las paginas web
    e = soup.find_all('a', class_="text-black")
    #eD = soup.find_all('span', class_="currency-local")
    #eC = soup.find_all('div', class_="address")

    depart = list()
    departR = list()
    #departD = list()
    #departC = list()

    # _________________Titulo Y Redirecconamiento___________________
    for i in e:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
            depart.append(i.text)
            redireccion = 'https://gojom.pe' + i['href']
            departR.append(redireccion)

    # __________________Dinero________________
    #cont = 0
    # for i in eD:
    #    if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles') and not('de' in i.text)):
    #        if (cont % 2 == 0):
    #            departD.append(i.text)
    #        cont = cont + 1

    # __________________Ciudad________________
    # for i in eC:
    #    if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
    #        departC.append(i.text)

    x = {'Comprar': {}, 'messeg': 'none'}
    # si el array tiene una distancia mayor que 10 se imprimen solo 10 sino solo se imprimiran todos
    # a esto se le llama operador  terniario
    print('**********************Comprar***************************')
    # para evitar un acceso de datos solo se emprimira 10
    try:
        for i in range(10 if (len(depart) >= 10) else len(depart)):
            # guardar en json
            aux = inmuebleImfoExtrac(departR[i], url)
            if (aux['img'] != {}):
                x['Comprar'][i] = aux
    except:
        x['messeg'] = 'Parece ser que tengo un problema al momento de listar, pero puedes visitar a ' + url

    return json.dumps(x)

# metodo para poder extraer los datos de los inmuebles para alquilar
# con el url https://casas360.pe/alquiler/inmueble/


def inmuebleALQUILER(messeg):
    # escaneo de la pagina web
    global UrlPrincipal
    url = UrlPrincipal + 'alquiler/' + \
        inte.resulParatDat(messeg)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ____________recoleccion de datos del mejor y del no mejor_________________

    # extraccion de etiquetas de las paginas web
    e = soup.find_all('a', class_="text-black")
    #eD = soup.find_all('span', class_="currency-local")
    #eC = soup.find_all('div', class_="address")

    depart = list()
    departR = list()
    #departD = list()
    #departC = list()

    # _________________Titulo Y Redirecconamiento___________________
    # solo acepta 8 datos de muestreo
    for i in e:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
            depart.append(i.text)
            redireccion = 'https://gojom.pe' + i['href']
            departR.append(redireccion)

    # __________________Dinero________________
    #cont = 0
    # for i in eD:
    #    if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles') and not('de' in i.text)):
    #        if (cont % 2 == 0):
    #            departD.append(i.text)
    #        cont = cont + 1

    # __________________Ciudad________________
    # for i in eC:
    #    if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
    #        departC.append(i.text)

    x = {'alquiler': {}, 'messeg': 'none'}
    print('**********************Alquilados***************************')
    # si el array tiene una distancia mayor que 10 se imprimen solo 10 sino solo se imprimiran todos
    # a esto se le llama operador  terniario
    try:
        for i in range(10 if (len(depart) >= 10) else len(depart)):
            # guardar en json
            aux = inmuebleImfoExtrac(departR[i], url)
            if (aux['img'] != {}):
                x['alquiler'][i] = aux
    except IndexError:
        x['messeg'] = 'Parece ser que tengo un problema al momento de listar, pero puedes visitar a ' + url

    return json.dumps(x)


# probar metodos creados de web scraping
# inmuebleREC_FAV('R')
# inmuebleCOMPRA()
# inmuebleALQUILER()
# *******************************Chatboot*******************************
