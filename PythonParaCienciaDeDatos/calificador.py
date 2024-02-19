from templates import template_iterable, template_poo, template_sencillo
import numpy as np

####################################################################################################
#                                       Tarea de prueba
####################################################################################################

@template_iterable([
    [[], np.zeros((1, 3))]
], 'ejercicio_0_1', '0')
def califica_ejercicio_0_1(f, uuid):
    return f

@template_iterable([
    [[], np.ones((3, 3))]
], 'ejercicio_0_2', '0')
def califica_ejercicio_0_2(f, uuid):
    return f

@template_iterable([
    [[], np.array([[13,  4, 52, 43, 42],
       [36, 44, 42, 98, 56]]) + 1]
], 'ejercicio_0_3', '0')
def califica_ejercicio_0_3(f, uuid):
    return f


####################################################################################################
#                                       Tarea 1
####################################################################################################


@template_iterable([
    [[], np.array([222,  98, 189])]
], 'ejercicio_4', '1')
def califica_ejercicio_4(f, uuid):
    return f

@template_iterable([
     [[], np.array(509)]
], 'ejercicio_5', '1')
def califica_ejercicio_5(f, uuid):
    return f

@template_iterable([
    [[[0, 1, 2, 3, 4, 5]], np.array([[0, 1, 2],
       [3, 4, 5]])],
    [[[47, 41, 68, 16, 96, 32]], np.array([[47, 41, 68],
       [16, 96, 32]])]
], 'ejercicio_6', '1')
def califica_ejercicio_6(f, uuid):
    return f

@template_iterable([
    [[[0, 1, 2]], np.array([1., 1., 1.])],
    [[[[1,2], [2,4]]], np.array([1., 1.])]
], 'ejercicio_7', '1')
def califica_ejercicio_7(f, uuid):
    return f

@template_iterable([
   [[[1,2]], np.array([1, 4])],
    [[[[1,2], [4,7]]], np.array([[ 1,  4],
       [16, 49]])]
], 'ejercicio_8', '1')
def califica_ejercicio_8(f, uuid):
    return f

@template_iterable([
    [[[[42, 19,  4],
 [67, 45, 94],
 [38, 24, 14]]], np.array([67, 45])]
], 'ejercicio_9', '1')
def califica_ejercicio_9(f, uuid):
    return f

@template_iterable([
    [[], np.ones((2,2)) *5]
], 'ejercicio_10', '1')
def califica_ejercicio_10(f, uuid):
    return f

@template_iterable([
    [[], np.arange(20, 40, 2)]
], 'ejercicio_11', '1')
def califica_ejercicio_11(f, uuid):
    return f

@template_iterable([
    [[[18, 16, 17, 19, 14]], np.array([1.8, 1.6, 1.7, 1.9, 1.4])]
], 'ejercicio_12', '1')
def califica_ejercicio_12(f, uuid):
    return f


####################################################################################################
#                                       Tarea 2.1
####################################################################################################

@template_iterable([
    [[[1,2,3]], np.array([[1],
       [2],
       [3]])]
], 'ejercicio_13', '1')
def califica_ejercicio_13(f, uuid):
    return f

@template_iterable([
    [[[1000,2000,3000]], np.array([1001, 2002, 3003])]
], 'ejercicio_14', '2')
def califica_ejercicio_14(f, uuid):
    return f

@template_iterable([
    [[[100,200,300,400,500,600,700,800,900]], np.array([[101, 202, 303],
       [401, 502, 603],
       [701, 802, 903]])]
], 'ejercicio_15', '2')
def califica_ejercicio_15(f, uuid):
    return f

@template_iterable([
    [[], np.array(4.5)]
], 'ejercicio_16', '2')
def califica_ejercicio_16(f, uuid):
    return f

@template_iterable([
    [[[[1,2,3],
    [3,4,5],
    [4,5,6]]], np.array([np.array([1, 2, 3]), np.array([4, 5, 6])])]
], 'ejercicio_17', '2')
def califica_ejercicio_17(f, uuid):
    return f

@template_iterable([
    [[[[1,2,3,4], [1,2,3,4]]], np.array([[-202.306, -204.612,  103.   ,  105.   ],
       [-202.306, -204.612,  103.   ,  105.   ]])],
    [[[[-8, 12,  3,  3, 14, 17,  1,  8],
       [12,  3,  7, 12,  2, -9, -5,  6]]], 
        np.array([[-181.552, -227.672, -206.918, -206.918,  116.   ,  120.   ,
                     101.   ,  109.   ],
                [-227.672, -206.918, -216.142, -227.672,  102.   ,   90.   ,
          94.   ,  107.   ]])],
    [[[[18,  1,  8, -5, -6],
       [10, 10, 15, -7,  9],
       [12, 12,  5, -5,  2],
       [-7, -5, -7,  4, -2]]], np.array([[-241.508, -202.306,  109.   ,   94.   ,   93.   ],
       [-223.06 , -223.06 ,  117.   ,   92.   ,  110.   ],
       [-227.672, -227.672,  106.   ,   94.   ,  102.   ],
       [-183.858, -188.47 ,   92.   ,  105.   ,   98.   ]])]
], 'ejercicio_18', '2')
def califica_ejercicio_18(f, uuid):
    return f

@template_iterable([
    [[[1,2,3]], np.array([[1.    , 2.    , 3.    ],
       [3.1416, 6.2832, 9.4248],
       [1.    , 4.    , 9.    ],
       [1.    , 1.41  , 1.73  ]])],
    [[[3,4,5]], np.array([[ 3.    ,  4.    ,  5.    ],
       [ 9.4248, 12.5664, 15.708 ],
       [ 9.    , 16.    , 25.    ],
       [ 1.73  ,  2.    ,  2.24  ]])],
    [[[6,7,8]], np.array([[ 6.    ,  7.    ,  8.    ],
       [18.8496, 21.9912, 25.1328],
       [36.    , 49.    , 64.    ],
       [ 2.45  ,  2.65  ,  2.83  ]])]
], 'ejercicio_19', '2')
def califica_ejercicio_19(f, uuid):
    return f

@template_iterable([
    [[[1,2,3], [2,2,2]], np.array([2, 4, 6])],
    [[[4,1,5], [1,4,3]], np.array([ 4,  4, 15])],
    [[[31,12,30], [3,20,10]], np.array([ 93, 240, 300])]
], 'ejercicio_20', '2')
def califica_ejercicio_20(f, uuid):
    return f

@template_iterable([
    [[[[10, 18],
        [14, 10]], [[19, 12],
        [14, 15]]], np.array([[442, 390],
       [406, 318]])],
    [[[[15, 17, 18],
 [17, 11, 19],
 [17, 19, 14]], [[14, 16, 17],
 [14, 17, 15],
 [11, 10, 18]]], np.array([[646, 709, 834],
       [601, 649, 796],
       [658, 735, 826]])],
    [[[18, 19, 17], [[16],
 [12],
 [12]]], np.array([720])]
], 'ejercicio_21', '2')
def califica_ejercicio_21(f, uuid):
    return f

@template_iterable([
    [[[1,2,3], .1, 3], np.array([0.729, 1.458, 2.187])],
    [[[[3,3,3], [1,1,1]], .3, 5], np.array([[0.50421, 0.50421, 0.50421],
       [0.16807, 0.16807, 0.16807]])],
    [[[[1,2,3], [4,5,6]], .2, 4], np.array([[0.4096, 0.8192, 1.2288],
       [1.6384, 2.048 , 2.4576]])]
], 'ejercicio_22', '2')
def califica_ejercicio_22(f, uuid):
    return f

####################################################################################################
#                                       Tarea 3.1
####################################################################################################



@template_iterable([
    [[45], 1.0],
    [[135], -1.0],
    [[225], 0.0],
    [[250], 2.75],
    [[360], -0.0],
], 'ejercico_23', '3')
def califica_ejercicio_23(f, uuid):
    return f

@template_iterable([
    [[10], 2.3],
    [[100], 4.61],
    [[1000], 6.91],
    [[10000], 9.21],
    [[100000], 11.51],
], 'ejercico_24', '3')
def califica_ejercicio_24(f, uuid):
    return f

@template_iterable([
    [[20], 4.32],
    [[200], 7.64],
    [[2000], 10.97],
    [[20000], 14.29],
    [[200000], 17.61],
], 'ejercico_25', '3')
def califica_ejercicio_25(f, uuid):
    return f

