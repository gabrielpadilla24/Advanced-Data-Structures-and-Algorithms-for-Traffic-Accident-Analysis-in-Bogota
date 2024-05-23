"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
default_limit = 1000
sys.setrecursionlimit(default_limit*1000)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    x= controller.new_controller()
    return x

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6-Los 10 accidentes menos recientes ocurridos en un mes y año para una localidad de la ciudad")
    print("7- Mostrar los N accidentes ocurridos dentro de una zona específica para un mes y un año")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control,crimesfile):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    x= controller.load_data(control,crimesfile)
    return x

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(data, f_inicial, f_final):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    respuesta = controller.req_1(data, f_inicial, f_final)[0]
    time = controller.req_1(data, f_inicial, f_final)[1]

    tabla =[
        ['CODIGO_ACCIDENTE', 'DIA_OCURRENCIA_ACC', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LOCALIDAD', 'FECHA_HORA_ACC', 'LATITUD', 'LONGITUD']


    ]
    for elemento in lt.iterator(respuesta):
        agregar = [elemento['CODIGO_ACCIDENTE'], elemento['DIA_OCURRENCIA_ACC'], elemento['DIRECCION'], elemento['GRAVEDAD'], elemento['CLASE_ACC'], elemento['LOCALIDAD'], elemento['FECHA_HORA_ACC'], elemento['LATITUD'], elemento['LONGITUD']]
        tabla.append(agregar)    
    
    print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))
    print(f"Hay {lt.size(respuesta)} accidentes registrados entre {f_inicial} y {f_final}")
    print(f"El tiempo de ejecucion es: {time}")





def print_req_2(data,anio, mes, hora_inicio, hora_fin):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print('========== Req No. 2 ==========') 
    respuesta = (controller.req_2(data, anio, mes, hora_inicio, hora_fin)[0])   
    time = (controller.req_2(data, anio, mes, hora_inicio, hora_fin)[1])   
    l_respuesta = lt.iterator(respuesta[1])
    print(f"Hay {respuesta[0]} accidentes en el intervalo de horas dado {hora_inicio} y {hora_final} para el mes {mes} de {anio}")
    tabla = [
        ['CODIGO_ACCIDENTE', 'HORA_OCURRENCIA_ACC', 'FECHA_OCURRENCIA_ACC', 'DIA_OCURRENCIA_ACC', 'LOCALIDAD', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD']
    ]
    for i in l_respuesta:
        fila = [i['CODIGO_ACCIDENTE'], i['HORA_OCURRENCIA_ACC'], i['FECHA_OCURRENCIA_ACC'], i['DIA_OCURRENCIA_ACC'], i['LOCALIDAD'], i['DIRECCION'], i['GRAVEDAD'], i['CLASE_ACC'], i['LATITUD'], i['LONGITUD']]
        tabla.append(fila)


    print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))
    print(f"El tiempo de ejecucion es: {time}")

def print_req_3(data, clase_acc, via):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print('========== Req No. 3 ==========')
    respuesta = controller.req_3(data, clase_acc, via)[0]
    time = controller.req_3(data, clase_acc, via)[1]
    print(f"Hay {respuesta[3]} accidentes de la clase {clase_acc} a lo largo de la vía {via} y los 3 más recientes son: ")
    tabla = [
        ['CODIGO_ACCIDENTE', 'FECHA_HORA_ACC', 'DIA_OCURRENCIA_ACC', 'LOCALIDAD', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD'],
        [respuesta[0]['value']['CODIGO_ACCIDENTE'], respuesta[0]['value']['FECHA_HORA_ACC'], respuesta[0]['value']['DIA_OCURRENCIA_ACC'], respuesta[0]['value']['LOCALIDAD'], respuesta[0]['value']['DIRECCION'], respuesta[0]['value']['GRAVEDAD'], respuesta[0]['value']['CLASE_ACC'], respuesta[0]['value']['LATITUD'], respuesta[0]['value']['LONGITUD']],
        [respuesta[1]['value']['CODIGO_ACCIDENTE'], respuesta[1]['value']['FECHA_HORA_ACC'], respuesta[1]['value']['DIA_OCURRENCIA_ACC'], respuesta[1]['value']['LOCALIDAD'], respuesta[1]['value']['DIRECCION'], respuesta[1]['value']['GRAVEDAD'], respuesta[1]['value']['CLASE_ACC'], respuesta[1]['value']['LATITUD'], respuesta[1]['value']['LONGITUD']],
        [respuesta[2]['value']['CODIGO_ACCIDENTE'], respuesta[2]['value']['FECHA_HORA_ACC'], respuesta[2]['value']['DIA_OCURRENCIA_ACC'], respuesta[2]['value']['LOCALIDAD'], respuesta[2]['value']['DIRECCION'], respuesta[2]['value']['GRAVEDAD'], respuesta[2]['value']['CLASE_ACC'], respuesta[2]['value']['LATITUD'], respuesta[2]['value']['LONGITUD']]

    ]
    print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))
    print(f"El tiempo de ejecucion es: {time}")
'''
    print(respuesta[0])
    print(respuesta[1])
    print(respuesta[2])'''

