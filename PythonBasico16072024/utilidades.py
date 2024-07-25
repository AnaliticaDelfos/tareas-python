import requests
import os
import mensajes
from controlador import Controlador
errores = []
ID_CURSO = "3aq6COc5HgXKFpkMKo0j"
correo = os.environ.get("JUPYTERHUB_USER")

def mandar_a_firestore(ejercicio, calificacion, resultados, tarea):
    global correo
    if correo:
        if correo == 'delfos':
            correo = 'estudiante@analiticadelfos.com'
        ruta = "https://us-central1-cursos-delfos.cloudfunctions.net/get_grades"
    else:
        correo = 'estudiante@analiticadelfos.com'
        ruta = "http://127.0.0.1:8086"
    resp = requests \
        .post(ruta, \
        json={"uuid": correo, \
        "id_curso": ID_CURSO, \
        "ejercicio": ejercicio, \
        "id_tarea": f'{tarea}', \
        "calificacion": calificacion, \
        "resultados": resultados, \
        "edicion": "1", \
        "tipo": "jupyter",
        "errores": errores
        })
    if resp.status_code != 200:
        print(mensajes.mensaje_de_error_en_servidor(resp))
    if resp.status_code == 200:
        print(mensajes.mensaje_de_calificacion_recibida())

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

def helper(resultados, tarea, nombre, **kwargs):
    global errores
    errores =  Controlador.obtener_errores()
    if not kwargs['error']:
        print(mensajes.mensaje_informacion_descriptiva_tarea_enviada(tarea, nombre))
        aciertos_arr = []
        errores_arr = []
        for resultado in resultados:
            if resultado['estado']:
                aciertos_arr.append(resultado)
            else:
                errores_arr.append(resultado)
        total = len(resultados)
        errores_len = len(errores_arr)
        aciertos = len(aciertos_arr)
        if total != 0:
            calificacion = (aciertos / total) * 100
            print(mensajes.mensaje_resumen_errores_aciertos(calificacion, aciertos, errores_len))
            
            print(mensajes.mensaje_casos_existosos())
            
            for resultado in aciertos_arr:
                print(mensajes.mensaje_de_resultados(resultado['esperado'], resultado['obtenido'], resultado.get('argumentos')))
            if errores_len == 0:
                print("======> No hubo errores :D <======\n")
            else:
                print("\033[0;31m======> Casos con error <======\n\033[00m")
                for resultado in errores_arr:
                    print(mensajes.mensaje_de_resultados(resultado['esperado'], resultado['obtenido'], resultado.get('argumentos')))
            resultados = list(map(convertir_a_tupla, resultados))
            mandar_a_firestore(nombre, calificacion, resultados, tarea)
            
    else:
        # errores.append(str(kwargs['exception_type']))
        mandar_a_firestore(nombre, None, None, tarea)
        mensajes.mensaje_error(f"{kwargs['excepcion']}")

    Controlador.limpiar_errores()