@template_iterable([
    [[-2], 0.14],
    [[-.25], 0.78],
    [[1], 2.72],
    [[10], 22026.47],
    [[-10], 0.0],
], 'ejercico_26', '3')
def califica_ejercicio_26(f, uuid):
    return f

@template_iterable([
    [[-3], 0.12],
    [[3], 8.0],
    [[30], 1073741824.0],
    [[.5], 1.41],
    [[-.5], 0.71],
], 'ejercico_27', '3')
def califica_ejercicio_27(f, uuid):
    return f

@template_iterable([
    [[10], 3628800],
    [[9], 362880],
    [[8], 40320],
    [[7], 5040],
    [[6], 720],
], 'ejercico_28', '3')
def califica_ejercicio_28(f, uuid):
    return f

@template_iterable([
    [[16], 4.0],
    [[32], 5.66],
    [[100], 10.0],
    [[121], 121],
    [[356], 18.87],
], 'ejercico_29', '3')
def califica_ejercicio_29(f, uuid):
    return f

@template_iterable([
    [[4, 6], 12],
    [[180, 324], 1620],
    [[12, 8], 24],
    [[20, 38], 380],
    [[34, 18], 306],
], 'ejercico_30', '3')
def califica_ejercicio_30(f, uuid):
    return f

####################################################################################################
#                                       Tarea 4.1
####################################################################################################

@template_iterable([
    [["asdASDASdasAS"], 'asdasdasdasas'],
    [["HOLA MUNDO"], 'hola mundo'],
    [["México Lindo Y Querido"], 'méxico lindo y querido'],
    [["TURURÚ"], 'tururú']
], 'ejercicio_31', '4')
def califica_ejercicio_31(f, uuid):
    return f

@template_iterable([
    [["a W sD W q Q s D"], 'A W SD W Q Q S D'],
    [["dhs JDJD sosks K K kj"], 'DHS JDJD SOSKS K K KJ'],
    [["En un lugar de La Mancha"], 'EN UN LUGAR DE LA MANCHA'],
    [['tururú'], "TURURÚ"]
], 'ejercicio_32', '4')
def califica_ejercicio_32(f, uuid):
    return f

@template_iterable([
    [["Aloho mora", "a"], 9],
    [["Pingüinos azules", " "], 9],
    [["Pepe pecas pica papas", "P"], 0],
    [["Con un pico", "u"], 4]
], 'ejercicio_33', '4')
def califica_ejercicio_33(f, uuid):
    return f

@template_iterable([
    [["Alberto"], 'Saludos: Alberto'],
    [["Máximo Décimo Meridio"], 'Saludos: Máximo Décimo Meridio'],
    [["Sáncho Panza"], 'Saludos: Sáncho Panza'],
    [["Darth Vader"], 'Saludos: Darth Vader']
], 'ejercicio_34', '4')
def califica_ejercicio_34(f, uuid):
    return f

@template_iterable([
    [["200000"], "El tipo de dato de la variable es: <class 'str'>"],
    [[1.2], "El tipo de dato de la variable es: <class 'float'>"],
    [[234], "El tipo de dato de la variable es: <class 'int'>"],
    [[[234]], "El tipo de dato de la variable es: <class 'list'>"]
], 'ejercicio_35', '4')
def califica_ejercicio_35(f, uuid):
    return f

@template_iterable([
    [["Rusa", 25, 1.5], 'Usuario de: Rusa con edad 25 y estatura 1.5'],
    [["Peruana", 35, 2.0], 'Usuario de: Peruana con edad 35 y estatura 2.0'],
    [["Austriaca", 18, 1.83], 'Usuario de: Austriaca con edad 18 y estatura 1.83'],
    [["Francesa", 55, 1.55], 'Usuario de: Francesa con edad 55 y estatura 1.55']
], 'ejercicio_36', '4')
def califica_ejercicio_36(f, uuid):
    return f

@template_iterable([
    [["PEPE@gmail.com "], 'pepe@gmail.com'],
    [["TOÑO@HOTMAIL.COM"], 'toño@hotmail.com'],
    [["       JONHSMITH@outlook.COM"], 'jonhsmith@outlook.com'],
    [["janedoe@HOTMAIL.COM"], 'janedoe@hotmail.com']
], 'ejercicio_37', '4')
def califica_ejercicio_37(f, uuid):
    return f

@template_iterable([
    [["Tururú", "u", "o"], 'tororú'],
    [["Pepe Pecas Pica Papas", "p", "w"], 'wewe wecas wica wawas'],
    [["AEIOU", "a", "r"], 'reiou'],
    [["ée", "e", "q"], 'éq']
], 'ejercicio_38', '4')
def califica_ejercicio_38(f, uuid):
    return f

@template_iterable([
    [["ESTANDARIZACIÓN"], 'estandarizacion'],
    [["ÁÉÍÓÚ"], 'aeiou'],
    [["áéíóú"], 'aeiou'],
    [["Papá"], 'papa']
], 'ejercicio_39', '4')
def califica_ejercicio_39(f, uuid):
    return f

@template_iterable([
    [["  Juan_PÉREZ@hotmail.com "], 'juan_perez@hotmail.com'],
    [["ESTUDIANTE@GMMAIL.COM"], 'estudiante@gmail.com'],
    [[" pepePECASpicaPAPAS@GMAIL.COM "], 'pepepecaspicapapas@gmail.com'],
    [[" sábadoFELÍz@HOTMAIL.COM "], 'sabadofeliz@hotmail.com']
], 'ejercicio_40', '4')
def califica_ejercicio_40(f, uuid):
    return f


####################################################################################################
#                                       Tarea 5.1
####################################################################################################

@template_iterable([
    [[3.4], 3],
    [["2"], 2],
    [[-3.2], -3],
    [["3"], 3]
], 'ejercicio_41', '5')
def califica_ejercicio_41(f, uuid):
    return f

@template_iterable([
    [[3], 3.0],
    [[1.2], 1.2],
    [["2.2"], 2.2],
    [[-3.19], -3.19]
], 'ejercicio_42', '5')
def califica_ejercicio_42(f, uuid):
    return f

@template_iterable([
    [["Hola"], 'Hola'],
    [[1.2], "1.2"],
    [["2.2"], "2.2"],
    [[-3.19], "-3.19"]
], 'ejercicio_43', '5')
def califica_ejercicio_43(f, uuid):
    return f

@template_iterable([
    [["4"], 8686868686],
    [[2], 4646464646],
    [[202], 40464046404640464046],
    [[81], 1627627627627626]
], 'ejercicio_44', '5')
def califica_ejercicio_44(f, uuid):
    return f

@template_iterable([
    [[1234], "2323"],
    [[22323], "2323"],
    [[1543], "5454545454"],
    [[321543], "2121"]
], 'ejercicio_45', '5')
def califica_ejercicio_45(f, uuid):
    return f

@template_iterable([
    [[2342], 4],
    [[1111111], 7],
    [[1], 1],
    [[321543], 6]
], 'ejercicio_46', '5')
def califica_ejercicio_46(f, uuid):
    return f

@template_iterable([
    [[2], '$2.00'],
    [[123456789], '$123,456,789.00'],
    [[1000000], '$1,000,000.00'],
    [[-10101], '$-10,101.00']
], 'ejercicio_47', '5')
def califica_ejercicio_47(f, uuid):
    return f

@template_iterable([
    [["E", -20], '1'],
    [["9", 4], '='],
    [["ñ", 10], 'û'],
    [["A", -5], '<']
], 'ejercicio_48', '5')
def califica_ejercicio_48(f, uuid):
    return f

@template_iterable([
    [[21211, 0], 4827],
    [[100, 0], 36],
    [[3121212, 0], 1024060],
    [[10, 0], 2]
], 'ejercicio_49', '5')
def califica_ejercicio_49(f, uuid):
    return f

@template_iterable([
    [[0], '0'],
    [[10], 'a'],
    [[57894], 'e226'],
    [[-962093], '-eae2d']
], 'ejercicio_50', '5')
def califica_ejercicio_50(f, uuid):
    return f

####################################################################################################
#                                       Tarea 6.1
####################################################################################################

