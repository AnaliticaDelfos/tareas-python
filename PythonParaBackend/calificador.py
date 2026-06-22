from templates import template_iterable, template_sencillo, template_custom
from models.resultado import Resultado
import os


####################################################################################################
#                                       Tarea 0 (Ejemplo)
####################################################################################################

@template_iterable([
    [[1, 2], 3],
], 'ejercicio_0_1', '0')
def califica_ejercicio_0_1(f):
    return f

@template_iterable([
    [[1, 2], -1],
], 'ejercicio_0_2', '0')
def califica_ejercicio_0_2(f):
    return f

@template_iterable([
    [[], "Hola, mundo!"],
], 'ejercicio_0_3', '0')
def califica_ejercicio_0_3(f):
    return f


####################################################################################################
#                                       Tarea 1 (Tipos de datos y operaciones)
####################################################################################################

@template_iterable([
    [["localhost", 8000], "http://localhost:8000"],
    [["127.0.0.1", 5432], "http://127.0.0.1:5432"],
    [["api.delfos.com", "443"], "http://api.delfos.com:443"]
], 'ejercicio_1', '1')
def califica_ejercicio_1(f):
    return f

@template_iterable([
    [["postgresql://user:pass@localhost:5432/mydb"], "postgresql"],
    [["sqlite:///:memory:"], "sqlite"],
    [["mongodb+srv://cluster/db"], "mongodb+srv"]
], 'ejercicio_2', '1')
def califica_ejercicio_2(f):
    return f

@template_iterable([
    [["8080"], 8080],
    [["443"], 443],
    [["5000"], 5000]
], 'ejercicio_3', '1')
def califica_ejercicio_3(f):
    return f

@template_iterable([
    [["/users", "limit=10&page=2"], "/users?limit=10&page=2"],
    [["/products", "category=books"], "/products?category=books"],
    [["/status", ""], "/status"]
], 'ejercicio_4', '1')
def califica_ejercicio_4(f):
    return f

@template_iterable([
    [["info", "User logged in"], "[INFO] User logged in"],
    [["error", "Failed to connect to database"], "[ERROR] Failed to connect to database"],
    [["WARNING", "Disk space low"], "[WARNING] Disk space low"]
], 'ejercicio_5', '1')
def califica_ejercicio_5(f):
    return f


####################################################################################################
#                                       Tarea 2 (Condicionales)
####################################################################################################

@template_iterable([
    [["admin"], True],
    [["superuser"], True],
    [["guest"], False],
    [["user"], False]
], 'ejercicio_6', '2')
def califica_ejercicio_6(f):
    return f

@template_iterable([
    [[200], "SUCCESS"],
    [[204], "SUCCESS"],
    [[400], "CLIENT_ERROR"],
    [[404], "CLIENT_ERROR"],
    [[500], "SERVER_ERROR"],
    [[503], "SERVER_ERROR"],
    [[302], "OTHER"],
    [[101], "OTHER"]
], 'ejercicio_7', '2')
def califica_ejercicio_7(f):
    return f

@template_iterable([
    [["user1", "password123"], True],
    [["", "password123"], False],
    [["user1", "pass"], False],
    [["", ""], False]
], 'ejercicio_8', '2')
def califica_ejercicio_8(f):
    return f

@template_iterable([
    [[20, False], True],
    [[20, True], True],
    [[16, True], True],
    [[16, False], False],
    [[18, False], True]
], 'ejercicio_9', '2')
def califica_ejercicio_9(f):
    return f

@template_iterable([
    [["application/json"], True],
    [["APPLICATION/JSON"], True],
    [["application/xml"], True],
    [["Application/Xml"], True],
    [["text/html"], False],
    [["image/png"], False]
], 'ejercicio_10', '2')
def califica_ejercicio_10(f):
    return f


####################################################################################################
#                                       Tarea 3 (Ciclos)
####################################################################################################

@template_iterable([
    [[[{"id": 1, "status": "active"}, {"id": 2, "status": "inactive"}, {"id": 3, "status": "active"}], "active"], 2],
    [[[{"status": "pending"}, {"status": "pending"}], "pending"], 2],
    [[[{"status": "pending"}, {"status": "pending"}], "active"], 0],
    [[[], "active"], 0]
], 'ejercicio_11', '3')
def califica_ejercicio_11(f):
    return f

@template_iterable([
    [[3], [1, 2, 3]],
    [[5], [1, 2, 3, 4, 5]],
    [[0], []],
    [[-1], []]
], 'ejercicio_12', '3')
def califica_ejercicio_12(f):
    return f

