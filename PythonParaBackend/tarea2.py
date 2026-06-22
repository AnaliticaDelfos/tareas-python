# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Condicionales
#####################################


import calificador
from controlador import Controlador

# %%
@Controlador("2", "ejercicio_6")
def ejercicio_6(role):
    """
    Instrucciones:
        La función "ejercicio_6" toma un rol de usuario "role" (string).
        Debe regresar True si el rol es exactamente "admin" o "superuser".
        De lo contrario, regresa False.

    Ejemplo:
        Si role = "admin", regresa True.
        Si role = "guest", regresa False.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_6("admin")

# %%
calificador.califica_ejercicio_6(ejercicio_6)

# %%
@Controlador("2", "ejercicio_7")
def ejercicio_7(status_code):
    """
    Instrucciones:
        La función "ejercicio_7" recibe un código de estado HTTP "status_code" (entero).
        Debe clasificar el código y regresar un string según los siguientes rangos:
        - Si está en el rango 200 a 299 (inclusive ambos): regresa "SUCCESS"
        - Si está en el rango 400 a 499 (inclusive ambos): regresa "CLIENT_ERROR"
        - Si está en el rango 500 a 599 (inclusive ambos): regresa "SERVER_ERROR"
        - Para cualquier otro código: regresa "OTHER"

    Ejemplo:
        Si status_code = 200, regresa "SUCCESS".
        Si status_code = 404, regresa "CLIENT_ERROR".
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_7(200)

# %%
calificador.califica_ejercicio_7(ejercicio_7)

# %%
@Controlador("2", "ejercicio_8")
def ejercicio_8(username, password):
    """
    Instrucciones:
        La función "ejercicio_8" toma un nombre de usuario "username" (string)
        y una contraseña "password" (string).
        Debe regresar True si se cumplen ambas condiciones:
        - El nombre de usuario no es una cadena vacía ("").
        - La contraseña tiene una longitud de al menos 8 caracteres.
        De lo contrario, regresa False.

    Ejemplo:
        Si username = "user1" y password = "password123", regresa True.
        Si username = "" y password = "password123", regresa False.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_8("user1", "password123")

# %%
calificador.califica_ejercicio_8(ejercicio_8)

# %%
@Controlador("2", "ejercicio_9")
def ejercicio_9(age, has_consent):
    """
    Instrucciones:
        La función "ejercicio_9" recibe la edad "age" (entero) y si tiene
        consentimiento parental "has_consent" (booleano).
        Debe regresar True si la persona es mayor o igual a 18 años,
        O si es menor de 18 años pero "has_consent" es True.
        De lo contrario, regresa False.

    Ejemplo:
        Si age = 16 y has_consent = True, regresa True.
        Si age = 16 y has_consent = False, regresa False.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_9(16, True)

# %%
calificador.califica_ejercicio_9(ejercicio_9)

# %%
@Controlador("2", "ejercicio_10")
def ejercicio_10(content_type):
    """
    Instrucciones:
        La función "ejercicio_10" recibe un encabezado "content_type" (string).
        Debe regresar True si "content_type" es igual a "application/json"
        o a "application/xml" sin importar si está escrito en mayúsculas o minúsculas.
        De lo contrario, regresa False.

    Ejemplo:
        Si content_type = "APPLICATION/JSON", regresa True.
        Si content_type = "text/html", regresa False.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_10("APPLICATION/JSON")

# %%
calificador.califica_ejercicio_10(ejercicio_10)