@template_iterable([
    [["Hola", "Hola"], "Son iguales"],
    [['Hola', 'Hola'], "Son iguales"],
    [["Hola", "hola"], "Son diferentes"],
    [["Mi nombre es:", "Mi nombre es"], "Son diferentes"],
    [["Tengo ... años", "Tengo --- años"], "Son diferentes"],
], 'ejercicio_51', '6')
def califica_ejercicio_51(f, uuid):
    return f

@template_iterable([
    [[2], True],
    [[201], False],
    [[3333], False],
    [[1234], True],
    [[209872], True],
], 'ejercicio_52', '6')
def califica_ejercicio_52(f, uuid):
    return f

@template_iterable([
    [[17], "Eres menor de edad"],
    [[18], "Eres mayor de edad"],
    [[12], "Eres menor de edad"],
    [[81], "Eres mayor de edad"],
    [[99], "Eres mayor de edad"],
], 'ejercicio_53', '6')
def califica_ejercicio_53(f, uuid):
    return f

@template_iterable([
    [[2,2], 1.0],
    [[4,2], 2.0],
    [[10,5], 2.0],
    [[23,0], "No puedo dividir entre cero"],
    [[1567,0], "No puedo dividir entre cero"],
], 'ejercicio_54', '6')
def califica_ejercicio_54(f, uuid):
    return f

@template_iterable([
    [[3,2], "El primero es mayor"],
    [[29834,209], "El primero es mayor"],
    [[1,2], "El segundo es mayor"],
    [[89,89], "Son iguales"],
    [[2,2], "Son iguales"],
], 'ejercicio_55', '6')
def califica_ejercicio_55(f, uuid):
    return f

@template_iterable([
    [[21], "Pertenece"],
    [[30], "Pertenece"],
    [[20], "No pertenece"],
    [[16], "No pertenece"],
    [[28], "Pertenece"],
], 'ejercicio_56', '6')
def califica_ejercicio_56(f, uuid):
    return f

@template_iterable([
    [[10000, 'Educación'], '8%'],
    [[15000, 'Educación'], '10%'],
    [[25000, 'Educación'], '10%'],
    [[10000, 'Ganadería'], '8%'],
    [[15000, 'Ganadería'], '10%'],
    [[25000, 'Ganadería'], '10%'],
    [[10000, 'Textiles'], '12%'],
    [[15000, 'Textiles'], '14%'],
    [[25000, 'Textiles'], '14%'],
    [[10000, 'Tecnología'], '12%'],
    [[15000, 'Tecnología'], '14%'],
    [[25000, 'Tecnología'], '14%'],
], 'ejercicio_57', '6')
def califica_ejercicio_57(f, uuid):
    return f

@template_iterable([
    [[5.5], 'Pasaste'],
    [[5.6], 'Pasaste'],
    [[10], 'Pasaste'],
    [[4.6], 'Prueba de nuevo'],
    [[5.4], 'Prueba de nuevo'],
], 'ejercicio_58', '6')
def califica_ejercicio_58(f, uuid):
    return f

@template_iterable([
    [[1.40], "Puede subir :D"],
    [[1.23], "No puede subir :("],
    [[1.80], "Puede subir :D"]
], 'ejercicio_59', '6')
def califica_ejercicio_59(f, uuid):
    return f

@template_iterable([
    [[1,2,3], "Escaleno"],
    [[3,3,3], "Equilátero"],
    [[1,2,2], "Isósceles"],
], 'ejercicio_60', '6')
def califica_ejercicio_60(f, uuid):
    return f

####################################################################################################
#                                       Tarea 7.1
####################################################################################################

@template_iterable([
    [[], []]
], 'ejercicio_61', '7')
def califica_ejercicio_61(f, uuid):
    return f

@template_iterable([
    [[], ()]
], 'ejercicio_62', '7')
def califica_ejercicio_62(f, uuid):
    return f

@template_iterable([
    [[], {}]
], 'ejercicio_63', '7')
def califica_ejercicio_63(f, uuid):
    return f

@template_iterable([
        ([[]], 0),
        ([[1,2,3]], 3),
        ([[1,2,3,4,5,6,7,8,9,10]], 10),
        ([list(range(100))], 100)
    ], 'ejercicio_64', '7')
def califica_ejercicio_64(f, uuid):
    return f

@template_iterable([
        ([()], 0),
        ([(1,2,3)], 3),
        ([(1,2,3,4,5,6,7,8,9,10)], 10),
        ([tuple(range(100))], 100)
    ], 'ejercicio_65', '7')
def califica_ejercicio_65(f, uuid):
    return 

@template_iterable([
        ([{}], 0),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], 3),
        ([{"Dia": "Martes"}], 1),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], 2)
    ], 'ejercicio_66', '7')
def califica_ejercicio_66(f, uuid):
    return f

@template_iterable([
        ([1], [1]),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], [{"Uno": 1,"Dos": 2, "Tres": 3}]),
        ([{"Dia": "Martes"}], [{"Dia": "Martes"}]),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], [{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}])
    ], 'ejercicio_67', '7')
def califica_ejercicio_67(f, uuid):
    return f

@template_iterable([
        ([1], (1,)),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], ({"Uno": 1,"Dos": 2, "Tres": 3},)),
        ([{"Dia": "Martes"}], ({"Dia": "Martes"},)),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], ({"Curso": "Python de la a a la z", "Fecha": "17 de enero"},))
    ], 'ejercicio_68', '7')
def califica_ejercicio_68(f, uuid):
    return f

@template_iterable([
        ([27], {'edad': 27}), 
        ([60], {'edad': 60}) 
    ], 'ejercicio_69', '7')
def califica_ejercicio_69(f, uuid):
    return f

@template_iterable([
        ([], ['a', 'b', 'c'])
    ], 'ejercicio_70', '7')
def califica_ejercicio_70(f, uuid):
    return f

####################################################################################################
#                                       Tarea 8.1
####################################################################################################


@template_iterable([
        ([], ('a', '1', 'b'))
    ], 'ejercicio_71', '8')
def califica_ejercicio_71(f, uuid):
    return f

@template_iterable([
    [[[1,2,3,4,5,6]], 6],
    [[['a', 'b', 'c', 'd', 'e', 'f']], 'f'],
    [[[10, 11, 12, 13, 14, 15, 16, 17]], 15]
], 'ejercicio_72', '8')
def califica_ejercicio_72(f, uuid):
    return f

@template_iterable([
            [[27], 26], 
            [[60], 59],
            [[101], 100],
        ], 'ejercicio_73', '8')
def califica_ejercicio_73(f, uuid):
        return f

@template_iterable([[[], {
    'estado': 'Activo',
    'datos': {
        'curso': 'Python básico',
        'tareas': 3
    }
}]], 'ejercicio_74', '8')
def califica_ejercicio_74(f, uuid):
    return f

@template_iterable([[[], [
    {"pais": "México", "nombre oficial": "Estados Unidos Mexicanos"},
    {"pais": "Estados Unidos", "nombre oficial": "Estados Unidos de América"}
]]], 'ejercicio_75', '8')
def califica_ejercicio_75(f, uuid):
    return f

@template_iterable([[[], {
        "tarea1": [
            10, 10, 8
        ],
        "tarea2": [
            10, 8, 7
        ]
    }]], 'ejercicio_76', '8')
def califica_ejercicio_76(f, uuid):
    return f

@template_iterable([[[], {
        "historial": ((3,5,1,6), (56,2,1,7), (62,4,78,3))
    }]], 'ejercicio_77', '8')
def califica_ejercicio_77(f, uuid):
    return f

@template_iterable([
    [['edad', 27], {'edad': 27}],
    [['Nombre', "Pepito"], {'Nombre': 'Pepito'}],
    [[1, 27], {1: 27}],
    [["Calif", 100], {'Calif': 100}],
], 'ejercicio_78', '8')
def califica_ejercicio_78(f, uuid):
    return f

@template_iterable([[
    [], list(range(10001))
]], 'ejercicio_79', '8')
def califica_ejercicio_79(f, uuid):
    return f

@template_iterable([
    [[10], list(range(10))],
    [[100], list(range(100))],
    [[110], list(range(110))],
    [[2], list(range(2))],
    [[3], list(range(3))],
], 'ejercicio_80', '8')
def califica_ejercicio_80(f, uuid):
    return f

