#
import unittest


# TEST: para probar entorno.
def ej00(valor):
    """
    Retorna valor sin hacer nada.
    Para que el test funcione, cambia return None
    por return valor
    """
    # return valor
    return None


# Operadores basicos: and, or, not, +, -, *, etc.
def ej01(dia_de_semana, vacaciones):
    """
    Descansamos si no es dia de semana o si
    estamos de vacaciones.
    Devuelve si descansamos...
    """
    return None


def ej02(a_se_rie, b_se_rie):
    """
    Hay 2 monos, a y b.
    Si ninguno se rie estamos en problemas.
    Si los dos se rien tambien.
    Retorna si estamos en problemas.
    """
    return None


def ej03(a, b):
    """
    Retorna la suma de a y b.
    Excepto si son iguales, si son iguales retorna
    el doble de la suma.
    """
    return 0


def ej04(gritando, hora):
    """
    gritando indica si el nene esta gritando.
    hora indica la hora entre 0 y 23.
    Si el nene llora antes de las 8 o despues de las
    23, estamos en problemas.
    Devuelve si estamos en problemas.
    """
    return False


def ej05(a, b):
    """
    Dados 2 numeros a y b, retorna si a es igual a 10,
    o si b es igual a 10, o si la suma de a y b es igual
    a 10.
    """
    return True


# Strings.
def ej06(cadena):
    """
    Dado una cadena, retorna otra cadena donde se agrego
    "not" al principio de la cadena.
    Excepto si la cadena empieza con "not", entonces
    devuelve la cadena como esta.
    """
    return cadena


def ej07(cadena, indice):
    """
    Retorna la cadena dada sin el caracter en el indice
    dado, por ejemplo: "12345", 0 -> "2345" porque elimina
    el indice 0: "1"
    El indice esta en el rango de la cadena.
    """
    return cadena


def ej08(cadena, n):
    """
    Retorna n-copias de la cadena.
    "Hola", 2 -> "HolaHola"
    """
    return ""


# Arrays
def ej09(nums):
    """
    Dado un array de numeros, devuelve la
    cantidad de veces que aparece el numero
    9.
    """
    return 0


def ej10(nums):
    """
    Dado un array de numeros, devuelve si
    el numero 9 aparece entre los primeros
    4 numeros del array.
    [1, 2, 3, 4, 5, 9] -> False: no aparece
    entre los primeros 4.
    [9, 9, 1, 2, 5] -> True
    [9] -> True
    """
    return False


def ej11(arreglo, n):
    """
    Dado un arreglo, devuelve uno nuevo con
    los elementos del original rotado n veces.
    Una rotacion toma el primer elemento del
    arreglo y lo pone al final.
    Ejemplo de rotacion 2:
    [1,2,3,4,5], 2 -> [3,4,5,1,2]
    """
    return arreglo


def ej12(arr_a, arr_b):
    """
    Dados 2 arreglos, arr_a y arr_b, devuelve
    True si los dos arreglos tienen el mismo
    elemento al principio y el mismo elemento
    al final.
    [1, 2, 3, 4] y [1, 4] tiene el mismo elemento
    al principio (1) y al final (4).
    """
    return False


def ej13(arreglo):
    """
    Devuelva la suma del minimo y el maximo del arreglo:
    [7, 9, 3, 5, 1, 4] -> 10: suma de 1 y 9.
    """
    return 0


def ej14(arreglo):
    """
    Devuelve si el arreglo tiene el numero 1, el 2 o el 3.
    [1, 5, 7] ->  True
    [5, 7, 9] -> False
    [] -> False
    [1, 2, 3] -> True
    """
    return False


def ej15(arreglo):
    """
    Devuelve True si el arreglo tiene elementos duplicados.
    [1, 2, 3] -> False
    [1, 2, 3, 3] -> True
    """
    return False


def ej16(agenda, nombre):
    """
    Dado un diccionario "agenda" donde las
    keys son nombres y los values son numeros
    de telefono, retorna el numero de telefono
    del nombre pedido o None si el nombre no
    esta agendado.
    """
    return None


def ej17(botellas, personas, findesemana):
    """
    Dado un asado, la cantidad de botellas esta
    bien si hay entre 2 y 3 botellas por persona.
    Excepto si es fin de semana, en ese caso no
    hay limite maximo para la cantidad de botellas.
    Retorna si la cantidad de botellas esta bien.
    """
    return False