@template_iterable([
    [[["a", "b", "c", "d", "e"], 1, 2], ["a", "b"]],
    [[["a", "b", "c", "d", "e"], 2, 2], ["c", "d"]],
    [[["a", "b", "c", "d", "e"], 3, 2], ["e"]],
    [[["a", "b", "c", "d", "e"], 4, 2], []]
], 'ejercicio_13', '3')
def califica_ejercicio_13(f):
    return f

@template_iterable([
    [[[100, 200, 50], 0.1], [90.0, 180.0, 45.0]],
    [[[10, 20], 0.5], [5.0, 10.0]],
    [[[], 0.1], []]
], 'ejercicio_14', '3')
def califica_ejercicio_14(f):
    return f

@template_iterable([
    [[["[INFO] OK", "[ERROR] DB fail", "[INFO] Job done"], "fail"], ["[ERROR] DB fail"]],
    [[["[INFO] OK", "[ERROR] DB fail", "[INFO] Job done"], "INFO"], ["[INFO] OK", "[INFO] Job done"]],
    [[["[INFO] OK", "[ERROR] DB fail", "[INFO] Job done"], "CORS"], []]
], 'ejercicio_15', '3')
def califica_ejercicio_15(f):
    return f


####################################################################################################
#                                       Tarea 4 (Listas y Tuplas)
####################################################################################################

@template_iterable([
    [[["task1", "task2"], "task3"], ["task1", "task2", "task3"]],
    [[[], "task1"], ["task1"]]
], 'ejercicio_16', '4')
def califica_ejercicio_16(f):
    return f

@template_iterable([
    [[["task1", "task2", "task3"]], ("task1", ["task2", "task3"])],
    [[["task1"]], ("task1", [])],
    [[[]], (None, [])]
], 'ejercicio_17', '4')
def califica_ejercicio_17(f):
    return f

@template_iterable([
    [[[4, 1, 2, 4, 3, 1]], [4, 1, 2, 3]],
    [[["a", "b", "a", "c"]], ["a", "b", "c"]],
    [[[]], []]
], 'ejercicio_18', '4')
def califica_ejercicio_18(f):
    return f

@template_iterable([
    [[[("Content-Type", "application/json"), ("Authorization", "Bearer token123")], "authorization"], "Bearer token123"],
    [[[("Content-Type", "application/json"), ("Authorization", "Bearer token123")], "content-type"], "application/json"],
    [[[("Content-Type", "application/json"), ("Authorization", "Bearer token123")], "host"], None]
], 'ejercicio_19', '4')
def califica_ejercicio_19(f):
    return f

@template_iterable([
    [[["Carlos", "Ana"], ["Beatriz", "Daniel"]], ["Ana", "Beatriz", "Carlos", "Daniel"]],
    [[[], ["A", "B"]], ["A", "B"]]
], 'ejercicio_20', '4')
def califica_ejercicio_20(f):
    return f


####################################################################################################
#                                       Tarea 5 (Diccionarios y Sets)
####################################################################################################

@template_iterable([
    [[{"username": "angel"}, "role", "guest"], "guest"],
    [[{"username": "angel", "role": "admin"}, "role", "guest"], "admin"]
], 'ejercicio_21', '5')
def califica_ejercicio_21(f):
    return f

@template_iterable([
    [[{"juan": "editor"}, {"editor": {"read", "edit"}}, "juan"], {"read", "edit"}],
    [[{"juan": "editor"}, {"editor": {"read", "edit"}}, "pedro"], set()],
    [[{"juan": "guest"}, {"editor": {"read", "edit"}}, "juan"], set()]
], 'ejercicio_22', '5')
def califica_ejercicio_22(f):
    return f

@template_iterable([
    [[[{"id": 101, "name": "A"}, {"id": 102, "name": "B"}]], {101: {"id": 101, "name": "A"}, 102: {"id": 102, "name": "B"}}],
    [[[]], {}]
], 'ejercicio_23', '5')
def califica_ejercicio_23(f):
    return f

# Para sets y lists, normalize a sets antes de comparar
def _eval_ejercicio_24(f):
    def wrapper(api, route):
        return f(api, route)
    return wrapper

@template_iterable([
    [[["read", "write", "delete"], ["read", "write"]], True],
    [[["read"], ["read", "write"]], False],
    [[set(), ["read"]], False],
    [[{"read"}, {"read"}], True]
], 'ejercicio_24', '5')
def califica_ejercicio_24(f):
    return _eval_ejercicio_24(f)