####################################################################################################
#                                       Tarea 9.1
####################################################################################################


@template_iterable([
    [[[1,2,3]], 6],
    [[[10, 20, 30]], 60],
    [[[9,8,7]], 24]
], 'ejercicio_81', '9')
def califica_ejercicio_81(f, uuid):
    return f

@template_iterable([
    [[[17, 18, 12, 12, 17]], 749088],
    [[[105, 148, 111, 143, 113]], 27873305460],
    [[[82, 56, 37, 153, 123]], 3197423376]
], 'ejercicio_82', '9')
def califica_ejercicio_82(f, uuid):
    return f

@template_iterable([
    [[["abecedario", "tacos", "enchiladas", "sal"]], ('abecedario', 'tacos', 'enchiladas')]
], 'ejercicio_83', '9')
def califica_ejercicio_83(f, uuid):
    return f

@template_iterable([
    [[10], 3628800],
    [[11], 39916800],
    [[12], 479001600],
], 'ejercicio_84', '9')
def califica_ejercicio_84(f, uuid):
    return f

@template_iterable([
    [[110], 3025],
    [[123], 3844],
    [[254], 16129],
], 'ejercicio_85', '9')
def califica_ejercicio_85(f, uuid):
    return f

@template_iterable([
    [[[3,7,5,1], 7], 1],
    [[[3,7,5,1], 1], 3],
    [[[3,7,5,1], 3], 0],
], 'ejercicio_86', '9')
def califica_ejercicio_86(f, uuid):
    return f

@template_iterable([
    [[[("tacos", 300), ("enchiladas", 200), ("sopes", 150)]], 650],
    [[[("Macbook Pro", 50), ("Macbook Air", 200), ("IPhone", 1000)]], 1250],
    [[[("Asus ROG", 5), ("Black Shark 4 Pro", 2), ("Realme GT Neo", 3), ("Nubia Red Magic 6", 4), ("Lenovo Legion Phone Duel 2", 1)]], 15],
    [[[("Sony MDR", 28), ("Cheelom", 34), ("Dinden", 3)]], 65],
    [[[("XYZ", 278), ("AYX", 312), ("KJO", 123)]], 713],
], 'ejercicio_87', '9')
def califica_ejercicio_87(f, uuid):
    return f

@template_iterable([
    [[{"comida": "enchiladas", "Aguacate": "Verde", "agua": "Salada", "espinaca": "verdura"}], {"Aguacate": "Verde", "agua": "Salada"}],
    [[{"automatico": "Vehículo", "standard": "Carro"}], {"automatico": "Vehículo"}]
], 'ejercicio_88', '9')
def califica_ejercicio_88(f, uuid):
    return f

@template_iterable([
    [[[[1,2,3],[5,6,7],[7,8,9]]], [6, 18, 24]],
    [[[[-31,24,-3],[-35,-61,47],[47,2,90]]], [-10, -49, 139]],
    [[[[-1,-4,-5,3],[-5,-1,4],[47,2,90],[5,-7,-1,-5,-8],[1,2], [8,7,5]]], [-7, -2, 139, -16, 3, 20]]
], 'ejercicio_89', '9')
def califica_ejercicio_89(f, uuid):
    return f

@template_iterable([
    [[{"ola": "Del mar", "hola": [1,2,3], "curso": "Python", "ZDRF": [3,4,5]}], ([6, 12], ['Python'])],
    [[{"RDF": [7,9,-1], "DCA": "Hola mundo", "SWECD": "Analitica", "QWSDE": "Delfos"}], ([15], ['Analitica', 'Delfos'])]
], 'ejercicio_90', '9')
def califica_ejercicio_90(f, uuid):
    return f

####################################################################################################
#                                       Tarea 10.1
####################################################################################################

@template_iterable([
    [[10, 20], [10, 12, 14, 16, 18, 20]],
    [[100, 200], [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]],
    [[1, 2], [2]],
    [[2, 4], [2, 4]],
    [[3, 100], [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]],
], 'ejercicio_91', '10')
def califica_ejercicio_91(f, uuid):
    return f

@template_iterable([
    [[[1,2,3,4,5,6,7,8,9,10]], [5,10]],
    [[[10, 20, 30, 40, 50]], [10, 20, 30, 40, 50]],
    [[[1]], []],
    [[[33,44,55,66,77,88,99]], [55]],
    [[[101, 105, 104, 100]], [105, 100]],
], 'ejercicio_92', '10')
def califica_ejercicio_92(f, uuid):
    return f

@template_iterable([
    [["ae22"], (2,2)],
    [["1bq22"], (0,3)],
    [["aeiou"], (5,0)],
    [["12345"], (0,5)],
    [["12345aeiou"], (5,5)],
], 'ejercicio_93', '10')
def califica_ejercicio_93(f, uuid):
    return f

@template_iterable([
    [[{"alumnos": [10, 10]}], 10],
    [[{"alumnos": [5, 10]}], 7.5],
    [[{"alumnos": [5, 10, 5, 10]}], 7.5],
    [[{"alumnos": [8, 7, 6, 5, 10]}], 7.2],
    [[{"alumnos": [2, .5, 10, 10, 10]}], 6.5],
], 'ejercicio_94', '10')
def califica_ejercicio_94(f, uuid):
    return f

@template_iterable([
    [[[1,2,3,4,3], 3], 2],
    [[[3,2,3,3,3], 3], 4],
    [[[3,2,8,3,7], 7], 1],
    [[[3,8,8,3,7], 8], 2],
], 'ejercicio_95', '10')
def califica_ejercicio_95(f, uuid):
    return f

@template_iterable([
    [[["Hola", "Hola", "Adios"]], {"Hola": 2, "Adios": 1}],
    [[["Manzana", "Plátano", "Manzana", "Fresa", "Fresa"]], {"Manzana": 2, "Plátano": 1, "Fresa": 2}],
    [[["Manzana", "Manzana", "Manzana", "Manzana", "Fresa"]], {"Manzana": 4, "Fresa": 1}],
    [[["Python", "C++", "Python", "C++"]], {"Python": 2, "C++": 2}],
], 'ejercicio_96', '10')
def califica_ejercicio_96(f, uuid):
    return f

@template_iterable([
    [[[1,2,3], [2,3,4]], [2,3]],
    [[[2,2,2,2,2], [2,2,2,2,2,4]], [2]],
    [[[-1,-2,-3], [-3,-2,-4]], [-2,-3]],
    [[[-10,20,-30], [10,20,30]], [20]],
], 'ejercicio_97', '10')
def califica_ejercicio_97(f, uuid):
    return f

@template_iterable([
    [[{"manzanas": 3, "platanos": 2}], 5],
    [[{"tacos": 2, "sopes": 5, "tortas": 10}], 17],
    [[{"playeras": 5, "pantalones": 5, "chamarras": 5}], 15],
], 'ejercicio_98', '10')
def califica_ejercicio_98(f, uuid):
    return f

@template_iterable([
    [[["Hola", ["Hola", "Adios"], 3, (19,), 5, 8]], (8,)],
    [[["8", ["8"], 8, (1,), 8]], (8,)],
    [[[6, 4, 9, 3, -8, 9]], (6,9)],
], 'ejercicio_99', '10')
def califica_ejercicio_99(f, uuid):
    return f

@template_iterable([
    [[3], """***
***
***"""],
[[4], """****
****
****
****"""]
], 'ejercicio_100', '10')
def califica_ejercicio_100(f, uuid):
    return f

@template_iterable([
    [[3.5, 1], 3.5],
    [[100.9, 1], 100.9],
    [[-3.689, 2], -3.69]
], 'redondear_a_n_digitos', '1')
def califica_redondear_a_n_digitos(f, uuid):
    return f

@template_iterable([
    [[6,3], 0],
    [[1,3], 1],
    [[100,67], 33],
    [[23,5], 3]
], 'modulo', '1')
def califica_modulo(f, uuid):
    return f

@template_iterable([
    [[100, 10], 10.0],
    [[1010, 10], 101.0],
    [[34, 34], 1.0],
    [[-6, 4], -2],
    [[.5, 1], 0.0],
], 'división_entera', '1')
def califica_division_entera(f, uuid):
    return f

@template_sencillo("HOLA, MUNDO", "en_mayusculas", '1', ["hola, mundo"])
def califica_en_mayusculas(f, uuid):
    return f

