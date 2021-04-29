pal = 'quiero tomarme un trago en piura'

InmuDataSub = {'playa': 'casa-de-playa',
               'campo': 'casa-de-campo',
               'agrícola': 'terreno-agricola',
               'comercial': 'local-comercial',
               'industrial': 'local-industrial',
               'terreno': 'terreno-lote'}

InmuData = ['Departamento',
            'Casa',
            'comercial',
            'Oficina',
            'industrial',
            'playa',
            'campo',
            'agrícola',
            'terreno',
            'Oficina'
            ]

cityData = ['Amazonas',
            'Ancash',
            'Apurimac',
            'Arequipa',
            'Ayacucho',
            'Cajamarca',
            'Callao',
            'Cusco',
            'Huancavelica',
            'Huánuco',
            'Ica',
            'Junín',
            'La Libertad',
            'Lambayeque',
            'Lima',
            'Loreto',
            'Madre de Dios',
            'Moquegua',
            'Pasco',
            'Piura',
            'Puno',
            'San Martin',
            'Tacna',
            'Tumbes',
            'Ucayali'
            ]


def extradDatCity(palabra):
    global cityData
    extpal = palabra.split()
    auxtpal = []  # array auxiliar
    # trasformar palabras del array a minusculas
    for i in extpal:
        auxtpal.append(i.lower())

    extpal = auxtpal[:]  # clonar el array trasformado
    # verificar si una palabra esta dentro de la data de ciudades
    for i in cityData:
        if (i.lower() in extpal):
            return i.lower()
    # en caso que no aya encontrado nada, retorna una letra
    return ''


def extradDatClasIn(palabra):
    global InmuData
    global InmuDataSub
    extpal = palabra.split()
    auxtpal = []  # array auxiliar
    # trasformar palabras del array a minusculas
    for i in extpal:
        auxtpal.append(i.lower())

    extpal = auxtpal[:]  # clonar el array trasformado
    # verificar si una palabra esta dentro de la data de ciudades
    an = ''
    for i in InmuData:
        if (i.lower() in extpal):
            an = i.lower()
    # en caso que no aya encontrado nada, retorna una letra
    if (an != ''):
        if (an in InmuDataSub):
            return InmuDataSub[an]
        else:
            return an
    else:
        return 'inmueble'


def resulParatDat(palabra):
    city = extradDatCity(palabra)
    carinm = extradDatClasIn(palabra)
    if(city != ''):
        return carinm + '/' + city + '//'
    else:
        return carinm


print(resulParatDat("quiero alquilar en amazonas"))
