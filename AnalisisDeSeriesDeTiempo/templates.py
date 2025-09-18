from models.resultado import Resultado
import mensajes
from utilidades import helper
from controlador import Controlador
import pandas as pd
from typing import Any
import numpy as np

def template_sencillo(esperado, nombre, tarea, argumentos=[]):
    """
    Argumentos:
        esperado: El valor que debe regresar la función
        nombre: El nombre de la función como cadena de caracteres
        tarea: el sufijo que representa la tarea actual
        argumentos: Una lista de argumentos que serán pasados a la función

    Ejemplo:
        @template_sencillo({1,2,3,4,5}, 'conjunto_con_elementos_del_1_al_5', tarea) No manda argumentos
        @template_sencillo("HOLA, MUNDO", "en_mayusculas", tarea, ["hola, mundo"]) Manda argumentos

    """
    def decoradora(funcion):
        def contenedora(f):
            error = False
            resultados = []
            excepcion = None
            try:
                resultado_obtenido = funcion(f)(*argumentos)
                resultado_esperado = esperado
                estado = resultado_obtenido == resultado_esperado
                resultados.append(Resultado(None, resultado_esperado, resultado_obtenido, estado).__dict__)
            except Exception as e:
                mensajes.mensaje_error(e)
                error = True
                excepcion = str(e)

            helper(resultados, tarea, nombre, error=error, excepcion=excepcion, exception_type=type(e))
        return contenedora
    return decoradora

def template_iterable(lista, nombre, tarea):
    """
    Argumentos:
        lista: Una lista que incluye en primer lugar una lista de elementos a evaluar
                y en segundo lugar el valor esperado
        nombre: El nombre de la función como cadena de caracteres
        tarea: el sufijo que representa la tarea actual

    Ejemplo: 
    @template_iterable([
        [["Hola"], 'H'],
        [["mundo",], 'm'],
        [["me"], 'm'],
        [["gusta"], 'g'],
        [["este"], 'e'],
        [["curso"], 'c'],
        [["y las"], 'y'],
        [["tareas"], 't'],
        [["están"], 'e'],
        [["geniales"], 'g']
    ], 'primer_caracter', tarea)
    """
    def decoradora(funcion):
        def contenedora(f):
            error = False
            resultados = []
            excepcion = None
            excepcion_type = None
            Controlador.calificando()
            
            for tupla in lista:
                try:
                    resultado_obtenido = funcion(f)(*tupla[0])
                    resultado_esperado = tupla[1]
                    estado = resultado_obtenido == resultado_esperado
                    resultados.append(Resultado(tupla[0], resultado_esperado, resultado_obtenido, estado).__dict__)
                except Exception as e:
                    mensajes.mensaje_error(e)
                    error = True
                    excepcion = str(e)
                    excepcion_type = type(e)
                    break
                Controlador.ignorar_traceback()
            Controlador.calificando()

            helper(resultados, tarea, nombre, error=error, excepcion=excepcion, exception_type=excepcion_type)
        return contenedora
    return decoradora 


def template_poo(lista: list, nombre, tarea):
    """
    Argumentos: 
        lista: Lista de tuplas que contiene en primer lugar el tipo de dato a evaluar: propiedad o metodo;
        en segundo lugar el atributo a buscar, tercer lugar los argumentos a usar y en cuarto lugar el valor esperado.
        clase: La clase que se usará para construir objetos.

    """
    def decoradora(funcion):
        def contenedora(c):
            obj = c()
            error = False
            resultados = []
            excepcion = None
            excepcion_type = None
            Controlador.calificando()
            
            for item in lista:
                try:
                    f = getattr(obj, item[1])
                    if item[0] == "metodo":
                        resultado_obtenido = f(*item[2])
                    else:
                        resultado_obtenido = f
                    resultado_esperado = item[3]
                    estado = resultado_obtenido == resultado_esperado
                    resultados.append(Resultado(item[2], resultado_esperado, resultado_obtenido, estado).__dict__)
                except Exception as e:
                    mensajes.mensaje_error(e)
                    error = True
                    excepcion = str(e)
                    excepcion_type = type(e)
                    break
            helper(resultados, tarea, nombre, error=error, excepcion=excepcion, exception_type=excepcion_type)
        return contenedora
    return decoradora

def template_pandas(lista: list, nombre, tarea):
    """
    Argumentos:
        caso: En primer lugar es el valor esperado y en segundo lugar los argumentos, dar [] cuando no haya argumentos

    """
    def decoradora(funcion):
        def contenedora(f):
            error = False
            resultados = []
            excepcion = None
            excepcion_type = None
            Controlador.calificando()
            try:
                resultado_obtenido = funcion(f)(*lista[0])
                if type(lista[1]) == pd.Series or type(lista[1]) == pd.DataFrame:
                    estado = lista[1].equals(resultado_obtenido)
                else:
                    estado = lista[1] == resultado_obtenido
                resultados.append(Resultado(None, lista[1], resultado_obtenido, estado).__dict__)
            except Exception as e:
                mensajes.mensaje_error(e)
                error = True
                excepcion = str(e)
                excepcion_type = type(e)
                Controlador.ignorar_traceback()
            Controlador.calificando()

            helper(resultados, tarea, nombre, error=error, excepcion=excepcion, exception_type=excepcion_type)
        return contenedora
    return decoradora

def template_numpy(lista: list, nombre, tarea):
    """
    Argumentos:
        caso: En primer lugar es el valor esperado y en segundo lugar los argumentos, dar [] cuando no haya argumentos

    """
    def decoradora(funcion):
        def contenedora(f):
            error = False
            resultados = []
            excepcion = None
            excepcion_type = None
            Controlador.calificando()
            try:
                resultado_obtenido: np.ndarray = funcion(f)(*lista[0])
                estado = bool(np.all(resultado_obtenido == lista[1]))
                resultados.append(Resultado(None, lista[1], resultado_obtenido, estado).__dict__)
            except Exception as e:
                mensajes.mensaje_error(e)
                error = True
                excepcion = str(e)
                excepcion_type = type(e)
                Controlador.ignorar_traceback()
            Controlador.calificando()

            helper(resultados, tarea, nombre, error=error, excepcion=excepcion, exception_type=excepcion_type)
        return contenedora
    return decoradora