@template_sencillo("hola, mundo", 'en_minusculas', '1', ["HOLA, MUNDO"])
def califica_en_minusculas(f, uuid):
    return f


####################################################################################################
#                                       Tarea 2
####################################################################################################

@template_iterable([
        [["Hola"], 'H'],
        [["mundo",], 'm'],
        [["me"], 'm'],
        [["gusta"], 'g'],
        [["este"], 'e'],
        [["curso"], 'c'],
        [["y las"], 'y'],
        [["'t2-'s"], '\''],
        [["están"], 'e'],
        [["geniales"], 'g']
    ], 'primer_caracter', '2')
def califica_primer_caracter(f, uuid):
    return f

@template_iterable([
        [["Esta",], 't'],
        [["'t2-'",], '-'],
        [["está",], 't'],
        [["curiosa",], 's'],
        [["eso de",], 'd'],
        [["usar",], 'a'],
        [["índices",], 'e'],
        [["negativos",], 'o'],
        [["es",], 'e'],
        [["nuevo",], 'v']
    ], 'penultimo_caracter', '2')
def califica_penultimo_caracter(f, uuid):
    return f

@template_iterable([
        [[1,2,3], "a = 1, b = 2 y c = 3"],
        [[4,5,6], "a = 4, b = 5 y c = 6"],
        [[7,8,9], "a = 7, b = 8 y c = 9"],
        [[10, 11, 12], "a = 10, b = 11 y c = 12"],
        [[13, 14, 15], "a = 13, b = 14 y c = 15"]
    ], 'mostrar_numeros', '2')
def califica_mostrar_numeros(f, uuid):
    return f

@template_iterable([
        [["Hola, ", "mundo"], 'Hola, mundo'],
        [["Estoy ", "aprendiendo"], "Estoy aprendiendo"],
        [["a ", "programar"], 'a programar'],
        [["en ", "Python"], 'en Python']
    ], 'concatenar_cadenas', '2')
def califica_concatenar_cadenas(f, uuid):
    return f

@template_iterable([
    [[10], 98.10000000000001],
    [[34], 333.54],
    [[54], 529.74],
    [[98], 961.38],
    [[8.3], 81.42300000000002],
], 'peso_de_un_cuerpo', '2')
def califica_peso_de_un_cuerpo(f, uuid):
    return f

@template_iterable([
    [[30, 25], 1.2],
    [[456, 234], 1.9487179487179487],
    [[89, 23], 3.869565217391304],
    [[1567, 1268], 1.2358044164037856],
    [[45, 87], 0.5172413793103449],
], 'calculo_de_velocidad_constante', '2')
def califica_calculo_de_velocidad_constante(f, uuid):
    return f

@template_iterable([
    [[30, 30, 100], 3030],
    [[20, 10, 130], 1320],
    [[45, 89, 78], 6987],
    [[487, 65, 10], 1137],
    [[1000, 10, 10], 1100],
], 'calculo_de_velocidad_con_aceleracion', '2')
def califica_calculo_de_velocidad_con_aceleracion(f, uuid):
    return f



@template_iterable([
    [[50.0, 1.60, 110.0, 1.90, 80.0, 1.50], 28.51923989432646],
    [[55.0, 1.50, 130.0, 1.60, 85.0, 1.55], 36.86850237985123],
    [[65.0, 1.65, 150.0, 1.50, 83.0, 1.62], 40.722685977705304],
    [[30.0, 1.30, 87.0, 1.80, 40.0, 1.32], 22.52005742681733],
    [[85.0, 1.80, 67.0, 1.40, 80.0, 1.56], 31.097117055603018],
], 'promedio_inidice_masa_corporal', '2')
def califica_promedio_inidice_masa_corporal(f, uuid):
    return f

####################################################################################################
#                                       Tarea 3
####################################################################################################

@template_iterable([
    [["Hola", "Hola"], "Son iguales"],
    [['Hola', 'Hola'], "Son iguales"],
    [["Hola", "hola"], "Son diferentes"],
    [["Mi nombre es:", "Mi nombre es"], "Son diferentes"],
    [["Tengo ... años", "Tengo --- años"], "Son diferentes"],
], 'son_iguales', '3')
def califica_son_iguales(f, uuid):
    return f

@template_iterable([
    [[2], True],
    [[201], False],
    [[3333], False],
    [[1234], True],
    [[209872], True],
], 'es_par', '3')
def califica_es_par(f, uuid):
    return f

@template_iterable([
    [[17], "Eres menor de edad"],
    [[18], "Eres mayor de edad"],
    [[12], "Eres menor de edad"],
    [[81], "Eres mayor de edad"],
    [[99], "Eres mayor de edad"],
], 'mayor_de_edad', '3')
def califica_mayor_de_edad(f, uuid):
    return f

@template_iterable([
    [[2,2], 1.0],
    [[4,2], 2.0],
    [[10,5], 2.0],
    [[23,0], "No puedo dividir entre cero"],
    [[1567,0], "No puedo dividir entre cero"],
], 'division_cuidadosa', '3')
def califica_division_cuidadosa(f, uuid):
    return f

@template_iterable([
    [[3,2], "El primero es mayor"],
    [[29834,209], "El primero es mayor"],
    [[1,2], "El segundo es mayor"],
    [[89,89], "Son iguales"],
    [[2,2], "Son iguales"],
], 'es_mayor', '3')
def califica_es_mayor(f, uuid):
    return f

@template_iterable([
    [[21], "Pertenece"],
    [[30], "Pertenece"],
    [[20], "No pertenece"],
    [[16], "No pertenece"],
    [[28], "Pertenece"],
], 'en_medio', '3')
def califica_en_medio(f, uuid):
    return f

@template_iterable([
    [[10000, 'Educación'], '8%'],
    [[15000, 'Educación'], '10%'],
    [[25000, 'Educación'], '10%'],
    [[10000, 'Ganadería'], '8%'],
    [[15000, 'Ganadería'], '10%'],
    [[25000, 'Ganadería'], '10%'],
    [[10000, 'Textiles'], '12%'],
    [[15000, 'Textiles'], '14%'],
    [[25000, 'Textiles'], '14%'],
    [[10000, 'Tecnología'], '12%'],
    [[15000, 'Tecnología'], '14%'],
    [[25000, 'Tecnología'], '14%'],
], 'impuestos', '3')
def califica_impuestos(f, uuid):
    return f

@template_iterable([
    [[5.5], 'Pasaste'],
    [[5.6], 'Pasaste'],
    [[10], 'Pasaste'],
    [[4.6], 'Prueba de nuevo'],
    [[5.4], 'Prueba de nuevo'],
], 'calificacion_aprobatoria', '3')
def califica_calificacion_aprobatoria(f, uuid):
    return f


@template_iterable([
    [[1.40], "Puede subir :D"],
    [[1.23], "No puede subir :("],
    [[1.80], "Puede subir :D"]
], 'puede_subir', '3')
def califica_puede_subir(f, uuid):
    return f

@template_iterable([
    [[1,2,3], "Escaleno"],
    [[3,3,3], "Equilátero"],
    [[1,2,2], "Isósceles"],
], 'tipo_de_triangulo', '3')
def califica_tipo_de_triangulo(f, uuid):
    return f
    
####################################################################################################
#                                       Tarea 4
####################################################################################################


@template_sencillo([], 'creacion_de_lista_vacia', '4')
def califica_creacion_de_lista_vacia(f, uuid):
    return f

@template_sencillo((), 'creacion_de_una_tupla_vacia', '4')
def califica_creacion_de_una_tupla_vacia(f, uuid):
    return f
    
@template_sencillo({}, 'creacion_de_un_diccionario_vacio', '4')    
def califica_creacion_de_un_diccionario_vacio(f, uuid):
    return f

@template_iterable([
        ([[]], 0),
        ([[1,2,3]], 3),
        ([[1,2,3,4,5,6,7,8,9,10]], 10),
        ([list(range(100))], 100)
    ], 'obtener_longitu_de_una_lista', '4')
def califica_obtener_longitud_de_una_lista(f, uuid):
    return f

@template_iterable([
        ([()], 0),
        ([(1,2,3)], 3),
        ([(1,2,3,4,5,6,7,8,9,10)], 10),
        ([tuple(range(100))], 100)
    ], 'obtener_longitud_de_una_tupla', '4')