@template_iterable([
    [[{"id": 1, "desc": None, "price": 10}], {"id": 1, "price": 10}],
    [[{"name": None}], {}],
    [[{"a": 1, "b": 2}], {"a": 1, "b": 2}]
], 'ejercicio_25', '5')
def califica_ejercicio_25(f):
    return f


####################################################################################################
#                                       Tarea 6 (Funciones)
####################################################################################################

@template_iterable([
    [["angel"], {"username": "angel", "role": "guest"}],
    [["admin", "superuser"], {"username": "admin", "role": "superuser"}]
], 'ejercicio_26', '6')
def califica_ejercicio_26(f):
    return f

# Wrapper para ejercicio_27 ya que tiene argumentos kwargs variables
def _eval_ejercicio_27(f):
    def wrapper(base_url, query_params):
        return f(base_url, **query_params)
    return wrapper

@template_iterable([
    [["https://api.delfos.com/users", {"limit": 10, "page": 1}], "https://api.delfos.com/users?limit=10&page=1"],
    [["https://api.delfos.com/users", {"page": 2, "limit": 5}], "https://api.delfos.com/users?limit=5&page=2"],
    [["https://status.delfos.com", {}], "https://status.delfos.com"]
], 'ejercicio_27', '6')
def califica_ejercicio_27(f):
    return _eval_ejercicio_27(f)

# Wrapper para ejercicio_28 ya que tiene argumentos *args
def _eval_ejercicio_28(f):
    def wrapper(args_tuple):
        return f(*args_tuple)
    return wrapper

@template_iterable([
    [[("auth", "logger", "cors")], ["cors", "logger", "auth"]],
    [[("auth",)], ["auth"]],
    [[()], []]
], 'ejercicio_28', '6')
def califica_ejercicio_28(f):
    return _eval_ejercicio_28(f)

@template_iterable([
    [[lambda x: len(x) > 3, "abcd"], "Validated"],
    [[lambda x: x % 2 == 0, 4], "Validated"]
], 'ejercicio_29', '6')
def califica_ejercicio_29(f):
    return f

# Para el caso que levanta excepcion en ejercicio_29, hacemos test manual
def validador_ejercicio_29_excepcion(f):
    from models.resultado import Resultado
    try:
        f(lambda x: len(x) > 3, "abc")
        r = False
    except ValueError as e:
        r = (str(e) == "Invalid data")
    except Exception:
        r = False
    return [Resultado(["lambda x: len(x) > 3", "abc"], "ValueError('Invalid data')", "ValueError" if r else "Other", r).__dict__]

@template_custom(validador_ejercicio_29_excepcion, 'ejercicio_29', '6')
def califica_ejercicio_29_excepcion(f):
    return f

# Wrapper para ejercicio_30
def _eval_ejercicio_30(f):
    def wrapper(func, args_list, kwargs_dict):
        return f(func, *args_list, **kwargs_dict)
    return wrapper

@template_iterable([
    [[lambda x, y: x + y, (5, 10), {}], 15],
    [[lambda name, role: f"{name}-{role}", ("angel",), {"role": "admin"}], "angel-admin"]
], 'ejercicio_30', '6')
def califica_ejercicio_30(f):
    return _eval_ejercicio_30(f)


####################################################################################################
#                                       Tarea 7 (Manejo de Archivos)
####################################################################################################

def validador_ejercicio_31(f):
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write("[INFO] OK\n[ERROR] Falla en DB\n[WARNING] Alerta\n[ERROR] Falla en Auth\n")
        tmp_path = tmp.name
    try:
        res = f(tmp_path)
        estado = (res == 2)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    return [Resultado([tmp_path], 2, res, estado).__dict__]

@template_custom(validador_ejercicio_31, 'ejercicio_31', '7')
def califica_ejercicio_31(f):
    return f

def validador_ejercicio_32(f):
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write("Initial\n")
        tmp_path = tmp.name
    try:
        f(tmp_path, "[INFO] Hit")
        with open(tmp_path, 'r') as r:
            lines = r.readlines()
        estado = (len(lines) == 2 and lines[1] == "[INFO] Hit\n")
        res_obtenido = lines[1] if len(lines) > 1 else "".join(lines)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    return [Resultado([tmp_path, "[INFO] Hit"], "[INFO] Hit\n", res_obtenido, estado).__dict__]

@template_custom(validador_ejercicio_32, 'ejercicio_32', '7')
def califica_ejercicio_32(f):
    return f

