# importaciones de metodos para web scraping

from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

# ****************************Web Scraping******************************

# metodo para poder extraer los datos de los inmuebles recomendados y favoritos
# con el url https://casas360.pe/


def inmuebleREC_FAV(tipdar):
    # escaneo de la pagina web
    url = 'https://casas360.pe/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ____________recoleccion de datos del mejor y del no mejor_________________

    # extraccion de etiquetas de las paginas web
    eq = soup.find_all('a', target="_blank")
    eqD = soup.find_all('span', class_="currency-local")
    eqC = soup.find_all('div', class_="address col")

    departamentos = list()  # lista de los nombres del lugar (descripccion)
    departamentosR = list()  # lista de las redirecciones
    departamentosD = list()  # lista de los costos
    departamentosC = list()  # lista de las ciudades

    # _________________Titulo Y Redireccion___________________
    # solo acepta 8 datos de muestreo
    for i in eq:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE')):
            departamentos.append(i.text)
            redireccion = 'https://casas360.pe' + i['href']
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
    for i in eqD:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE')):
            departamentosD.append(i.text)

    mejorD = departamentosD[0:7]
    departamentosD.reverse()
    favoritD = departamentosD[0:7]
    favoritD.reverse()
    # __________________Ciudad________________
    for i in eqC:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE')):
            departamentosC.append(i.text)

    mejorC = departamentosC[0:7]
    departamentosC.reverse()
    favoritC = departamentosC[0:7]
    favoritC.reverse()

    # ______________________IMPRECION___________________
    if (tipdar == 'R'):
        print('**********************RECOMENDADO***************************')
        for i in range(7):
            print('title: ', mejor[i])
            print('costo: ', mejorD[i])
            print('ciudad: ', mejorC[i])
            print('url: ', mejorR[i])
            print('----------------------------------------------------------')
    elif (tipdar == 'F'):
        print('************************FAVORITOS****************************')
        for i in range(7):
            print('title: ', favorit[i])
            print('costo: ', favoritD[i])
            print('ciudad: ', favoritC[i])
            print('url: ', favoritR[i])
            print('----------------------------------------------------------')

# metodo para poder extraer los datos de los inmuebles para comprar
# con el url https://casas360.pe/alquiler/inmueble?o=mas-baratos


def inmuebleCOMPRA():
    # escaneo de la pagina web
    url = 'https://casas360.pe/alquiler/inmueble?o=mas-baratos'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ____________recoleccion de datos del mejor y del no mejor_________________

    # extraccion de etiquetas de las paginas web
    e = soup.find_all('a', class_="text-black")
    eD = soup.find_all('span', class_="currency-local")
    eC = soup.find_all('div', class_="address")

    depart = list()
    departR = list()
    departD = list()
    departC = list()

    # _________________Titulo Y Redirecconamiento___________________
    for i in e:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
            depart.append(i.text)
            redireccion = 'https://casas360.pe' + i['href']
            departR.append(redireccion)

    # __________________Dinero________________
    cont = 0
    for i in eD:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles') and not('de' in i.text)):
            if (cont % 2 == 0):
                departD.append(i.text)
            cont = cont + 1

    # __________________Ciudad________________
    for i in eC:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
            departC.append(i.text)

    x = {'Comprar': {}}
    # si el array tiene una distancia mayor que 10 se imprimen solo 10 sino solo se imprimiran todos
    # a esto se le llama operador  terniario
    print('**********************Comprar***************************')
    # para evitar un acceso de datos solo se emprimira 10
    for i in range(10 if (len(depart) >= 10) else len(depart)):
        # guardado en json
        x['Comprar'][i] = {'depart': depart[i], 'costo': departD[i],
                           'result': departC[i], 'url': departR[i]}
    return json.dumps(x)

# metodo para poder extraer los datos de los inmuebles para alquilar
# con el url https://casas360.pe/alquiler/inmueble/


def inmuebleALQUILER():
    # escaneo de la pagina web
    url = 'https://casas360.pe/alquiler/inmueble/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # ____________recoleccion de datos del mejor y del no mejor_________________

    # extraccion de etiquetas de las paginas web
    e = soup.find_all('a', class_="text-black")
    eD = soup.find_all('span', class_="currency-local")
    eC = soup.find_all('div', class_="address")

    depart = list()
    departR = list()
    departD = list()
    departC = list()

    # _________________Titulo Y Redirecconamiento___________________
    # solo acepta 8 datos de muestreo
    for i in e:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
            depart.append(i.text)
            redireccion = 'https://casas360.pe' + i['href']
            departR.append(redireccion)

    # __________________Dinero________________
    cont = 0
    for i in eD:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles') and not('de' in i.text)):
            if (cont % 2 == 0):
                departD.append(i.text)
            cont = cont + 1

    # __________________Ciudad________________
    for i in eC:
        if((i.text != 'Analizar') and (i.text != '') and (i.text != 'TITLE') and (i.text != 'Inmuebles')):
            departC.append(i.text)

    x = {'alquiler': {}, 'messeg': ''}
    print('**********************Alquilados***************************')
    # si el array tiene una distancia mayor que 10 se imprimen solo 10 sino solo se imprimiran todos
    # a esto se le llama operador  terniario
    for i in range(10 if (len(depart) >= 10) else len(depart)):
        # guardar en json
        x['alquiler'][i] = {'depart': depart[i], 'costo': departD[i],
                            'result': departC[i], 'url': departR[i]}

    return json.dumps(x)


# probar metodos creados de web scraping
# inmuebleREC_FAV('R')
# inmuebleCOMPRA()
# inmuebleALQUILER()
# *******************************Chatboot*******************************