def califica_obtener_longitud_de_una_tupla(f, uuid):
    return f

@template_iterable([
        ([{}], 0),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], 3),
        ([{"Dia": "Martes"}], 1),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], 2)
    ], 'obtener_longitud_de_un_diccionario', '4')
def califica_obtener_longitud_de_un_diccionario(f, uuid):
    return f

@template_iterable([
        ([1], [1]),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], [{"Uno": 1,"Dos": 2, "Tres": 3}]),
        ([{"Dia": "Martes"}], [{"Dia": "Martes"}]),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], [{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}])
    ], 'creacion_de_una_lista_con_exactamente_un_elemento', '4')
def califica_creacion_de_una_lista_con_exactamente_un_elemento(f, uuid):
    return f

@template_iterable([
        ([1], (1,)),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], ({"Uno": 1,"Dos": 2, "Tres": 3},)),
        ([{"Dia": "Martes"}], ({"Dia": "Martes"},)),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], ({"Curso": "Python de la a a la z", "Fecha": "17 de enero"},))
    ], 'creacion_de_una_tupla_con_exactamente_un_elemento', '4')
def califica_creacion_de_una_tupla_con_exactamente_un_elemento(f, uuid):
    return f

@template_iterable([
        ([27], {'edad': 27}), 
        ([60], {'edad': 60}) 
    ], 'creacion_de_un_diccionario_con_clave_edad', '4')
def califica_creacion_de_un_diccionario_con_clave_edad(f, uuid):
    return f

@template_sencillo(['a', 'b', 'c'], 'creacion_de_una_lista_con_tres_elementos', '4')
def califica_creacion_de_una_lista_con_tres_elementos(f, uuid):
    return f

####################################################################################################
#                                       Tarea 5
####################################################################################################


@template_iterable([
        ([], ('a', '1', 'b'))
    ], 'creacion_de_una_tupla_con_exactamente_un_elemento', '5')
def califica_creacion_de_una_tupla_con_tres_elementos(f, uuid):
    return f

@template_iterable([
    [[[1,2,3,4,5,6]], 6],
    [[['a', 'b', 'c', 'd', 'e', 'f']], 'f'],
    [[[10, 11, 12, 13, 14, 15, 16, 17]], 15]
], 'acceder_al_elemento_5', '5')
def califica_acceder_al_elemento_5(f, uuid):
    return f
    
@template_iterable([
            [[27], 26], 
            [[60], 59],
            [[101], 100],
        ], 'acceder_al_ultimo_elemento_de_una_tupla_en_rango', '5')
def califica_acceder_al_ultimo_elemento_de_una_tupla_en_rango(f, uuid):
        return f

@template_sencillo({
    'estado': 'Activo',
    'datos': {
        'curso': 'Python de la A a la Z',
        'tareas': 3
    }
}, 'creacion_de_diccionario_dentro_de_otro_diccionario', '5')
def califica_creacion_de_diccionario_dentro_de_otro_diccionario(f, uuid):
    return f

@template_sencillo([
    {"pais": "México", "nombre oficial": "Estados Unidos Mexicanos"},
    {"pais": "Estados Unidos", "nombre oficial": "Estados Unidos de América"}
], 'creacion_de_lista_de_diccionarios', '5')
def califica_creacion_de_lista_de_diccionarios(f, uuid):
    return f

@template_sencillo({
        "tarea1": [
            10, 10, 8
        ],
        "tarea2": [
            10, 8, 7
        ]
    }, 'creacion_de_diccionario_con_listas', '5')
def califica_creacion_de_diccionario_con_listas(f, uuid):
    return f

@template_sencillo({
        "historial": ((3,5,1,6), (56,2,1,7), (62,4,78,3))
    }, 'creacion_de_diccionario_con_tuplas', '5')
def califica_creacion_de_diccionario_con_tuplas(f, uuid):
    return f

@template_iterable([
    [['edad', 27], {'edad': 27}],
    [['Nombre', "Pepito"], {'Nombre': 'Pepito'}],
    [[1, 27], {1: 27}],
    [["Calif", 100], {'Calif': 100}],
], 'creacion_de_diccionario_a_partir_de_clave', '5')
def califica_creacion_de_diccionario_a_partir_de_clave(f, uuid):
    return f

@template_sencillo(
    list(range(10001)), 'lista_hasta_10000', '5'
)
def califica_lista_hasta_10000(f, uuid):
    return f

@template_iterable([
    [[10], list(range(10))],
    [[100], list(range(100))],
    [[110], list(range(110))],
    [[2], list(range(2))],
    [[3], list(range(3))],
], 'lista_en_rango', '5')
def califica_lista_en_rango(f, uuid):
    return f

####################################################################################################
#                                       Tarea 6
####################################################################################################


@template_iterable([
    [[[1,2,3]], 6],
    [[[10, 20, 30]], 60],
    [[[9,8,7]], 24]
], 'obtener_suma_sencilla', '6')
def califica_obtener_suma_sencilla(f, uuid):
    return f


@template_iterable([
    [[[17, 18, 12, 12, 17]], 749088],
    [[[105, 148, 111, 143, 113]], 27873305460],
    [[[82, 56, 37, 153, 123]], 3197423376]
], 'obtener_multiplicacion_sencilla', '6')
def califica_obtener_multiplicacion_sencilla(f, uuid):
    return f

@template_iterable([
    [[["abecedario", "tacos", "enchiladas", "sal"]], ('abecedario', 'tacos', 'enchiladas')]
], 'obtener_palabras_mayores_a_3', '6')
def califica_obtener_palabras_mayores_a_3(f, uuid):
    return f

@template_iterable([
    [[10], 3628800],
    [[11], 39916800],
    [[12], 479001600],
], 'obtener_factorial', '6')
def califica_obtener_factorial(f, uuid):
    return f

@template_iterable([
    [[110], 3025],
    [[123], 3844],
    [[254], 16129],
], 'sumar_impares', '6')
def califica_sumar_impares(f, uuid):
    return f

@template_iterable([
    [[[3,7,5,1], 7], 1],
    [[[3,7,5,1], 1], 3],
    [[[3,7,5,1], 3], 0],
], 'encontrar_indice', '6')
def califica_encontrar_indice(f, uuid):
    return f

@template_iterable([
    [[[("tacos", 300), ("enchiladas", 200), ("sopes", 150)]], 650],
    [[[("Macbook Pro", 50), ("Macbook Air", 200), ("IPhone", 1000)]], 1250],
    [[[("Asus ROG", 5), ("Black Shark 4 Pro", 2), ("Realme GT Neo", 3), ("Nubia Red Magic 6", 4), ("Lenovo Legion Phone Duel 2", 1)]], 15],
    [[[("Sony MDR", 28), ("Cheelom", 34), ("Dinden", 3)]], 65],
    [[[("XYZ", 278), ("AYX", 312), ("KJO", 123)]], 713],
], 'suma_totales', '6')
def califica_suma_totales(f, uuid):
    return f

@template_iterable([
    [[[[1,2,3],[5,6,7],[7,8,9]]], [6, 18, 24]],
    [[[[-31,24,-3],[-35,-61,47],[47,2,90]]], [-10, -49, 139]],
    [[[[-1,-4,-5,3],[-5,-1,4],[47,2,90],[5,-7,-1,-5,-8],[1,2], [8,7,5]]], [-7, -2, 139, -16, 3, 20]]
], 'suma_filas', '6')
def califica_suma_filas(f, uuid):
    return f


@template_iterable([
    [[{"comida": "enchiladas", "Aguacate": "Verde", "agua": "Salada", "espinaca": "verdura"}], {"Aguacate": "Verde", "agua": "Salada"}],
    [[{"automatico": "Vehículo", "standard": "Carro"}], {"automatico": "Vehículo"}]
], 'revisar_claves', '6')
def califica_revisar_claves(f, uuid):
    return f

@template_iterable([
    [[{"ola": "Del mar", "hola": [1,2,3], "curso": "Python", "ZDRF": [3,4,5]}], ([6, 12], ['Python'])],
    [[{"RDF": [7,9,-1], "DCA": "Hola mundo", "SWECD": "Analitica", "QWSDE": "Delfos"}], ([15], ['Analitica', 'Delfos'])]
], 'filtrado', '6')
def califica_filtrado(f, uuid):
    return f

