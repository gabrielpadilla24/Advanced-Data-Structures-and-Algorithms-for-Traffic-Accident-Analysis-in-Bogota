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
 """

import config as cf
import model
import time
import csv
import tracemalloc
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    x= model.new_data_structs()
    return x


# Funciones para la carga de datos

def load_data(analyzer, crimesfile):
    """
    Carga los datos del reto y retorna un diccionario con el objeto analyzer y la cantidad de filas y columnas.
    """
    crimesfile = cf.data_dir + crimesfile
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"), delimiter=",")
    num_rows = len(list(input_file))  # Contar el número de filas
    num_cols = len(input_file.fieldnames)  # Contar el número de columnas

    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"), delimiter=",")
    for crime in input_file:
        model.add_data(analyzer['Datos'], crime)
        model.add_fecha(analyzer['fecha'],crime)
        model.add_aniomes(analyzer['Anio_y_mes'],crime)
        model.add_clase(analyzer['clase'],crime)
        model.add_gravedad(analyzer['gravedad'],crime)
        model.add_localidad(analyzer['localidad'],crime)

    return  analyzer,  num_rows,  num_cols


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start = get_time()
    returnable =  model.req_1(control, fecha_inicial, fecha_final)
    stop = get_time()
    time = delta_time(start, stop)
    return returnable, time


def req_2(control, anio, mes, hora_inicio, hora_final):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start = get_time()
    returnable =  model.req_2(control, anio, mes, hora_inicio, hora_final)
    stop = get_time()
    time = delta_time(start, stop)
    return returnable, time


def req_3(control, clase_acc, via):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    start = get_time()
    returnable =  model.req_3(control, clase_acc, via)
    stop = get_time()
    time = delta_time(start, stop)
    return returnable, time


def req_4(control, fecha_inicial, fecha_final, gravedad):
    """
    Retorna el resultado del requerimiento 4
    """
    start = get_time()
    returnable =  model.req_4(control, fecha_inicial, fecha_final, gravedad)[0]
    numac =  model.req_4(control, fecha_inicial, fecha_final, gravedad)[1]
    stop = get_time()
    time = delta_time(start, stop)
    return returnable, time, numac


def req_5(data, anio, mes, localidad):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start=get_time()
    x= model.req_5(data, anio, mes, localidad)
    stop=get_time()
    tiempo=delta_time(start,stop)
    return x,tiempo

def req_6(data,anio,mes,latitud,longitud,radio,num):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start=get_time()
    x= model.req_6(data,anio,mes,latitud,longitud,radio,num)
    stop=get_time()
    tiempo=delta_time(start,stop)
    return x,tiempo


def req_7(data, anio, mes):
    """
    Retorna el resultado del requerimiento 7
    """
    start=get_time()
    x= model.req_7(data, anio, mes)
    stop=get_time()
    tiempo=delta_time(start,stop)
    return x,tiempo


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
