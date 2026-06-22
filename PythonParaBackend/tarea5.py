# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Diccionarios y Conjuntos (Sets)
#####################################


import calificador
from controlador import Controlador

# %%
@Controlador("5", "ejercicio_21")
def ejercicio_21(user_data, key, default_value):
    """
    Instrucciones:
        La función "ejercicio_21" toma un diccionario "user_data", una cadena "key"
        y un valor por defecto "default_value".
        Debe buscar de forma segura la clave "key" en el diccionario y regresar su valor.
        Si la clave no existe, debe regresar el valor de "default_value".

    Ejemplo:
        Si user_data = {"username": "angel", "email": "angel@delfos.com"},
        key = "role" y default_value = "guest", la función regresa "guest".
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_21({"username": "angel"}, "role", "guest")

# %%
calificador.califica_ejercicio_21(ejercicio_21)

# %%
@Controlador("5", "ejercicio_22")
def ejercicio_22(user_roles, role_permissions, user):
    """
    Instrucciones:
        La función "ejercicio_22" recibe:
        - "user_roles": un diccionario que mapea nombres de usuarios a su rol (ej: {"ana": "admin"}).
        - "role_permissions": un diccionario que mapea roles a un conjunto (set) de permisos
          (ej: {"admin": {"read", "write"}}).
        - "user": un string con el nombre del usuario a buscar.
        Debe regresar el conjunto (set) de permisos del usuario.
        Si el usuario no está en "user_roles", o su rol no está en "role_permissions",
        debe regresar un conjunto vacío: set().

    Ejemplo:
        Si user_roles = {"juan": "editor"}, role_permissions = {"editor": {"read", "edit"}},
        y user = "juan", regresa {"read", "edit"}.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_22({"juan": "editor"}, {"editor": {"read"}}, "juan")

# %%
calificador.califica_ejercicio_22(ejercicio_22)

# %%
@Controlador("5", "ejercicio_23")
def ejercicio_23(db_records):
    """
    Instrucciones:
        La función "ejercicio_23" recibe una lista de diccionarios "db_records".
        Cada diccionario representa un registro de base de datos con una clave "id".
        Debe transformar esta lista en un único diccionario donde las llaves sean los "id" (enteros o strings)
        de cada registro y los valores sean los diccionarios completos. Regresa el diccionario resultante.

    Ejemplo:
        Si db_records = [{"id": 101, "name": "Prod A"}, {"id": 102, "name": "Prod B"}],
        la función regresa:
        {101: {"id": 101, "name": "Prod A"}, 102: {"id": 102, "name": "Prod B"}}
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_23([{"id": 1, "name": "A"}])

# %%
calificador.califica_ejercicio_23(ejercicio_23)

# %%
@Controlador("5", "ejercicio_24")
def ejercicio_24(api_scopes, route_scopes):
    """
    Instrucciones:
        La función "ejercicio_24" toma dos colecciones (listas o conjuntos) de scopes (permisos):
        - "api_scopes": los scopes asignados al token del usuario.
        - "route_scopes": los scopes requeridos por la ruta.
        Debe regresar True si TODOS los scopes requeridos en "route_scopes" están presentes
        dentro de "api_scopes". De lo contrario, regresa False.

    Ejemplo:
        Si api_scopes = ["read", "write", "delete"] y route_scopes = ["read", "write"],
        la función regresa True.
        Si api_scopes = ["read"] y route_scopes = ["read", "write"], regresa False.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_24(["read", "write"], ["read"])

# %%
calificador.califica_ejercicio_24(ejercicio_24)

# %%
@Controlador("5", "ejercicio_25")
def ejercicio_25(payload):
    """
    Instrucciones:
        La función "ejercicio_25" recibe un diccionario "payload".
        Debe limpiar el diccionario eliminando cualquier clave cuyo valor sea exactamente None,
        y regresar el diccionario modificado o uno nuevo.

    Ejemplo:
        Si payload = {"id": 1, "name": "Laptop", "description": None, "price": 1200},
        la función regresa {"id": 1, "name": "Laptop", "price": 1200}.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_25({"id": 1, "description": None})

# %%
calificador.califica_ejercicio_25(ejercicio_25)
