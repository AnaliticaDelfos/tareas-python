# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Entrada y Salida (I/O) de Archivos
#####################################


import calificador
from controlador import Controlador

# %%
@Controlador("7", "ejercicio_31")
def ejercicio_31(filepath):
    """
    Instrucciones:
        La función "ejercicio_31" recibe la ruta de un archivo de texto "filepath" que contiene líneas de log.
        Debe abrir el archivo en modo lectura, recorrerlo línea por línea y contar cuántas líneas
        contienen la palabra exacta "ERROR". Regresa ese conteo total (entero).

    Ejemplo:
        Si el archivo contiene:
        [INFO] Todo bien
        [ERROR] Falla en DB
        [WARNING] Lentitud detectada
        [ERROR] Falla en Auth
        La función regresa 2.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
# Para probar, puedes crear un archivo temporal en tu equipo.

# %%
calificador.califica_ejercicio_31(ejercicio_31)

# %%
@Controlador("7", "ejercicio_32")
def ejercicio_32(filepath, log_line):
    """
    Instrucciones:
        La función "ejercicio_32" recibe la ruta de un archivo "filepath" (string) y una línea de log "log_line" (string).
        Debe abrir el archivo en modo "append" (anexar al final) y escribir la línea de log.
        Asegúrate de agregar un salto de línea "\n" al final si "log_line" no lo incluye.

    Ejemplo:
        Si filepath = "logs.txt" y log_line = "[INFO] Endpoint hit",
        debe escribir "[INFO] Endpoint hit\n" al final del archivo.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
# Para probar, puedes crear un archivo temporal en tu equipo.

# %%
calificador.califica_ejercicio_32(ejercicio_32)

# %%
@Controlador("7", "ejercicio_33")
def ejercicio_33(filepath):
    """
    Instrucciones:
        La función "ejercicio_33" recibe la ruta de un archivo "filepath" que emula un archivo de configuración (.env).
        El archivo contiene líneas con el formato CLAVE=VALOR.
        Debe leer el archivo, saltar las líneas vacías o aquellas que comiencen con el caracter "#" (comentarios),
        y regresar un diccionario con los pares clave-valor (tanto clave como valor deben ser strings limpios
        de espacios en blanco al principio o al final).

    Ejemplo:
        Si el archivo contiene:
        # Configuración de base de datos
        DB_HOST=localhost
        DB_PORT=5432

        la función regresa {"DB_HOST": "localhost", "DB_PORT": "5432"}.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
# Para probar, puedes crear un archivo temporal en tu equipo.

# %%
calificador.califica_ejercicio_33(ejercicio_33)

# %%
@Controlador("7", "ejercicio_34")
def ejercicio_34(filepath, data):
    """
    Instrucciones:
        La función "ejercicio_34" recibe la ruta de un archivo "filepath" y un diccionario "data" (con datos planos).
        Debe abrir el archivo en modo escritura (sobrescribir) y guardar cada par clave-valor en el formato
        "clave: valor" (un par por línea).

    Ejemplo:
        Si data = {"host": "localhost", "port": 8000}, el archivo resultante debe contener:
        host: localhost
        port: 8000
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
# Para probar, puedes crear un archivo temporal en tu equipo.

# %%
calificador.califica_ejercicio_34(ejercicio_34)

# %%
@Controlador("7", "ejercicio_35")
def ejercicio_35(filepath):
    """
    Instrucciones:
        La función "ejercicio_35" recibe la ruta de un archivo CSV simple de usuarios "filepath".
        La primera línea contiene los encabezados: "id,nombre,rol".
        Las líneas siguientes contienen los datos de los usuarios, por ejemplo: "1,Ana,admin".
        Debe leer el archivo y regresar una lista de diccionarios con el formato:
        [{"id": "1", "nombre": "Ana", "rol": "admin"}, ...]

    Ejemplo:
        Si el archivo contiene:
        id,nombre,rol
        1,Ana,admin
        2,Pedro,guest
        La función regresa [{"id": "1", "nombre": "Ana", "rol": "admin"}, {"id": "2", "nombre": "Pedro", "rol": "guest"}].
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
# Para probar, puedes crear un archivo temporal en tu equipo.

# %%
calificador.califica_ejercicio_35(ejercicio_35)
