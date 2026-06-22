# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Ciclos / Loops
#####################################


import calificador
from controlador import Controlador

# %%
@Controlador("3", "ejercicio_11")
def ejercicio_11(records, status):
    """
    Instrucciones:
        La función "ejercicio_11" toma una lista de diccionarios "records"
        y una cadena "status". Cada diccionario de la lista tiene una clave "status".
        La función debe regresar el número total de registros (diccionarios)
        cuyo status sea exactamente igual al valor proporcionado en el parámetro "status".

    Ejemplo:
        Si records = [{"id": 1, "status": "active"}, {"id": 2, "status": "inactive"}, {"id": 3, "status": "active"}]
        y status = "active", la función regresa 2.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_11([{"status": "active"}, {"status": "inactive"}], "active")

# %%
calificador.califica_ejercicio_11(ejercicio_11)

# %%
@Controlador("3", "ejercicio_12")
def ejercicio_12(max_retries):
    """
    Instrucciones:
        La función "ejercicio_12" recibe un número entero "max_retries" (intentos máximos).
        Debe simular un bucle de reintento de conexión e ir guardando el número de cada intento
        (empezando desde 1 hasta "max_retries" inclusive) en una lista, y finalmente regresar esa lista.
        Si "max_retries" es menor o igual a 0, regresa una lista vacía.

    Ejemplo:
        Si max_retries = 3, regresa [1, 2, 3].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_12(3)

# %%
calificador.califica_ejercicio_12(ejercicio_12)

# %%
@Controlador("3", "ejercicio_13")
def ejercicio_13(items, page, size):
    """
    Instrucciones:
        La función "ejercicio_13" recibe una lista "items", el número de página "page"
        (1-indexed, es decir, la primera página es la 1) y el tamaño de página "size" (entero).
        Debe calcular los índices correspondientes y regresar la sublista de elementos
        para esa página utilizando rebanado de listas (slicing) o un ciclo.

    Ejemplo:
        Si items = ["a", "b", "c", "d", "e"], page = 2 y size = 2,
        los elementos de la página 1 son ["a", "b"], y los de la página 2 son ["c", "d"].
        La función regresa ["c", "d"].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_13(["a", "b", "c", "d"], 2, 2)

# %%
calificador.califica_ejercicio_13(ejercicio_13)

# %%
@Controlador("3", "ejercicio_14")
def ejercicio_14(prices, discount):
    """
    Instrucciones:
        La función "ejercicio_14" recibe una lista de precios "prices" (números)
        y un porcentaje de descuento "discount" (float entre 0.0 y 1.0, por ejemplo, 0.10 para un 10%).
        Debe aplicar el descuento a cada uno de los precios de la lista y regresar una nueva lista
        con los precios con descuento aplicados.

    Ejemplo:
        Si prices = [100, 200, 50] y discount = 0.1, la función regresa:
        [90.0, 180.0, 45.0].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_14([100, 200], 0.1)

# %%
calificador.califica_ejercicio_14(ejercicio_14)

# %%
@Controlador("3", "ejercicio_15")
def ejercicio_15(logs, keyword):
    """
    Instrucciones:
        La función "ejercicio_15" recibe una lista de cadenas de texto "logs" y una palabra clave "keyword" (string).
        Debe regresar una nueva lista que contenga únicamente las líneas de log que incluyan
        la palabra clave "keyword" (búsqueda sensible a mayúsculas/minúsculas).

    Ejemplo:
        Si logs = ["[INFO] User logged in", "[ERROR] Connection failed", "[INFO] Job done"]
        y keyword = "Connection", la función regresa ["[ERROR] Connection failed"].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_15(["[INFO] OK", "[ERROR] Fail"], "Fail")

# %%
calificador.califica_ejercicio_15(ejercicio_15)