@template_iterable([
    [[10], (1, 2, 3, 5, 7)],
    [[11], (1, 2, 3, 5, 7, 11)],
    [[60], (1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59)]
], 'encontrar_primos', '6')
def califica_encontrar_primos(f, uuid):
    return f

@template_iterable([
    [[{"alberto": 10, "mariana": 10, "roberto": 8}], ['AL', 'MA', 'RO']],
    [[{"Pepe": 8, "Antonio": 7, "Esmeralda": 8}], ['PE', 'AN', 'ES']],
    [[{"Salmon": 9, "Brenda": 3, "Sofía": 10}], ['SA', 'BR', 'SO']]
], 'obtener_nickname', '6')
def califica_obtener_nickname(f, uuid):
    return f


####################################################################################################
#                                       Tarea 7
####################################################################################################


@template_iterable([
    [[10, 20], [10, 12, 14, 16, 18, 20]],
    [[100, 200], [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]],
    [[1, 2], [2]],
    [[2, 4], [2, 4]],
    [[3, 100], [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]],
], 'pares_en_rango', '7')
def califica_pares_en_rango(f, uuid):
    return f


@template_iterable([
    [[[1,2,3,4,5,6,7,8,9,10]], [5,10]],
    [[[10, 20, 30, 40, 50]], [10, 20, 30, 40, 50]],
    [[[1]], []],
    [[[33,44,55,66,77,88,99]], [55]],
    [[[101, 105, 104, 100]], [105, 100]],
], 'multiplos_de_5', '7')
def califica_multiplos_de_5(f, uuid):
    return f

@template_iterable([
    [["ae22"], (2,2)],
    [["1bq22"], (0,3)],
    [["aeiou"], (5,0)],
    [["12345"], (0,5)],
    [["12345aeiou"], (5,5)],
], 'contar_vocales_y_numeros', '7')
def califica_contar_vocales_y_numeros(f, uuid):
    return f

@template_iterable([
    [[{"alumnos": [10, 10]}], 10],
    [[{"alumnos": [5, 10]}], 7.5],
    [[{"alumnos": [5, 10, 5, 10]}], 7.5],
    [[{"alumnos": [8, 7, 6, 5, 10]}], 7.2],
    [[{"alumnos": [2, .5, 10, 10, 10]}], 6.5],
], 'obtener_promedio2', '7')
def califica_obtener_promedio2(f, uuid):
    return f

@template_iterable([
    [[[1,2,3,4,3], 3], 2],
    [[[3,2,3,3,3], 3], 4],
    [[[3,2,8,3,7], 7], 1],
    [[[3,8,8,3,7], 8], 2],
], 'encontrar_ocurrencias', '7')
def califica_encontrar_ocurrencias(f, uuid):
    return f

@template_iterable([
    [[["Hola", "Hola", "Adios"]], {"Hola": 2, "Adios": 1}],
    [[["Manzana", "Plátano", "Manzana", "Fresa", "Fresa"]], {"Manzana": 2, "Plátano": 1, "Fresa": 2}],
    [[["Manzana", "Manzana", "Manzana", "Manzana", "Fresa"]], {"Manzana": 4, "Fresa": 1}],
    [[["Python", "C++", "Python", "C++"]], {"Python": 2, "C++": 2}],
], 'contar_en_lista', '7')
def califica_contar_en_lista(f, uuid):
    return f

@template_iterable([
    [[[1,2,3], [2,3,4]], [2,3]],
    [[[2,2,2,2,2], [2,2,2,2,2,4]], [2]],
    [[[-1,-2,-3], [-3,-2,-4]], [-2,-3]],
    [[[-10,20,-30], [10,20,30]], [20]],
], 'elementos_comunes', '7')
def califica_elementos_comunes(f, uuid):
    return f

@template_iterable([
    [[{"manzanas": 3, "platanos": 2}], 5],
    [[{"tacos": 2, "sopes": 5, "tortas": 10}], 17],
    [[{"playeras": 5, "pantalones": 5, "chamarras": 5}], 15],
], 'sumar_claves_de_diccionario', '7')
def califica_sumar_claves_de_diccionario(f, uuid):
    return f

@template_iterable([
    [[["Hola", ["Hola", "Adios"], 3, (19,), 5, 8]], (8,)],
    [[["8", ["8"], 8, (1,), 8]], (8,)],
    [[[6, 4, 9, 3, -8, 9]], (6,9)],
], 'separar_numeros', '7')
def califica_separar_numeros(f, uuid):
    return f

####################################################################################################
#                                       Tarea 8
####################################################################################################

@template_iterable([
    [[3], """***
***
***"""],
[[4], """****
****
****
****"""]
], 'cuadrado_de_asteriscos', '8')
def califica_cuadrado_de_asteriscos(f, uuid):
    return f

@template_iterable([
    [[3, 4], """***
***
***
***"""],
[[4,3], """****
****
****"""]
], 'rectangulo_de_asteriscos', '8')
def califica_rectangulo_de_asteriscos(f, uuid):
    return f

@template_iterable([
    [[3], """*
**
***"""],
[[4], """*
**
***
****"""]
], 'triangulo_de_asteriscos', '8')
def califica_triangulo_de_asteriscos(f, uuid):
    return f

####################################################################################################
#                                       Tarea 9
####################################################################################################

@template_poo([
    ('metodo', 'mostrar_saludo', [], "Hola"),
    ('propiedad', 'saludo', [], 'Hola')
], "ejercicio_101", "10")
def califica_clase_saludos(f, uuid):
    return f

@template_poo([
    ('metodo', 'ladrar', [], "¡GUAU!"),
    ('metodo', 'asignar_raza', ["Pastor alemán"], "Raza asignada"),
    ('metodo', 'asignar_nombre', ["Pepe"], "Nombre asignado"),
    ('propiedad', 'raza', [], 'Pastor alemán'),
    ('propiedad', 'nombre', [], 'Pepe')
], "perro", "9")
def califica_clase_perro(f, uuid):
    return f

@template_poo([
    ('propiedad', 'marca', [], 'Delfos'),
    ('metodo', 'suma', [1,2], 3),
    ('metodo', 'suma', [-1,-2], -3),
    ('metodo', 'resta', [-1,-2], 1),
    ('metodo', 'resta', [1,-2], 3),
    ('metodo', 'multiplicacion', [1,-2], -2),
    ('metodo', 'multiplicacion', [10,20], 200),
    ('metodo', 'division', [1,-2], -.5),
    ('metodo', 'division', [1,2], .5),
    ('metodo', 'division', [1,0], "No se puede dividir entre cero"),
], 'calculadora_basica', "9")
def califica_clase_calculadora_basica(f, uuid):
    return f

@template_poo([
    ('propiedad', 'marca', [], 'Delfos'),
    ('metodo', 'euclideana', [[0,0], [0,0]], 0.0),
    ('metodo', 'euclideana', [[0,0], [0,1]], 1.0),
    ('metodo', 'euclideana', [[0,0], [1,1]], 1.41),
    ('metodo', 'euclideana', [[0,1], [0,0]], 1.),
    ('metodo', 'euclideana', [[1,1], [0,0]], 1.41),
    ('metodo', 'manhattan', [[0,0], [0,0]], 0),
    ('metodo', 'manhattan', [[0,0], [0,1]], 1),
    ('metodo', 'manhattan', [[0,0], [1,1]], 2),
    ('metodo', 'manhattan', [[0,1], [0,0]], 1),
    ('metodo', 'manhattan', [[1,1], [0,0]], 2),
    ('metodo', 'discreta', [[0,0], [0,0]], 1),
    ('metodo', 'discreta', [[0,0], [0,1]], 0),
    ('metodo', 'discreta', [[0,0], [1,1]], 0),
    ('metodo', 'discreta', [[0,1], [0,0]], 0),
    ('metodo', 'discreta', [[1,1], [0,0]], 0),

], 'distancias', "9")
def califica_distancias(f, uuid):
    return f

####################################################################################################
#                                       Extras
####################################################################################################

@template_iterable([
    [[10, 20], list(range(10, 20))],
    [[38, 40], list(range(38, 40))],
    [[12, 22], list(range(12, 22))],
    [[-2, 32], list(range(-2, 32))],
    [[-29, 20], list(range(-29, 20))],
], 'lista_en_rango_v_2', '5')
def califica_lista_en_rango_v_2(f, uuid):
    return f


