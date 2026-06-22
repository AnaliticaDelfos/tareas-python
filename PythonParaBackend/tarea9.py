# %%
#
#
# EJECUTAR ESTA CELDA CADA VEZ QUE ENTRES A HACER LA TAREA
#
#

#####################################
#  Programación Orientada a Objetos
#####################################


import calificador
from controlador import Controlador

# %%
@Controlador("9", "ejercicio_41")
class Usuario:
    """
    Instrucciones:
        Define la clase "Usuario" que tenga:
        - Un constructor (__init__) que reciba y asigne los atributos de instancia:
          "username" (string) y "email" (string).
        - Un método de instancia "to_dict(self)" que regrese un diccionario
          con las claves "username" y "email" y sus respectivos valores.

    Ejemplo:
        u = Usuario("angel", "a@delfos.com")
        u.to_dict() regresa {"username": "angel", "email": "a@delfos.com"}.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

# %%
# Puedes probar tu clase aquí:
# u = Usuario("angel", "a@delfos.com")
# print(u.to_dict())

# %%
calificador.califica_ejercicio_41(Usuario)

# %%
@Controlador("9", "ejercicio_42")
class UsuarioVip:
    """
    Instrucciones:
        Define la clase "UsuarioVip" que herede de la clase "Usuario" definida en el ejercicio anterior.
        Debe tener:
        - Un constructor que reciba "username", "email" y adicionalmente "descuento" (float).
          Debe llamar al constructor de la clase base (super()) para asignar "username" y "email",
          y asignar "descuento" como atributo propio de la instancia.
        - Debe sobrescribir el método "to_dict(self)" para que regrese un diccionario
          con las claves "username", "email" y "descuento".

    Ejemplo:
        u_vip = UsuarioVip("angel_vip", "vip@delfos.com", 0.15)
        u_vip.to_dict() regresa {"username": "angel_vip", "email": "vip@delfos.com", "descuento": 0.15}.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

# %%
# Puedes probar tu clase aquí:
# u_vip = UsuarioVip("angel_vip", "vip@delfos.com", 0.15)
# print(u_vip.to_dict())

# %%
calificador.califica_ejercicio_42(UsuarioVip)

# %%
@Controlador("9", "ejercicio_43")
class BaseModel:
    """
    Instrucciones:
        Define la clase "BaseModel" que tenga:
        - Un constructor que reciba y asigne un atributo de instancia "id" (entero o string).
        - Un método de instancia "save(self, db_list)" que reciba una lista "db_list"
          (que simula una tabla de base de datos) y agregue a esta lista el diccionario del propio modelo
          (el cual obtendremos llamando a un método "to_dict(self)" que regresa {"id": self.id}).

    Ejemplo:
        db = []
        model = BaseModel(101)
        model.save(db)
        # db ahora contiene [{"id": 101}]
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

# %%
# Puedes probar tu clase aquí:
# db = []
# model = BaseModel(101)
# model.save(db)
# print(db)

# %%
calificador.califica_ejercicio_43(BaseModel)

# %%
# Para el ejercicio 44, definimos la excepción ValidationError:
class ValidationError(Exception):
    pass

@Controlador("9", "ejercicio_44")
def validate_user(user_dict):
    """
    Instrucciones:
        La función "validate_user" recibe un diccionario "user_dict".
        - Debe validar que la clave "username" exista y que su longitud sea mayor o igual a 3.
        - Si no cumple con esto, debe levantar la excepción "ValidationError"
          (ya definida arriba) con el mensaje de error: "Username invalido".
        - Si es válido, regresa True.

    Ejemplo:
        validate_user({"username": "al"}) -> levanta ValidationError("Username invalido")
        validate_user({"username": "ana"}) -> regresa True
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

    return # ← Escribe aquí tu código

# %%
# Puedes probar la función aquí:
# validate_user({"username": "ana"})

# %%
calificador.califica_ejercicio_44(validate_user)

# %%
@Controlador("9", "ejercicio_45")
class APIResponse:
    """
    Instrucciones:
        Define la clase "APIResponse" que tenga:
        - Un constructor que reciba y asigne los atributos de instancia:
          "status_code" (entero), "data" (diccionario o lista) y "message" (string).
        - Un método de instancia "is_success(self)" que regrese True si el código de estado
          "status_code" está en el rango de éxito de HTTP (mayor o igual a 200 y menor a 300).
          De lo contrario, regresa False.

    Ejemplo:
        res = APIResponse(200, {"id": 1}, "Success")
        res.is_success() regresa True.
        res_error = APIResponse(400, {}, "Bad Request")
        res_error.is_success() regresa False.
    """

    # Escribe aquí tu código ↓


    # Escribe aquí tu código ↑

# %%
# Puedes probar tu clase aquí:
# res = APIResponse(200, {}, "OK")
# print(res.is_success())

# %%
calificador.califica_ejercicio_45(APIResponse)
