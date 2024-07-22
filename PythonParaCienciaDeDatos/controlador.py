import traceback

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
                Controlador.__errores.append({"tarea": controlador_self.tarea, "ejercicio": controlador_self.tarea, "tipo": str(type(e)).split("'")[1], "descripcion": str(e)})

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