@template_iterable([
        ([[]], 0),
        ([[1,2,3]], 3),
        ([[1,2,3,4,5,6,7,8,9,10]], 10),
        ([list(range(100))], 100)
    ], 'obtener_longitu_de_una_lista', '4')
def califica_obtener_longitud_de_una_lista(f, uuid):
    return f




@template_iterable([
        ([{}], 0),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], 3),
        ([{"Dia": "Martes"}], 1),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], 2)
    ], 'obtener_longitud_de_un_diccionario', '4')
def califica_obtener_longitud_de_un_diccionario(f, uuid):
    return f

@template_iterable([
        ([1], [1]),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], [{"Uno": 1,"Dos": 2, "Tres": 3}]),
        ([{"Dia": "Martes"}], [{"Dia": "Martes"}]),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], [{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}])
    ], 'creacion_de_una_lista_con_exactamente_un_elemento', '4')
def califica_creacion_de_una_lista_con_exactamente_un_elemento(f, uuid):
    return f

@template_iterable([
        ([1], (1,)),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], ({"Uno": 1,"Dos": 2, "Tres": 3},)),
        ([{"Dia": "Martes"}], ({"Dia": "Martes"},)),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], ({"Curso": "Python de la a a la z", "Fecha": "17 de enero"},))
    ], 'creacion_de_una_tupla_con_exactamente_un_elemento', '4')
def califica_creacion_de_una_tupla_con_exactamente_un_elemento(f, uuid):
    return f

@template_iterable([
        ([27], {'edad': 27}), 
        ([60], {'edad': 60}) 
    ], 'creacion_de_un_diccionario_con_clave_edad', '4')
def califica_creacion_de_un_diccionario_con_clave_edad(f, uuid):
    return f





@template_sencillo({1,2,3,4,5}, 'conjunto_con_elementos_del_1_al_5', 't6-')
def califica_conjunto_con_elementos_del_1_al_5(f, uuid):
    return f
    
@template_iterable([
    [['Hola', 'Aloha', 'Saludos'], {'Hola', 'Aloha', 'Saludos'}]
], 'conjunto_con_tres_palabras', 't6-')
def califica_conjunto_con_tres_palabras(f, uuid):
    return f






####################################################################################################
#                                       Tarea 7
####################################################################################################











@template_iterable([
    [[10, 20], list(range(10, 20))],
    [[38, 40], list(range(38, 40))],
    [[12, 22], list(range(12, 22))],
    [[-2, 32], list(range(-2, 32))],
    [[-29, 20], list(range(-29, 20))],
], 'lista_en_rango_v_2', 't4-')
def califica_lista_en_rango_v_2(f, uuid):
    return f

@template_iterable([
    [[[1,2,3], 4,5,6], [1,2,3,4,5,6]],
    [[[1,2,3], 'hola', 'adios', 'saludos'], [1,2,3,'hola', 'adios', 'saludos']],
    [[[2, "", 1], "4,5,6", {}, ()], [2, "", 1,"4,5,6", {}, ()]]
], 'agregar_elementos_al_final_de_una_lista', 't4-')
def califica_agregar_elementos_al_final_de_una_lista(f, uuid):
    return f

@template_iterable([
    [[[1,2,3], [4,5,6]], [1,2,3,4,5,6]],
    [[['a', 'e'], ['i', 'o', 'u']], ['a', 'e','i', 'o', 'u']],
], 'extender_lista_con_otra_lista', 't4-')
def califica_extender_lista_con_otra_lista(f, uuid):
    return f

@template_iterable([
    [[[1,3], 2, 1], [1,2,3]],
    [[["Hola, ", "mundo", " de nuevo"] , " soy yo", 2], ["Hola, ", "mundo", " soy yo", " de nuevo"]]
], 'insertar_elementos_en_una_posicion', 't4-')
def califica_insertar_elementos_en_una_posicion(f, uuid):
    return f

@template_iterable([
    [[[1,2,3,4,5,6,7,8,9], 0], [2,3,4,5,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 1], [1,3,4,5,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 2], [1,2,4,5,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 3], [1,2,3,5,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 4], [1,2,3,4,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 5], [1,2,3,4,5,7,8,9]],
], 'borrar_elemento_por_indice', 't4-')
def califica_borrar_elemento_por_indice(f, uuid):
    return f

@template_iterable([
    [[[1, 'hola', 2, 'salduo', 3, 'adiós'], 1], ['hola', 2, 'salduo', 3, 'adiós']],
    [[[1, 'hola', 2, 'salduo', 3, 'adiós'], 'hola'], [1, 2, 'salduo', 3, 'adiós']]
], '_borrar_coincidencia', 't4-')
def califica_borrar_coincidencia(f, uuid):
    return f

@template_iterable([
    [[[9,8,6,7,4,5,3,1,2]], [1,2,3,4,5,6,7,8,9]],
    [[[5,6,7,4,8,3,9,2,1]], [1,2,3,4,5,6,7,8,9]],
], 'ordenar_lista', 't4-')
def califica_ordenar_lista(f, uuid):
    return f

@template_iterable([
    [[[1,2,3,4,5,6,7,8,9], 1000], [1,2,3,4,5,1000,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], "Hola"], [1,2,3,4,5,"Hola",7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], "Sorpresa"], [1,2,3,4,5,"Sorpresa",7,8,9]],
], 'asignar_en_5', 't4-')
def califica_asignar_en_5(f, uuid):
    return f

@template_sencillo({
        'tiendas': {
            'Don Pepe Chuy': [
                {
                    'Ventas': [100, 200, 300] 
                },
                {
                    'Ventas': [100, 200, 300]
                }
            ],
            'El Ruki': [
                {
                    'Ventas': [234, 543, 654]
                },
                {
                    'Ventas': [980, 579, 123] 
                }
            ]
        }
    }, 'borrar_elemento_en_estructura_compleja', 't4-', argumentos=[
        {
        'tiendas': {
            'Don Pepe Chuy': [
                {
                    'Ventas': [100, 200, 300, -1]
                },
                {
                    'Ventas': [100, 200, 300]
                }
            ],
            'El Ruki': [
                {
                    'Ventas': [234, 543, 654]
                },
                {
                    'Ventas': [980, 579, 123, 0]
                }
            ]
        }
    }
    ])
def califica_borrar_elemento_en_estructura_compleja(f, uuid):
    return f

@template_sencillo(
    {'Pepe': 9.5, 'Juan': 9.5},
    'obtener_promedio', 't4-',
    argumentos=[
            {
            'Pepe':[
                    {'nombre': 'primer parcial', 'calif': 9},
                    {'nombre': 'segundo parcial', 'calif': 10}
                ],
            'Juan': [
                    {'nombre': 'primer parcial', 'calif': 9},
                    {'nombre': 'segundo parcial', 'calif': 10}
                ]
            }
        ]
    )
def califica_obtener_promedio(f, uuid):
    return f
####################################################################################################
#                                       Tarea 3
####################################################################################################





####################################################################################################
#                              Tarea 5 (tarea 4 ya que la uno no fue tarea)
####################################################################################################





@template_iterable([
    [[3], 6],
    [[4], 24],
    [[5], 120],
    [[6], 720],
    [[7], 5040],
    [[8], 40320],
], 'calcular_factorial', 't5-')
def califica_calcular_factorial(f, uuid):
    return f

@template_iterable([
    [[[1,2,3], [2,4,6]], True],
    [[[10,20,30], [20,40,60]], True],
    [[[1,2,3], [2,4,5]], False],
    [[[4,3,8], [8,6,16]], True],
    [[[1], [1]], False]
], 'pares_un_medio', 't5-')
def califica_pares_un_medio(f, uuid):
    return f



@template_iterable([
    [[[1,2,3,4,5,6]], (4.0, 3.0)],
    [[[3,4,5,1,7,3,2]], (3.0, 3.8)],
    [[[1,2,3,5,6,10,11,200,32,13]], (50.0, 6.6)],
    [[[2,8,6,3,7,4,83,21,45]], (5.0, 31.8)],
    [[[97,5,3,2,34,5,6,766]], (202.0, 27.5)],
], 'promedios', 't5-')
def califica_promedios(f, uuid):
    return f

