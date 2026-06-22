# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Tipos de datos y operaciones
#####################################


import calificador
from controlador import Controlador

# %%
@Controlador("1", "ejercicio_1")
def ejercicio_1(host, port):
    """
    Instrucciones:
        La función "ejercicio_1" toma los parámetros "host" (string)
        y "port" (entero o string), y debe regresar la URL base del servidor
        HTTP en el formato: "http://host:port"

    Ejemplo:
        Si host = "localhost" y port = 8000, la función regresa:
        "http://localhost:8000"

    Recuerda:
        Cuida la indentación y convierte el puerto a string si es necesario.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_1("localhost", 8000)

# %%
calificador.califica_ejercicio_1(ejercicio_1)

# %%
@Controlador("1", "ejercicio_2")
def ejercicio_2(db_uri):
    """
    Instrucciones:
        La función "ejercicio_2" toma el parámetro "db_uri" (string) que representa
        una URI de conexión a base de datos, y debe regresar el motor de base de
        datos utilizado (la parte antes de "://").

    Ejemplo:
        Si db_uri = "postgresql://user:pass@localhost:5432/mydb",
        la función regresa "postgresql".

    Recuerda:
        Usa métodos de strings como split.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_2("postgresql://user:pass@localhost:5432/mydb")

# %%
calificador.califica_ejercicio_2(ejercicio_2)

# %%
@Controlador("1", "ejercicio_3")
def ejercicio_3(port_str):
    """
    Instrucciones:
        La función "ejercicio_3" recibe un puerto en formato de texto "port_str"
        y debe regresar el mismo puerto convertido en un tipo de dato entero (int).

    Ejemplo:
        Si port_str = "8080", la función regresa 8080.

    Recuerda:
        Utiliza la función de conversión int().
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_3("8080")

# %%
calificador.califica_ejercicio_3(ejercicio_3)

# %%
@Controlador("1", "ejercicio_4")
def ejercicio_4(path, query_params):
    """
    Instrucciones:
        La función "ejercicio_4" toma "path" (string) y "query_params" (string).
        Debe construir y regresar la ruta completa.
        Si "query_params" no está vacío, concatena "?" y "query_params" al final del path.
        Si "query_params" está vacío, regresa únicamente el "path".

    Ejemplo:
        Si path = "/users" y query_params = "limit=10&page=2", regresa:
        "/users?limit=10&page=2"
        Si path = "/status" y query_params = "", regresa:
        "/status"
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_4("/users", "limit=10&page=2")

# %%
calificador.califica_ejercicio_4(ejercicio_4)

# %%
@Controlador("1", "ejercicio_5")
def ejercicio_5(level, message):
    """
    Instrucciones:
        La función "ejercicio_5" toma un nivel de log "level" (string)
        y un mensaje "message" (string), y debe regresar un log formateado
        donde el nivel de log esté en mayúsculas y encerrado en corchetes.

    Ejemplo:
        Si level = "info" y message = "User logged in", regresa:
        "[INFO] User logged in"
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_5("info", "User logged in")

# %%
calificador.califica_ejercicio_5(ejercicio_5)