#        [respuesta[0]['CODIGO_ACCIDENTE'], respuesta[0]['FECHA_HORA_ACC'], respuesta[0]['DIA_OCURRENCIA_ACC'], respuesta[0]['LOCALIDAD'], respuesta[0]['DIRECCION'], respuesta[0]['GRAVEDAD'], respuesta[0]['CLASE_ACC'], respuesta[0]['LATITUD'], respuesta[0]['LONGITUD']]


def print_req_4(control, fecha_inicial, fecha_final, gravedad):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    dataans = controller.req_4(control, fecha_inicial, fecha_final, gravedad)
    
    print("Hay", dataans[2],"accidentes entre las fechas", fecha_inicial, "y", fecha_final)
    print(tabulate(dataans[0], headers="keys", tablefmt="fancy_grid"))

    
    print("Tiempo de ejecucion:", dataans[1])


def print_req_5(data, anio, mes, localidad):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    x=controller.req_5(data, anio, mes, localidad)
    respuesta = (controller.req_5(data, anio, mes, localidad)[0])   
    time = (controller.req_5(data, anio, mes, localidad)[1])   
    l_respuesta = lt.iterator(respuesta)
    tamanho=lt.size(respuesta)
    print('Estos son los '+str(tamanho)+' accidentes menos recientes en el mes de '+str(mes)+' del año '+str(anio)+' en la localidad de '+str(localidad))
    tabla = [
        ['CODIGO_ACCIDENTE','DIA_OCURRENCIA_ACC' ,'FECHA_HORA_ACC','DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD']
    ]
    for i in l_respuesta:
       
        fila = [i['CODIGO_ACCIDENTE'], i['DIA_OCURRENCIA_ACC'],i['FECHA_HORA_ACC'], i['DIRECCION'], i['GRAVEDAD'], i['CLASE_ACC'], i['LATITUD'], i['LONGITUD']]
        tabla.append(fila)

    print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))
    print(f"El tiempo de ejecucion es: {time}")
    return x

def print_req_6(data,anio,mes,latitud,longitud,radio,num):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    respuesta = (controller.req_6(data,anio,mes,latitud,longitud,radio,num)[0])   
    time = (controller.req_6(data,anio,mes,latitud,longitud,radio,num)[1])   
    l_respuesta = lt.iterator(respuesta)
    print('Estos son los '+str(num)+" accidentes mas cercanos a la localizacion de latitud "+str(latitud)+' y longitud '+str(longitud)+' en el año '+str(anio)+' en el mes '+str(mes))
    tabla = [
        ['CODIGO_ACCIDENTE', 'FECHA_HORA_ACC', 'DIA_OCURRENCIA_ACC', 'LOCALIDAD', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD']
    ]
    for i in l_respuesta:
       
        fila = [i['CODIGO_ACCIDENTE'], i['FECHA_HORA_ACC'], i['LOCALIDAD'], i['DIRECCION'], i['GRAVEDAD'], i['CLASE_ACC'], i['LATITUD'], i['LONGITUD']]
        tabla.append(fila)

    print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))
    print(f"El tiempo de ejecucion es: {time}")
    

