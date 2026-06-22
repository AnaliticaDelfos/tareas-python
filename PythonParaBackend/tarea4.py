# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Listas y Tuplas
#####################################


import calificador
from controlador import Controlador

# %%
@Controlador("4", "ejercicio_16")
def ejercicio_16(queue, task):
    """
    Instrucciones:
        La función "ejercicio_16" toma una lista "queue" que representa una cola de tareas
        y un string "task" que es la nueva tarea a encolar.
        Debe agregar la nueva tarea al final de la cola y regresar la lista resultante.
        Modifica la lista original en el proceso o crea una nueva.

    Ejemplo:
        Si queue = ["enviar_email", "procesar_pago"] y task = "generar_pdf",
        la función regresa ["enviar_email", "procesar_pago", "generar_pdf"].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_16(["tarea1"], "tarea2")

# %%
calificador.califica_ejercicio_16(ejercicio_16)

# %%
@Controlador("4", "ejercicio_17")
def ejercicio_17(queue):
    """
    Instrucciones:
        La función "ejercicio_17" recibe una lista "queue" (cola de tareas).
        Debe extraer y remover la primera tarea de la cola (primer elemento).
        Debe regresar una tupla que contenga:
        1. La tarea extraída.
        2. La lista de la cola restante (sin la tarea extraída).
        Si la cola está vacía, debe regresar la tupla (None, []).

    Ejemplo:
        Si queue = ["enviar_email", "procesar_pago", "generar_pdf"],
        la función regresa ("enviar_email", ["procesar_pago", "generar_pdf"]).
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_17(["tarea1", "tarea2"])

# %%
calificador.califica_ejercicio_17(ejercicio_17)

# %%
@Controlador("4", "ejercicio_18")
def ejercicio_18(user_ids):
    """
    Instrucciones:
        La función "ejercicio_18" recibe una lista de enteros o strings "user_ids"
        que contiene elementos duplicados.
        Debe remover los duplicados y regresar una lista que conserve únicamente los valores únicos,
        pero manteniendo el orden de aparición original de los elementos.

    Ejemplo:
        Si user_ids = [4, 1, 2, 4, 3, 1], la función regresa [4, 1, 2, 3].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_18([1, 2, 2, 3])

# %%
calificador.califica_ejercicio_18(ejercicio_18)

# %%
@Controlador("4", "ejercicio_19")
def ejercicio_19(headers_list, header_name):
    """
    Instrucciones:
        La función "ejercicio_19" recibe una lista "headers_list" de tuplas, donde cada tupla
        tiene el formato (header_name, header_value), y un string "header_name".
        Debe buscar el header cuyo nombre coincida de forma insensible a mayúsculas/minúsculas
        con "header_name", y regresar su valor (string).
        Si no se encuentra el header, regresa None.

    Ejemplo:
        Si headers_list = [("Content-Type", "application/json"), ("Authorization", "Bearer token123")]
        y header_name = "authorization", la función regresa "Bearer token123".
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_19([("Content-Type", "application/json")], "content-type")

# %%
calificador.califica_ejercicio_19(ejercicio_19)

# %%
@Controlador("4", "ejercicio_20")
def ejercicio_20(list1, list2):
    """
    Instrucciones:
        La función "ejercicio_20" recibe dos listas de strings ("list1" y "list2") que contienen
        nombres de usuarios.
        Debe unir ambas listas, ordenar los elementos alfabéticamente y regresar la lista resultante.

    Ejemplo:
        Si list1 = ["Carlos", "Ana"] y list2 = ["Beatriz", "Daniel"],
        la función regresa ["Ana", "Beatriz", "Carlos", "Daniel"].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_20(["Carlos", "Ana"], ["Beatriz"])

# %%
calificador.califica_ejercicio_20(ejercicio_20)
