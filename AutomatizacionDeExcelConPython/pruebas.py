#
#
# EJECUTAR ESTA CELDA
#
#

#####################################
#       Tarea ejemplo
#####################################


import calificador
from controlador import Controlador
CORREO = "estudiante@analiticadelfos.com"


@Controlador("1", "suma_test")
def suma_test(a, b):
    """
    Instrucciones:
        Esta función toma los parámetros a y b
        y devuelve la suma de dichos parámetros
    
    Ejemplo:
        Si a = 1
        y b = 2
        la función debe regresar un 3

    Recuerda:
        Lo que la función "regresa" va justo después
        de la palabra return

    Recuerda:
        Cuida la indentación.
    """

    # Escribe aquí tu código


    # Escribe aquí tu código

    return 1/0# Escribe aquí tu código


suma_test(1,2)

calificador.califica_suma_test(suma_test, CORREO, False)