def print_req_7(data, anio, mes):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    dataans = controller.req_7(data,anio,mes)
    
    for data in lt.iterator(dataans[0]):
        print()
        print("Primer y ultimo accidente para el día", data[0]["FECHA_OCURRENCIA_ACC"])
        print()
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
        print()
    
    print("Tiempo de ejecucion:", dataans[1])


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print('Ponga 1 si desea cargar el  archivo small')
                print('Ponga 2 si desea cargar el  archivo 5pct')
                print('Ponga 3 si desea cargar el  archivo 10pct')
                print('Ponga 4 si desea cargar el  archivo 20pct')
                print('Ponga 5 si desea cargar el  archivo 30pct')
                print('Ponga 6 si desea cargar el  archivo 50pct')
                print('Ponga 7 si desea cargar el  archivo 80pct')
                print('Ponga 8 si desea cargar el  archivo large')
                x=int(input())
                a=''
                if x==1:
                    a='datos_siniestralidad-small.csv'
                elif x==2:
                    a='datos_siniestralidad-5pct.csv'
                elif x==3:
                    a='datos_siniestralidad-10pct.csv'
                elif x==4:
                    a='datos_siniestralidad-20pct.csv'
                elif x==5:
                    a='datos_siniestralidad-30pct.csv'
                elif x==6:
                    a='datos_siniestralidad-50pct.csv'
                elif x==7:
                    a='datos_siniestralidad-80pct.csv'
                elif x==8:
                    a='datos_siniestralidad-large.csv'
                
                print("Cargando información de los archivos ....\n")

                print('')
                print('')
                print('')
                print('---------------------------------------------------')
                print('Información de los accidentes cargados: ')
                
                
                data = load_data(control,a)
                print(f"Total de accidentes: {data[1]}")
                print(f"Total de columnas: {data[2]}")
                
                datos = data[0]['Datos']['elements'][0:3]
                datos1 = data[0]['Datos']['elements'][-3:]

                print('Los primeros 3 registros de accidentes cargados fueron: ')
                tabla = [
                    ['FECHA_OCURRENCIA_ACC', 'HORA_OCURRENCIA_ACC', 'LOCALIDAD', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD'],
                    [datos[0]['FECHA_OCURRENCIA_ACC'], datos[0]['HORA_OCURRENCIA_ACC'], datos[0]['LOCALIDAD'],datos[0]['DIRECCION'], datos[0]['GRAVEDAD'], datos[0]['CLASE_ACC'], datos[0]['LATITUD'], datos[0]['LONGITUD']],
                    [datos[1]['FECHA_OCURRENCIA_ACC'], datos[1]['HORA_OCURRENCIA_ACC'], datos[1]['LOCALIDAD'],datos[1]['DIRECCION'], datos[1]['GRAVEDAD'], datos[1]['CLASE_ACC'], datos[1]['LATITUD'], datos[1]['LONGITUD']],
                    [datos[2]['FECHA_OCURRENCIA_ACC'], datos[2]['HORA_OCURRENCIA_ACC'], datos[2]['LOCALIDAD'],datos[2]['DIRECCION'], datos[2]['GRAVEDAD'], datos[2]['CLASE_ACC'], datos[2]['LATITUD'], datos[2]['LONGITUD']]
                    
                ]
                print(tabulate(tabla, headers='firstrow', tablefmt='fancy_grid'))
                print('')
                print('Los ultimos 3 registros de accidentes cargados fueron:')
                tabla1 = [
                    ['FECHA_OCURRENCIA_ACC', 'HORA_OCURRENCIA_ACC', 'LOCALIDAD', 'DIRECCION', 'GRAVEDAD', 'CLASE_ACC', 'LATITUD', 'LONGITUD'],
                    [datos1[0]['FECHA_OCURRENCIA_ACC'], datos1[0]['HORA_OCURRENCIA_ACC'], datos1[0]['LOCALIDAD'],datos1[0]['DIRECCION'], datos1[0]['GRAVEDAD'], datos1[0]['CLASE_ACC'], datos1[0]['LATITUD'], datos1[0]['LONGITUD']],
                    [datos1[1]['FECHA_OCURRENCIA_ACC'], datos1[1]['HORA_OCURRENCIA_ACC'], datos1[1]['LOCALIDAD'],datos1[1]['DIRECCION'], datos1[1]['GRAVEDAD'], datos1[1]['CLASE_ACC'], datos1[1]['LATITUD'], datos1[1]['LONGITUD']],
                    [datos1[2]['FECHA_OCURRENCIA_ACC'], datos1[2]['HORA_OCURRENCIA_ACC'], datos1[2]['LOCALIDAD'],datos1[2]['DIRECCION'], datos1[2]['GRAVEDAD'], datos1[2]['CLASE_ACC'], datos1[2]['LATITUD'], datos1[2]['LONGITUD']]
                    
                ]
                print(tabulate(tabla1, headers='firstrow', tablefmt='fancy_grid'))
                
            elif int(inputs) == 2:
                f_inicial = input("Escriba la fecha inicial: ")
                f_final = input("Escriba la fecha final: ")
                
                print_req_1(data, f_inicial, f_final)

            elif int(inputs) == 3:
                anio = int(input('Escriba el año que quiera consultar: '))
                mes = input('Escriba el mes que quiere consultar: ')
                hora_inicio = input('Escriba la hora de inicio: ')
                hora_final = input('Escriba la hora final: ')
                print_req_2(data, anio, mes, hora_inicio, hora_final)

            elif int(inputs) == 4:
                clase_acc = input('Escriba la clase del accidente que quiere consultar: ')
                via = input('Escriba la via para la cual quiere hacer la consulta: ')
                print_req_3(data, clase_acc, via)

            elif int(inputs) == 5:
                f_inicial = input("Escriba la fecha inicial: ")
                f_final = input("Escriba la fecha final: ")
                gravedad = input("Escriba la gravedad a consultar: ")
                
                print_req_4(data, f_inicial, f_final, gravedad)

            elif int(inputs) == 6:
                anio = int(input('Escriba el año entre 2015 y 2022 que quiera consultar: '))
                mes = input('Escriba el mes que quiere consultar: ')
                localidad = input('Escriba la localidad: ')
                
              
                print_req_5(data, anio, mes, localidad)

            elif int(inputs) == 7:
                anio = int(input('Escriba el año entre 2015 y 2022 que quiera consultar: '))
                mes = input('Escriba el mes que quiere consultar: ')
                latitud = input('Escriba la Latitud de las coordenadas del centro del área: ')
                longitud = input('Escriba la Longitud de las coordenadas del centro del área: ')
            
                radio=input('Escriba el radio del area: ')
                num=input('Escriba el numero de accidentes que desea que se muestren: ')
                print_req_6(data,anio,mes,latitud,longitud,radio,num)

            elif int(inputs) == 8:
                anio = int(input('Escriba el año entre 2015 y 2022 que quiera consultar: '))
                mes = input('Escriba el mes que quiere consultar: ')
                print_req_7(data, anio, mes)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
