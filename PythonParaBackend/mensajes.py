def mensaje_de_resultados(esperado, obtenido, argumentos=None):
    if argumentos:
        if len(argumentos) == 1:
            return f"\033[0;34m Valores de entrada: {argumentos[0]}. \
            \033[0;35m Valor esperado: {esperado}. \
            \033[0;36m Valor obtenido: {obtenido}\n\033[00m"
        else:
            return f"\033[0;34mValores de entrada: {argumentos}. \
            \033[0;35mValor esperado: {esperado}. \
            \033[0;36mValor obtenido: {obtenido}\n"
    else:
        return f"\033[0;34mValores de entrada: N/A. \
        \033[0;35mValor esperado: {esperado}. \
        \033[0;36mValor obtenido: {obtenido}\n"

def mensaje_no_hubo_errores():
    return "======> No hubo errores :D <======\n"

def mensaje_casos_de_error():
    return "\033[0;31m======> Casos con error <======\n\033[00m"

def mensaje_casos_existosos():
    return "======> Casos existosos: <======\n"

def mensaje_error(error):
    print("\033[0;31mHubo un error y no se pudo ejecutar el código, la tarea no fue calificada")
    print(f"El error es: {error}\033[00m")

def mensaje_resumen_errores_aciertos(calificacion, aciertos, errores):
    return f"""
======================================================
            ||          Calificación: {calificacion}            
            ||          Aciertos: {aciertos}                   
            ||          Errores: {errores}                     
======================================================
    """

def mensaje_enviando_calificacion():
    return "============> Enviando calificación <============\n"

def mensaje_de_error_en_servidor(respuesta):
    return f"""
            Hubo un error inesperado del lado del servidor, por favor
            revisa si tu calificación fue agregada.
            Error {respuesta.json()}
        """

def mensaje_de_calificacion_recibida():
    return "\033[0;32m============> Calificación recibida <============\n"

def mensaje_informacion_descriptiva_tarea_enviada(tarea, nombre):
    return f"""===============================================================================\n
============> Calificando: tarea {tarea} - ejercicio {nombre} <============\n
===============================================================================\n"""