import requests
from datetime import datetime

prod = True

class Resultado:
    def __init__(self, argumentos, esperado, obtenido, estado):
        self.argumentos = argumentos
        self.esperado = esperado
        self.obtenido = obtenido
        self.estado = estado

def mandar_a_firestore(uuid, ejercicio, calificacion, resultados, opinion, tarea):
    print(f"============> Enviando calificación <============\n")
    resp = requests \
        .post("https://us-central1-cursos-delfos.cloudfunctions.net/get_grades", \
        json={"uuid": uuid, \
        "id_curso": "mjJLGuQqX1pR5iR6IrDI", \
        "ejercicio": ejercicio, \
        "id_tarea": f'{tarea}', \
        "calificacion": calificacion, \
        "resultados": resultados, \
        "edicion": "1", \
        "tipo": "jupyter"
        })
    if resp.status_code != 200:
        print(f"""
            Hubo un error inesperado del lado del servidor, por favor
            revisa si tu calificación fue agregada.
            Error {resp.json()}
        """)
    if resp.status_code == 200:
        print(f"============> Calificación recibida <============\n")

def deseo_ayudar():
    while True:
        entrada = (input("""
        ========================================================
        || Del 0 al 5, donde 0 es no me sirvió en lo absoluto ||
        || y 5 es me sirvió muchísimo                         ||
        || ¿Qué tanto te sirvió este ejercicio?:              ||
        ========================================================
        """))
        try:
            numero = int(entrada)
            if numero > 5:
                print("Que entusiasta! Gracias! :D")
            elif numero < 0:
                print("¿De verdad no te gustó? :(")
            return numero
        except:
            print("Me diste algo que no es un número")


def convertir_a_tupla(r):
    esperado = r['esperado']
    obtenido = r['obtenido']
    argumentos = r['argumentos']
    estado = r['estado']
    if type(esperado) == set:
        esperado = tuple(esperado)
    if type(obtenido) == set:
        obtenido = tuple(obtenido)
    if type(argumentos) == set:
        argumentos = tuple(argumentos)
    return {'esperado': esperado, 'obtenido': obtenido, 'argumentos': argumentos, 'estado': estado}

def helper(resultados, tarea, nombre, uuid, **kwargs):
    if not kwargs['error']:
        assert uuid != None, "Ingresa tu correo"
        assert uuid != "TU CORREO", "Ingresa tu correo"
        print(f"===============================================================================\n")
        print(f"============> Calificando: tarea {tarea} - ejercicio {nombre} <============\n")
        print(f"===============================================================================\n")
        aciertos_arr = []
        errores_arr = []
        for resultado in resultados:
            if resultado['estado']:
                aciertos_arr.append(resultado)
            else:
                errores_arr.append(resultado)
        total = len(resultados)
        errores = len(errores_arr)
        aciertos = len(aciertos_arr)
        if total != 0:
            calificacion = (aciertos / total) * 100
            print(f"""
        ======================================================
                    ||          Calificación: {calificacion}            
                    ||          Aciertos: {aciertos}                   
                    ||          Errores: {errores}                     
        ======================================================
            """)
            
            print("======> Casos existosos: <======\n")
            
            for resultado in aciertos_arr:
                if resultado['argumentos']:
                    if len(resultado['argumentos']) == 1:
                        print(f"Valores de entrada: {resultado['argumentos'][0]}. \
                        Valor esperado: {resultado['esperado']}. \
                        Valor obtenido: {resultado['obtenido']}\n")
                    else:
                        print(f"Valores de entrada: {resultado['argumentos']}. \
                        Valor esperado: {resultado['esperado']}. \
                        Valor obtenido: {resultado['obtenido']}\n")
                else:
                    print(f"Valores de entrada: N/A. \
                    Valor esperado: {resultado['esperado']}. \
                    Valor obtenido: {resultado['obtenido']}\n")
             
            if errores == 0:
                print("======> No hubo errores :D <======\n")
            else:
                print("======> Casos con error <======\n")
                for resultado in errores_arr:
                    if resultado['argumentos']:
                        if len(resultado['argumentos']) == 1:
                            print(f"Valores de entrada: {resultado['argumentos'][0]}. \
                            Valor esperado: {resultado['esperado']}. \
                            Valor obtenido: {resultado['obtenido']}\n")
                        else:
                            print(f"Valores de entrada: {resultado['argumentos']}. \
                            Valor esperado: {resultado['esperado']}. \
                            Valor obtenido: {resultado['obtenido']}\n")
                    else:
                        print(f"Valores de entrada: N/A. \
                        Valor esperado: {resultado['esperado']}. \
                        Valor obtenido: {resultado['obtenido']}\n")
            if kwargs['deseo']:
                opinion = deseo_ayudar()
            else:
                opinion = None
            resultados = list(map(convertir_a_tupla, resultados))
            if prod:
                mandar_a_firestore(uuid, nombre, calificacion, resultados, opinion, tarea)
            else:
                print("Sandbox")
    else:
        ...
        # print(kwargs['excepcion'])

def mensaje_error(error):
    print("Hubo un error y no se pudo ejecutar el código, la tarea no fue calificada")
    print(f"El error es: {error}")

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
        def contenedora(f, uuid, deseo_ayudar):
            error = False
            resultados = []
            excepcion = None
            try:
                resultado_obtenido = funcion(f, uuid, deseo_ayudar)(*argumentos)
                resultado_esperado = esperado
                estado = resultado_obtenido == resultado_esperado
                resultados.append(Resultado(None, resultado_esperado, resultado_obtenido, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                excepcion = str(e)

            helper(resultados, tarea, nombre, uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)
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
        def contenedora(f, uuid, deseo_ayudar):
            error = False
            resultados = []
            excepcion = None
            for tupla in lista:
                try:
                    resultado_obtenido = funcion(f, uuid, deseo_ayudar)(*tupla[0])
                    resultado_esperado = tupla[1]
                    estado = resultado_obtenido == resultado_esperado
                    resultados.append(Resultado(tupla[0], resultado_esperado, resultado_obtenido, estado).__dict__)
                except Exception as e:
                    mensaje_error(e)
                    error = True
                    excepcion = str(e)
                    break

            helper(resultados, tarea, nombre, uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)
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
        def contenedora(c, uuid, deseo_ayudar):
            obj = c()
            error = False
            resultados = []
            excepcion = None
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
                    mensaje_error(e)
                    error = True
                    excepcion = str(e)
                    break
            helper(resultados, tarea, nombre, uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)
        return contenedora
    return decoradora