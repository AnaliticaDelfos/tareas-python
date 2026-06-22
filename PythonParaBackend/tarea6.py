# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Funciones
#####################################


import calificador
from controlador import Controlador

# %%
@Controlador("6", "ejercicio_26")
def ejercicio_26(username, role="guest"):
    """
    Instrucciones:
        La función "ejercicio_26" recibe un nombre de usuario "username" (string)
        y opcionalmente un rol "role" (string), el cual tiene como valor por defecto "guest".
        Debe regresar un diccionario con el formato: {"username": username, "role": role}.

    Ejemplo:
        Si llamamos ejercicio_26("angel"), regresa {"username": "angel", "role": "guest"}.
        Si llamamos ejercicio_26("admin", "superuser"), regresa {"username": "admin", "role": "superuser"}.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_26("angel")

# %%
calificador.califica_ejercicio_26(ejercicio_26)

# %%
@Controlador("6", "ejercicio_27")
def ejercicio_27(base_url, **query_params):
    """
    Instrucciones:
        La función "ejercicio_27" toma una URL base "base_url" (string) y un conjunto
        de parámetros de consulta variables mediante "**query_params".
        Debe construir y regresar la URL final con los parámetros concatenados como un query string.
        Los parámetros en el query string deben ordenarse alfabéticamente por su nombre de clave
        para asegurar un resultado consistente.
        Si no se pasan parámetros, regresa la "base_url" tal cual.

    Ejemplo:
        Si base_url = "https://api.delfos.com/users", query_params = {"limit": 10, "page": 1},
        la función regresa: "https://api.delfos.com/users?limit=10&page=1"
        (Nota: la clave "limit" va antes de "page" alfabéticamente).
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_27("https://api.delfos.com/users", limit=10, page=1)

# %%
calificador.califica_ejercicio_27(ejercicio_27)

# %%
@Controlador("6", "ejercicio_28")
def ejercicio_28(*middlewares):
    """
    Instrucciones:
        La función "ejercicio_28" recibe un número variable de cadenas de texto "*middlewares"
        que representan nombres de middlewares a ejecutar en un pipeline de backend.
        Debe regresar una lista con los nombres de los middlewares en orden inverso (del último al primero).

    Ejemplo:
        Si llamamos ejercicio_28("auth", "logger", "cors"), la función regresa ["cors", "logger", "auth"].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_28("auth", "logger")

# %%
calificador.califica_ejercicio_28(ejercicio_28)

# %%
@Controlador("6", "ejercicio_29")
def ejercicio_29(validator_func, data):
    """
    Instrucciones:
        La función "ejercicio_29" recibe una función validadora "validator_func" (que toma un argumento
        y regresa True o False) y un dato "data".
        Debe llamar a "validator_func" pasándole "data".
        - Si la llamada regresa False, la función debe levantar una excepción de tipo ValueError con el mensaje "Invalid data".
        - Si regresa True, debe regresar la cadena "Validated".

    Ejemplo:
        Si validator_func = lambda x: len(x) > 3 y data = "abc",
        levanta ValueError("Invalid data").
        Si data = "abcd", regresa "Validated".
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_29(lambda x: len(x) > 3, "abcd")

# %%
calificador.califica_ejercicio_29(ejercicio_29)

# %%
@Controlador("6", "ejercicio_30")
def ejercicio_30(f, *args, **kwargs):
    """
    Instrucciones:
        La función "ejercicio_30" recibe otra función "f", y parámetros variables "*args" y "**kwargs".
        Debe ejecutar la función "f" pasándole todos los argumentos "*args" y "**kwargs" recibidos,
        y regresar el resultado obtenido.

    Ejemplo:
        Si f = lambda x, y: x + y, args = (5, 10), kwargs = {},
        la función regresa 15.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_30(lambda x, y: x + y, 5, 10)

# %%
calificador.califica_ejercicio_30(ejercicio_30)
