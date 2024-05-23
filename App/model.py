"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from DISClib.DataStructures import rbt
assert cf
import datetime
import time
import math as math
import matplotlib.pyplot as plt


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    analyzer= {'Datos': None,
               'fecha':None,
               'Anio_y_mes':None,
               'clase':None,
               'gravedad':None,
               'localidad':None}
    analyzer['Datos']=lt.newList('ARRAY_LIST',cmpDatos)
    analyzer['fecha']=om.newMap('RBT',cmpFecha)
    analyzer['Anio_y_mes']=om.newMap()
    analyzer['clase']=mp.newMap()
    analyzer['gravedad']=mp.newMap()
    analyzer['localidad']=mp.newMap()
    return analyzer

def cmpFecha(offense1, offense2):
    """
    Compara dos tipos de crimenes
    """
    
    if (offense1 == offense2):
        return 0
    elif (offense1 > offense2):
        return 1
    else:
        return -1
    
def cmpDatos(datos_1,datos_2):
    if (datos_1 == datos_2):
        return 0
    elif (datos_1 > datos_2):
        return 1
    else:
        return -1

# Funciones para agregar informacion al modelo

def add_data(analyzer, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    lt.addLast(analyzer,data)
    
def add_fecha(tree,crimen):
    fecha=crimen['HORA_OCURRENCIA_ACC']
    fecha=datetime.datetime.strptime(fecha,'%H:%M:%S')
    
    pos=om.get(tree,fecha.date())
    if pos is None:
        dateEntry=lt.newList()
        om.put(tree, fecha.date(),dateEntry)
    else:
        dateEntry= me.getValue(pos)
    lt.addLast(dateEntry,crimen)
    return tree
    
    
    
def add_aniomes(tree,crimen):
    anio=int(crimen['ANO_OCURRENCIA_ACC'])
    mes=crimen['MES_OCURRENCIA_ACC']
    esta=om.contains(tree,anio)
    if esta:
        entry=om.get(tree,anio)
        anio_nuevo=me.getValue(entry)
    else:
        anio_nuevo=mp.newMap()
        om.put(tree,anio,anio_nuevo)
    esta_el_mes=mp.contains(anio_nuevo,mes)
    if esta_el_mes:
        entry=mp.get(anio_nuevo,mes)
        mes_nuevo=me.getValue(entry)
    else:
        mes_nuevo=lt.newList()
        mp.put(anio_nuevo,mes,mes_nuevo)
    lt.addLast(mes_nuevo,crimen)
    return tree
    
    
def add_clase(map,crimen):
    clase=crimen['CLASE_ACC']
    esta=mp.contains(map,clase)
    if esta:
        entry=mp.get(map,clase)
        clase_nueva=me.getValue(entry)
    else:
        clase_nueva=lt.newList()
        mp.put(map,clase,clase_nueva)
    lt.addLast(clase_nueva,crimen)
    return map

def add_gravedad(map,crimen):
    clase=crimen['GRAVEDAD']
    esta=mp.contains(map,clase)
    if esta:
        entry=mp.get(map,clase)
        clase_nueva=me.getValue(entry)
    else:
        clase_nueva=lt.newList()
        mp.put(map,clase,clase_nueva)
    lt.addLast(clase_nueva,crimen)
    return map

def add_localidad(map,crimen):
    clase=crimen['LOCALIDAD']
    esta=mp.contains(map,clase)
    if esta:
        entry=mp.get(map,clase)
        clase_nueva=me.getValue(entry)
    else:
        clase_nueva=lt.newList()
        mp.put(map,clase,clase_nueva)
    lt.addLast(clase_nueva,crimen)
    return map

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    x=mp.get(data_structs,id)
    return x


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 1
    """
    datos = data_structs[0]
    filtered = lt.newList()
    x = datos['Datos']['elements']
    for i in x:
        fecha = i['FECHA_OCURRENCIA_ACC']
        if fecha >= fecha_inicial and fecha <= fecha_final:
            lt.addLast(filtered, i)

    return filtered


def req_2(data_structs, anio, mes, hora_inicio, hora_fin):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    mes = mes.upper()
    datos = data_structs[0]
    anio = om.get(datos['Anio_y_mes'], anio)
    datos_anio = anio['value']
    filtrado_mes = mp.get(datos_anio, mes)
    x = filtrado_mes['value']

    datos_iterables = lt.iterator(x)
    lista_tabulate = lt.newList()

    for i in datos_iterables:
        hora = i['HORA_OCURRENCIA_ACC']
        if hora > hora_inicio and hora < hora_fin:
            lt.addLast(lista_tabulate, i)



    
    

    return lt.size(lista_tabulate), lista_tabulate


def req_3(data_structs, clase_acc, via):
    """
    Función que soluciona el requerimiento 3
    """
    datos = data_structs[0]
    clase_acc = clase_acc.upper()
    datos_cl_acc = mp.get(datos['clase'], clase_acc)
    x = (datos_cl_acc['value'])

    nuevo = om.newMap()
    lista_iterable = lt.iterator(x)

    for i in lista_iterable:
        if via in i['DIRECCION']:
            om.put(nuevo, i['FECHA_HORA_ACC'], i)
    total = om.size(nuevo)
    mas_reciente_key = om.maxKey(nuevo)
    mas_reciente = om.get(nuevo, mas_reciente_key)
    om.remove(nuevo, mas_reciente_key)
    mas_reciente2_key = om.maxKey(nuevo)
    mas_reciente2 = om.get(nuevo, mas_reciente2_key)
    om.remove(nuevo, mas_reciente2_key)
    mas_reciente3_key = om.maxKey(nuevo)
    mas_reciente3 = om.get(nuevo, mas_reciente3_key)
    
    return mas_reciente, mas_reciente2, mas_reciente3, total
    


def req_4(data_structs, fecha_inicial, fecha_final, gravedad):
    """
    Función que soluciona el requerimiento 1
    """
    gravedad = gravedad.upper()
    datos = data_structs[0]
    infecha = lt.newList()
    x = datos['Datos']['elements']
    for i in x:
        fecha = i['FECHA_OCURRENCIA_ACC']
        if fecha >= fecha_inicial and fecha <= fecha_final:
            lt.addLast(infecha, i)

    filtered = lt.newList()
    
    for acc in lt.iterator(infecha):
        gravity = acc['GRAVEDAD']
        if gravity == gravedad:
            lt.addLast(filtered, acc)
            
    numac = lt.size(filtered)
    
    filtered = merg.sort(filtered, cmpFechaHora)
    
    cincooldest = lt.subList(filtered, 1, 5)
    
    returnable = {"CODIGO_ACCIDENTE":[], "FECHA_HORA_ACC":[], "DIA_OCURRENCIA_ACC":[], "LOCALIDAD":[], "DIRECCION":[], "CLASE_ACC":[], "LATITUD":[], "LONGITUD":[]}
    
    for acc in lt.iterator(cincooldest):
        for key in returnable.keys():
            returnable[key].append(acc[key])
    
    return returnable, numac


def req_5(data, anio, mes, localidad):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    mes = mes.upper()
    datos = data[0]
    anio = om.get(datos['Anio_y_mes'], anio)
    datos_anio = anio['value']
    filtrado_mes = mp.get(datos_anio, mes)
    x = filtrado_mes['value']

    datos_iterables = lt.iterator(x)
    lista_tabulate = lt.newList()
    mapa=om.newMap()
    for i in datos_iterables:
        if i['LOCALIDAD']==localidad:
         
          om.put(mapa, i['FECHA_OCURRENCIA_ACC'], i)
    
    lista_final=lt.newList()
    keyset=om.keySet(mapa)
    for i in lt.iterator(keyset):
        entry=om.get(mapa,i)
        x=me.getValue(entry)
        x['Fechas']=i
        lt.addLast(lista_final,x)
    
    lista_ordenada=merg.sort(lista_final,compFech)
    
    tamanhoL=lt.size(lista_final)
    if tamanhoL>=10:
        lista_ordenada=lt.subList(lista_ordenada,1,10)
    
    return lista_ordenada

def compFech(datos_1,datos_2):
    datos_1=datetime.datetime.strptime(datos_1['Fechas'], "%Y/%m/%d")
    datos_2=datetime.datetime.strptime(datos_2['Fechas'], "%Y/%m/%d")
    if (datos_1 >datos_2):
        return True
    elif (datos_1 < datos_2):
        return False
    
def req_6(data,anio,mes,latitud,longitud,radio,num):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    #Formula Haversine
     # TODO: Realizar el requerimiento 5
    mes = mes.upper()
    datos = data[0]
    anio = om.get(datos['Anio_y_mes'], anio)
    datos_anio = anio['value']
    filtrado_mes = mp.get(datos_anio, mes)
    x = filtrado_mes['value']
    
    datos_iterables = lt.iterator(x)
    latitud=float(latitud)
    longitud=float(longitud)
   
    mapa=om.newMap()
    lon1=longitud
    lat1=latitud
    for i in datos_iterables:
        lon2= i['LONGITUD']
        lat2=i['LATITUD'] 
        lon2=float(lon2)
        lat2=float(lat2)
        c=haversine(lon1,lon2,lat1,lat2)
        
        if c<=float(radio):
            om.put(mapa,c,i)
    lista_final=lt.newList()
   
    
    
    keyset=om.keySet(mapa)
    for i in lt.iterator(keyset):
        entry=om.get(mapa,i)
        x=me.getValue(entry)
        x['Distancia']=i
        lt.addLast(lista_final,x)
    
    lista_ordenada=merg.sort(lista_final,cmpKM)
    
    
    
    tamanhoL=lt.size(lista_final)
    if tamanhoL>=int(num):
        lista_ordenada=lt.subList(lista_ordenada,1,int(num))
    
    return lista_ordenada
    

def haversine(lon1,lon2,lat1,lat2):
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    km = 6367 * c
    return km     
def cmpKM(datos_1,datos_2):
    datos_1=datos_1['Distancia']
    datos_2=datos_2['Distancia']
    if (datos_1 <datos_2):
        return True
    elif (datos_1 > datos_2):
        return False
    

def addDataFecha(mapa, llave, elem):
    esta=mp.contains(mapa,llave)
    if esta:            
        entry=mp.get(mapa,llave)
        clase_nueva=me.getValue(entry)
    else:
        clase_nueva=lt.newList()            
        mp.put(mapa,llave,clase_nueva)
    lt.addLast(clase_nueva,elem)     
        
"""def addDataFechaOM(mapa, llave, elem):
    esta=om.contains(mapa,llave)
    if esta:            
        entry=om.get(mapa,llave)
        clase_nueva=om.get(mapa, entry)
    else:
        clase_nueva=lt.newList()            
        om.put(mapa,llave,clase_nueva)
    lt.addLast(clase_nueva,elem)  """

def req_7(data, anio, mes):
    """
    Función que soluciona el requerimiento 7
    """
    
    yr = str(anio)
    mes = mes.upper()
    datos = data[0]
    anio = om.get(datos['Anio_y_mes'], anio)
    datos_anio = anio['value']
    filtrado_mes = mp.get(datos_anio, mes)["value"]
    
    
    bytime = mp.newMap(maptype="CHAINING")
    for elem in lt.iterator(filtrado_mes):
        fixed = {
            "CODIGO_ACCIDENTE" : elem["CODIGO_ACCIDENTE"],
            "FECHA_HORA_ACC" : elem["FECHA_HORA_ACC"], "DIA_OCURRENCIA_ACC" : elem["DIA_OCURRENCIA_ACC"], 
            "LOCALIDAD" : elem["LOCALIDAD"], "DIRECCION" : elem["DIRECCION"], "GRAVEDAD" : elem["GRAVEDAD"],
            "CLASE_ACC" : elem["CLASE_ACC"], "LATITUD" : elem["LATITUD"], "LONGITUD" : elem["LONGITUD"],
            "HORA_OCURRENCIA_ACC" : elem["HORA_OCURRENCIA_ACC"], "FECHA_OCURRENCIA_ACC" : elem["FECHA_OCURRENCIA_ACC"]}
        addDataFecha(bytime, elem["FECHA_OCURRENCIA_ACC"], fixed)
        
    """bytime = om.newMap("RBT", cmpFecha)
    for elem in lt.iterator(filtrado_mes):
        fixed = {
            "CODIGO_ACCIDENTE" : elem["CODIGO_ACCIDENTE"],
            "FECHA_HORA_ACC" : elem["FECHA_HORA_ACC"], "DIA_OCURRENCIA_ACC" : elem["DIA_OCURRENCIA_ACC"], 
            "LOCALIDAD" : elem["LOCALIDAD"], "DIRECCION" : elem["DIRECCION"], "GRAVEDAD" : elem["GRAVEDAD"],
            "CLASE_ACC" : elem["CLASE_ACC"], "LATITUD" : elem["LATITUD"], "LONGITUD" : elem["LONGITUD"],
            "HORA_OCURRENCIA_ACC" : elem["HORA_OCURRENCIA_ACC"], "FECHA_OCURRENCIA_ACC" : elem["FECHA_OCURRENCIA_ACC"]}
        addDataFechaOM(bytime, elem["FECHA_OCURRENCIA_ACC"], fixed)"""
        
    firstlastacc = lt.newList()
    flag1 = True
    flag2 = True    
    
    keys = mp.keySet(bytime)    
    #keys = merg.sort(keys, cmpDate)
    
        
    for index, day in enumerate(lt.iterator(keys)):
        lt.addLast(firstlastacc, [lt.getElement(mp.get(bytime, day)["value"], 1),lt.getElement(mp.get(bytime, day)["value"], 1)])
        #lt.addLast(firstlastacc, [lt.getElement(om.get(bytime, day)["value"], 1),lt.getElement(om.get(bytime, day)["value"], 1)])
        for acc in lt.iterator(mp.get(bytime, day)["value"]):
            if time.strptime(acc["HORA_OCURRENCIA_ACC"], "%H:%M:%S") < time.strptime(lt.getElement(firstlastacc,index+1)[0]["HORA_OCURRENCIA_ACC"], "%H:%M:%S"):
                lt.getElement(firstlastacc,index+1)[0] = acc
                flag1= False
            if time.strptime(acc["HORA_OCURRENCIA_ACC"], "%H:%M:%S") > time.strptime(lt.getElement(firstlastacc,index+1)[1]["HORA_OCURRENCIA_ACC"], "%H:%M:%S"):
                lt.getElement(firstlastacc,index+1)[1] = acc
                flag2 = False
        if flag1:
            lt.getElement(firstlastacc,index+1)[0] = lt.getElement(firstlastacc,index+1)[1]
        if flag2:
            lt.getElement(firstlastacc,index+1)[1] = lt.getElement(firstlastacc,index+1)[0]
    
    
    fig = plt.figure(figsize = (10, 5))
    
    horas = lt.newList()
    headers = ["00:00:00", "01:00:00", "02:00:00", "03:00:00", "04:00:00", "05:00:00", "06:00:00", "07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00", "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00", "17:00:00", "18:00:00", "19:00:00", "20:00:00", "21:00:00", "22:00:00", "23:00:00"]
    [lt.addLast(horas, i) for i in headers]
    values = [0]*len(headers)
    
    for day in lt.iterator(mp.keySet(bytime)):
        for acc in lt.iterator(mp.get(bytime, day)["value"]):
            for index, franjas in enumerate(lt.iterator(horas)):
                if index != lt.size(horas)-1:
                    if acc["HORA_OCURRENCIA_ACC"] > franjas and acc["HORA_OCURRENCIA_ACC"] < lt.getElement(horas, index+2):
                        values[index] += 1
    
    
    plt.bar(headers, values, color ='maroon',
            width = 0.4)
    
    plt.xticks(rotation=90)
    plt.xlabel("Hora del día")
    plt.ylabel("Número de accidentes")
    plt.title("Frecuencia de 31 accidentes por hora del día Para el mes de"+ mes+ "de"+ yr)
    plt.show(block=False)
    
    return firstlastacc
    


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento

def cmpDate(datos_1,datos_2):
    if (time.strptime(datos_1, "%Y/%m/%d") == time.strptime(datos_2, "%Y/%m/%d")):

        return 0
    elif (time.strptime(datos_1, "%Y/%m/%d") > time.strptime(datos_2, "%Y/%m/%d")):

        return 1
    else:
        
        return -1
    
def cmpFechaHora(datos_1,datos_2):
    if (time.strptime(datos_1["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00") == time.strptime(datos_2["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00")):

        return 0
    elif (time.strptime(datos_1["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00") < time.strptime(datos_2["FECHA_HORA_ACC"], "%Y/%m/%d %H:%M:%S+00")):

        return 1
    else:
        
        return -1


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