def validador_ejercicio_33(f):
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write("# Config\n\nDB_HOST=localhost\nDB_PORT = 5432\n  # Comentario indentado\n")
        tmp_path = tmp.name
    try:
        res = f(tmp_path)
        esperado = {"DB_HOST": "localhost", "DB_PORT": "5432"}
        estado = (res == esperado)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    return [Resultado([tmp_path], esperado, res, estado).__dict__]

@template_custom(validador_ejercicio_33, 'ejercicio_33', '7')
def califica_ejercicio_33(f):
    return f

def validador_ejercicio_34(f):
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp_path = tmp.name
    try:
        data = {"host": "localhost", "port": "8000"}
        f(tmp_path, data)
        with open(tmp_path, 'r') as r:
            content = r.read().strip().split('\n')
        # Las lineas pueden estar en cualquier orden
        lineas_esperadas = {"host: localhost", "port: 8000"}
        lineas_obtenidas = {line.strip() for line in content}
        estado = (lineas_esperadas == lineas_obtenidas)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    return [Resultado([tmp_path, data], list(lineas_esperadas), list(lineas_obtenidas), estado).__dict__]

@template_custom(validador_ejercicio_34, 'ejercicio_34', '7')
def califica_ejercicio_34(f):
    return f

def validador_ejercicio_35(f):
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        tmp.write("id,nombre,rol\n1,Ana,admin\n2,Pedro,guest\n")
        tmp_path = tmp.name
    try:
        res = f(tmp_path)
        esperado = [{"id": "1", "nombre": "Ana", "rol": "admin"}, {"id": "2", "nombre": "Pedro", "rol": "guest"}]
        estado = (res == esperado)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    return [Resultado([tmp_path], esperado, res, estado).__dict__]

@template_custom(validador_ejercicio_35, 'ejercicio_35', '7')
def califica_ejercicio_35(f):
    return f


####################################################################################################
#                                       Tarea 8 (Excepciones)
####################################################################################################

@template_iterable([
    [[lambda: "ok"], "ok"],
    [[lambda: 1/0], "DATABASE_ERROR"],
    [[lambda: int("abc")], "DATABASE_ERROR"]
], 'ejercicio_36', '8')
def califica_ejercicio_36(f):
    return f

@template_iterable([
    [[lambda x: int(x), "123"], 123],
    [[lambda x: int(x), "abc"], {"error": "invalid_format"}],
    [[lambda x: x.split(), None], {"error": "invalid_format"}]
], 'ejercicio_37', '8')
def califica_ejercicio_37(f):
    return f

def validador_ejercicio_38(f):
    r1 = False
    try:
        res1 = f(10)
        if res1 == 10:
            r1 = True
    except Exception:
        r1 = False
    
    r2 = False
    try:
        f(-5)
    except ValueError as e:
        if str(e) == "Debe ser entero positivo":
            r2 = True
            
    r3 = False
    try:
        f("5")
    except ValueError as e:
        if str(e) == "Debe ser entero positivo":
            r3 = True

    return [
        Resultado([10], 10, 10 if r1 else None, r1).__dict__,
        Resultado([-5], "ValueError('Debe ser entero positivo')", "ValueError" if r2 else None, r2).__dict__,
        Resultado(["5"], "ValueError('Debe ser entero positivo')", "ValueError" if r3 else None, r3).__dict__
    ]

@template_custom(validador_ejercicio_38, 'ejercicio_38', '8')
def califica_ejercicio_38(f):
    return f

def validador_ejercicio_39(f):
    cleanup_called = False
    def cleanup():
        nonlocal cleanup_called
        cleanup_called = True

    # Caso exitoso
    res = f(lambda: 42, cleanup)
    r1 = (res == 42 and cleanup_called)

    # Caso con error
    cleanup_called = False
    r2 = False
    try:
        f(lambda: 1/0, cleanup)
    except ZeroDivisionError:
        r2 = cleanup_called
    except Exception:
        r2 = False

    return [
        Resultado(["db_func=lambda: 42"], "Result 42 + Cleanup=True", f"{res} + Cleanup={cleanup_called}", r1).__dict__,
        Resultado(["db_func=lambda: 1/0"], "ZeroDivisionError + Cleanup=True", f"ZeroDivisionError + Cleanup={cleanup_called}", r2).__dict__
    ]

@template_custom(validador_ejercicio_39, 'ejercicio_39', '8')
def califica_ejercicio_39(f):
    return f

