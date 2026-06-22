# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Manejo de Excepciones
#####################################


import calificador
from controlador import Controlador

# Definición de la excepción personalizada para el Ejercicio 40:
class MissingEmailError(Exception):
    pass

# %%
@Controlador("8", "ejercicio_36")
def ejercicio_36(db_func):
    """
    Instrucciones:
        La función "ejercicio_36" recibe otra función "db_func" (que simula una consulta a base de datos).
        Debe intentar ejecutar "db_func()".
        - Si la ejecución es exitosa, regresa su resultado.
        - Si levanta cualquier excepción, debe capturarla y regresar el string "DATABASE_ERROR".

    Ejemplo:
        Si db_func = lambda: 1 / 0, la función regresa "DATABASE_ERROR".
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_36(lambda: "OK")

# %%
calificador.califica_ejercicio_36(ejercicio_36)

# %%
@Controlador("8", "ejercicio_37")
def ejercicio_37(json_parse_func, raw_str):
    """
    Instrucciones:
        La función "ejercicio_37" recibe una función "json_parse_func" y un string "raw_str".
        Debe intentar ejecutar "json_parse_func(raw_str)".
        - Si ocurre un ValueError o un TypeError durante la ejecución,
          debe capturar el error y regresar el diccionario: {"error": "invalid_format"}.
        - Si es exitoso, regresa el resultado del parseo.

    Ejemplo:
        Si json_parse_func = int y raw_str = "no_es_un_numero",
        se levanta ValueError, por lo que regresa {"error": "invalid_format"}.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_37(int, "123")

# %%
calificador.califica_ejercicio_37(ejercicio_37)

# %%
@Controlador("8", "ejercicio_38")
def ejercicio_38(value):
    """
    Instrucciones:
        La función "ejercicio_38" recibe un valor "value".
        - Si "value" no es de tipo entero (int) o es menor o igual a 0,
          debe levantar una excepción de tipo ValueError con el mensaje: "Debe ser entero positivo".
        - De lo contrario, regresa el valor.

    Ejemplo:
        Si value = -5 o "5", levanta ValueError("Debe ser entero positivo").
        Si value = 10, regresa 10.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_38(10)

# %%
calificador.califica_ejercicio_38(ejercicio_38)

# %%
@Controlador("8", "ejercicio_39")
def ejercicio_39(db_func, cleanup_func):
    """
    Instrucciones:
        La función "ejercicio_39" recibe "db_func" (que simula una operación de base de datos)
        y "cleanup_func" (que simula cerrar la conexión).
        Debe ejecutar "db_func()" y regresar su resultado, pero asegurándose
        de que la función "cleanup_func()" siempre sea ejecutada sin importar si la primera falló o no.
        Nota: si "db_func()" levanta un error, este debe propagarse (no capturarse para silenciarlo),
        pero la limpieza debe haber ocurrido antes de propagarlo.

    Ejemplo:
        Si db_func = lambda: 42, y cleanup_func limpia, regresa 42.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_39(lambda: 42, lambda: print("Limpieza"))

# %%
calificador.califica_ejercicio_39(ejercicio_39)

# %%
@Controlador("8", "ejercicio_40")
def ejercicio_40(user_data):
    """
    Instrucciones:
        La función "ejercicio_40" recibe un diccionario "user_data".
        Debe verificar si la clave "email" está presente en el diccionario.
        - Si la clave "email" no está presente, debe levantar la excepción personalizada
          "MissingEmailError" (ya definida arriba).
        - Si está presente, regresa el valor asociado a la clave "email".

    Ejemplo:
        Si user_data = {"username": "pedro"}, levanta MissingEmailError.
        Si user_data = {"email": "p@delfos.com"}, regresa "p@delfos.com".
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
ejercicio_40({"email": "p@delfos.com"})

# %%
calificador.califica_ejercicio_40(ejercicio_40)