def ej18(velocidad, juegaseleccion):
    """
    Devuelve el valor de una infraccion de transito
    para un limite de velocidad de 60.
    Si la velocidad es menor igual a 60, devuelve 0
    (sin multa).
    Si la velocidad esta entre 61 y 80, devuelve 1
    (multa leve).
    Si la velocidad es mayor a 81, devuelve 2.
    Excepto si juega la seleccion, si juega la
    seleccion todas las multas son 0 o 1 (no hay
    multas graves).
    """
    return 0


def ej19(numeros_sumadores):
    """
    Los numeros juegan en un equipo sumando.
    El resultado del equipo es la suma de los
    numeros en el arreglo numeros_sumadores.
    Pero, si un numero aparece mas de 1 ves
    en el arreglo, ese numero se descalifica y
    no suma.
    Retorna el resultado del equipo de numeros.
    Ejemplos:
    [1, 2, 3] -> 6
    [3, 2, 3] -> 2  # el 3 no suma por tramposo!
    [3, 3, 3] -> 0  # flor de tranposo.
    """
    return 0


class Clase1Tests(unittest.TestCase):
    def test_ej00(self):
        for i in [None, 1, 3, "4", dict()]:
            self.assertEqual(ej00(i), i)

    def test_ej01(self):
        self.assertEqual(ej01(True, True), True)
        self.assertEqual(ej01(True, False), False)
        self.assertEqual(ej01(False, True), True)
        self.assertEqual(ej01(False, False), True)

    def test_ej02(self):
        self.assertEqual(ej02(True, True), True)
        self.assertEqual(ej02(True, False), False)
        self.assertEqual(ej02(False, True), False)
        self.assertEqual(ej02(False, False), True)

    def test_ej03(self):
        self.assertEqual(ej03(1, 2), 3)
        self.assertEqual(ej03(3, 2), 5)
        self.assertEqual(ej03(2, 2), 8)
        self.assertEqual(ej03(10, 10), 40)
        self.assertEqual(ej03(0, 0), 0)
        self.assertEqual(ej03(0, -1), -1)

    def test_ej04(self):
        self.assertEqual(ej04(True, 0), True)
        self.assertEqual(ej04(True, 7), True)
        self.assertEqual(ej04(True, 8), False)
        self.assertEqual(ej04(True, 23), False)
        self.assertEqual(ej04(False, 0), False)
        self.assertEqual(ej04(False, 7), False)
        self.assertEqual(ej04(False, 8), False)
        self.assertEqual(ej04(False, 23), False)

    def test_ej05(self):
        self.assertEqual(ej05(10, 0), True)
        self.assertEqual(ej05(45, 10), True)
        self.assertEqual(ej05(5, 5), True)
        self.assertEqual(ej05(4, 5), False)
        self.assertEqual(ej05(3, 5), False)
        self.assertEqual(ej05(1, 5), False)
        self.assertEqual(ej05(4, 8), False)

    def test_ej06(self):
        self.assertEqual(ej06("cool"), "not cool")
        self.assertEqual(ej06("x"), "not x")
        self.assertEqual(ej06("bad"), "not bad")
        self.assertEqual(ej06(""), "not ")
        self.assertEqual(ej06("not cool"), "not cool")
        self.assertEqual(ej06("not"), "not")
        self.assertEqual(ej06("is not"), "not is not")

    def test_ej07(self):
        self.assertEqual(ej07("cool", 2), "col")
        self.assertEqual(ej07("cool", 0), "ool")
        self.assertEqual(ej07("cool", 1), "col")
        self.assertEqual(ej07("cool", 3), "coo")

    def test_ej08(self):
        self.assertEqual(ej08("hi", 2), "hihi")
        self.assertEqual(ej08("", 10), "")
        self.assertEqual(ej08("hi", 0), "")
        self.assertEqual(ej08("Qi", 5), "QiQiQiQiQi")

    def test_ej09(self):
        self.assertEqual(ej09([0, 1, 2]), 0)
        self.assertEqual(ej09([0, 9, 2]), 1)
        self.assertEqual(ej09([9, 1, 2]), 1)
        self.assertEqual(ej09([0, 9, 9]), 2)

    def test_ej10(self):
        self.assertEqual(ej10([0, 1, 2, 3, 9]), False)
        self.assertEqual(ej10([0, 1, 2, 9, 0]), True)
        self.assertEqual(ej10([0]), False)
        self.assertEqual(ej10([9]), True)
        self.assertEqual(ej10([0, 9, 1]), True)

    def test_ej11(self):
        self.assertEqual(ej11([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])
        self.assertEqual(ej11([1, 2, 3, 4, 5], 1), [2, 3, 4, 5, 1])
        self.assertEqual(ej11([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
        self.assertEqual(ej11([1, 2, 3, 4, 5], 3), [4, 5, 1, 2, 3])
        self.assertEqual(ej11([1, 2, 3, 4, 5], 6), [2, 3, 4, 5, 1])

    def test_ej12(self):
        self.assertEqual(ej12([1, 2, 3, 4], [1, 4]), True)
        self.assertEqual(ej12([1, 2, 3, 4], [1, 3]), False)
        self.assertEqual(ej12([2, 2, 3, 4], [1, 4]), False)
        self.assertEqual(ej12([1, 2, 3, 4], [1, 2, 3, 4]), True)
        self.assertEqual(ej12([3, 4], [3, 1, 2, 4]), True)
        self.assertEqual(ej12([4], [4, 1, 2, 4]), True)

    def test_ej13(self):
        self.assertEqual(ej13([1, 2, 3, 4]), 5)
        self.assertEqual(ej13([7, 9, 2, 1, 4]), 10)
        self.assertEqual(ej13([1, 1]), 2)

    def test_ej14(self):
        self.assertEqual(ej14([1, 2, 3]), True)
        self.assertEqual(ej14([5, 6, 7]), False)
        self.assertEqual(ej14([]), False)
        self.assertEqual(ej14([3, 4, 5]), True)
        self.assertEqual(ej14([8, 9, 0, 2]), True)

    def test_ej15(self):
        self.assertEqual(ej15([]), False)
        self.assertEqual(ej15([1]), False)
        self.assertEqual(ej15([1, 2]), False)
        self.assertEqual(ej15([1, 2, 3]), False)
        self.assertEqual(ej15([1, 1]), True)
        self.assertEqual(ej15([1, 2, 1]), True)
        self.assertEqual(ej15([1, 2, 3, 3]), True)

    def test_ej16(self):
        agenda = dict(nacho='151234567', mario='156789012')
        self.assertEqual(ej16(agenda, 'nacho'), '151234567')
        self.assertEqual(ej16(agenda, 'mario'), '156789012')
        self.assertEqual(ej16(agenda, 'raul'), None)

    def test_ej17(self):
        self.assertEqual(ej17(0, 2, False), False)
        self.assertEqual(ej17(3, 2, False), False)
        self.assertEqual(ej17(4, 2, False), True)
        self.assertEqual(ej17(6, 2, False), True)
        self.assertEqual(ej17(7, 2, False), False)

        self.assertEqual(ej17(0, 2, True), False)
        self.assertEqual(ej17(3, 2, True), False)
        self.assertEqual(ej17(4, 2, True), True)
        self.assertEqual(ej17(6, 2, True), True)
        self.assertEqual(ej17(7, 2, True), True)

    def test_ej18(self):
        self.assertEqual(ej18(40, False), 0)
        self.assertEqual(ej18(60, False), 0)
        self.assertEqual(ej18(61, False), 1)
        self.assertEqual(ej18(80, False), 1)
        self.assertEqual(ej18(81, False), 2)
        self.assertEqual(ej18(90, False), 2)

        self.assertEqual(ej18(40, True), 0)
        self.assertEqual(ej18(60, True), 0)
        self.assertEqual(ej18(61, True), 1)
        self.assertEqual(ej18(80, True), 1)
        self.assertEqual(ej18(81, True), 1)
        self.assertEqual(ej18(90, True), 1)

    def test_ej19(self):
        self.assertEqual(ej19([]), 0)
        self.assertEqual(ej19([10]), 10)
        self.assertEqual(ej19([1, 2, 3]), 6)
        self.assertEqual(ej19([1, 2, 3, 4, 5]), 15)
        self.assertEqual(ej19([3, 2, 3]), 2)
        self.assertEqual(ej19([3, 3, 3]), 0)
        self.assertEqual(ej19([3, 2, 3, 2, 3]), 0)
        self.assertEqual(ej19([3, 2, 3, 1, 3]), 3)


if __name__ == "__main__":
    unittest.main()