def validador_ejercicio_40(f):
    r1 = False
    try:
        res1 = f({"email": "test@delfos.com", "username": "ana"})
        if res1 == "test@delfos.com":
            r1 = True
    except Exception:
        r1 = False

    r2 = False
    try:
        f({"username": "ana"})
    except Exception as e:
        if e.__class__.__name__ == "MissingEmailError":
            r2 = True

    return [
        Resultado([{"email": "test@delfos.com"}], "test@delfos.com", "test@delfos.com" if r1 else None, r1).__dict__,
        Resultado([{"username": "ana"}], "MissingEmailError", "MissingEmailError" if r2 else None, r2).__dict__
    ]

@template_custom(validador_ejercicio_40, 'ejercicio_40', '8')
def califica_ejercicio_40(f):
    return f


####################################################################################################
#                                       Tarea 9 (POO)
####################################################################################################

def validador_ejercicio_41(Usuario):
    u = Usuario("angel", "a@delfos.com")
    r1 = (u.username == "angel" and u.email == "a@delfos.com")
    d = u.to_dict()
    r2 = (d == {"username": "angel", "email": "a@delfos.com"})
    return [
        Resultado(["__init__"], True, r1, r1).__dict__,
        Resultado(["to_dict"], {"username": "angel", "email": "a@delfos.com"}, d, r2).__dict__
    ]

@template_custom(validador_ejercicio_41, 'ejercicio_41', '9')
def califica_ejercicio_41(f):
    return f

def validador_ejercicio_42(UsuarioVip):
    u = UsuarioVip("angel_vip", "vip@delfos.com", 0.15)
    r1 = (u.username == "angel_vip" and u.email == "vip@delfos.com" and u.descuento == 0.15)
    d = u.to_dict()
    r2 = (d == {"username": "angel_vip", "email": "vip@delfos.com", "descuento": 0.15})
    return [
        Resultado(["__init__"], True, r1, r1).__dict__,
        Resultado(["to_dict"], {"username": "angel_vip", "email": "vip@delfos.com", "descuento": 0.15}, d, r2).__dict__
    ]

@template_custom(validador_ejercicio_42, 'ejercicio_42', '9')
def califica_ejercicio_42(f):
    return f

def validador_ejercicio_43(BaseModel):
    db = []
    m = BaseModel(101)
    r1 = (m.id == 101)
    m.save(db)
    r2 = (db == [{"id": 101}])
    return [
        Resultado(["__init__"], 101, m.id if r1 else None, r1).__dict__,
        Resultado(["save"], [{"id": 101}], db, r2).__dict__
    ]

@template_custom(validador_ejercicio_43, 'ejercicio_43', '9')
def califica_ejercicio_43(f):
    return f

def validador_ejercicio_44(validate_user):
    r1 = False
    try:
        res1 = validate_user({"username": "ana"})
        if res1 is True:
            r1 = True
    except Exception:
        r1 = False

    r2 = False
    try:
        validate_user({"username": "al"})
    except Exception as e:
        if e.__class__.__name__ == "ValidationError" and str(e) == "Username invalido":
            r2 = True

    r3 = False
    try:
        validate_user({})
    except Exception as e:
        if e.__class__.__name__ == "ValidationError" and str(e) == "Username invalido":
            r3 = True

    return [
        Resultado([{"username": "ana"}], True, True if r1 else None, r1).__dict__,
        Resultado([{"username": "al"}], "ValidationError('Username invalido')", "ValidationError" if r2 else None, r2).__dict__,
        Resultado([{}], "ValidationError('Username invalido')", "ValidationError" if r3 else None, r3).__dict__
    ]

@template_custom(validador_ejercicio_44, 'ejercicio_44', '9')
def califica_ejercicio_44(f):
    return f

def validador_ejercicio_45(APIResponse):
    res1 = APIResponse(200, {"id": 1}, "Success")
    r1 = (res1.status_code == 200 and res1.data == {"id": 1} and res1.message == "Success")
    r2 = (res1.is_success() is True)
    
    res2 = APIResponse(400, {}, "Error")
    r3 = (res2.is_success() is False)
    
    res3 = APIResponse(299, [], "OK")
    r4 = (res3.is_success() is True)

    return [
        Resultado(["__init__"], True, r1, r1).__dict__,
        Resultado(["is_success 200"], True, res1.is_success(), r2).__dict__,
        Resultado(["is_success 400"], False, res2.is_success(), r3).__dict__,
        Resultado(["is_success 299"], True, res3.is_success(), r4).__dict__
    ]

@template_custom(validador_ejercicio_45, 'ejercicio_45', '9')
def califica_ejercicio_45(f):
    return f
