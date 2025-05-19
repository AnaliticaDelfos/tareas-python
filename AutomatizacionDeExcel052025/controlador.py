import traceback
from datetime import datetime, timezone, timedelta

class Controlador:
    __errores = []
    __mostrar_traceback = True
    def __init__(self, tarea, ejercicio):
        self.tarea = tarea
        self.ejercicio = ejercicio

    def __call__(self, func):
        controlador_self = self
        def contenedora(*args, **kwargs):
            resultado = None
            try:
                resultado = func(*args, **kwargs)
            except Exception as e:
                if Controlador.__mostrar_traceback:
                    traceback.print_exc()
                Controlador.__errores.append({"tarea": controlador_self.tarea, "ejercicio": controlador_self.tarea, "tipo": str(type(e)).split("'")[1]})

            return resultado
        return contenedora
    
    @staticmethod
    def obtener_errores():
        return Controlador.__errores
    
    @staticmethod
    def calificando():
        Controlador.__mostrar_traceback = True

    @staticmethod
    def ignorar_traceback():
        Controlador.__mostrar_traceback = False

    @staticmethod
    def limpiar_errores():
        Controlador.__errores.clear()
        
    @staticmethod
    def validar_fecha(tarea):
        fechas = {
            "0": datetime(2025, 6, 2, 23, 59, 59, tzinfo=timezone.utc),
            "1": datetime(2025, 6, 2, 23, 59, 59, tzinfo=timezone.utc),
            "2": datetime(2025, 6, 2, 23, 59, 59, tzinfo=timezone.utc),
            "3": datetime(2025, 6, 2, 23, 59, 59, tzinfo=timezone.utc),
            "4": datetime(2025, 6, 9, 23, 59, 59, tzinfo=timezone.utc),
            "5": datetime(2025, 6, 9, 23, 59, 59, tzinfo=timezone.utc),
            "6": datetime(2025, 6, 19, 19, 59, 59, tzinfo=timezone.utc),
            "7": datetime(2025, 6, 19, 19, 59, 59, tzinfo=timezone.utc),
        }
        return datetime.now(tz=timezone.utc) - timedelta(hours=6) < fechas[tarea] 