import math
import unittest


# Clases y objetos
class ClaseMinima(object):
    """
    No podria ser mas chica.
    """
    pass


"""
Ejercicio 01
Retorna una instancia de clase ClaseMinima.
"""
def ej01():
    return None


class Figura(object):
    def get_area(self):
        raise NotImplementedError("Hay que implementarlo en la subclase")
        return 0.0

    def get_perimetro(self):
        raise NotImplementedError("Hay que implementarlo en la subclase")
        return 0.0


"""
Ejercicio 2:

Definir las subclases de Figura: Rectangulo y Circulo.
Rectangulo se inicializa con 2 parametros en el constructor: largo y alto.
Circulo tiene 1 parametro en el constructor: el radio.

Cada subclase debe redefinir los metodos get_area y get_perimetro.
Area:
    rectangulo: base x altura
    circulo: pi x radio al cuadrado
Circunferencia:
    rectangulo: base * 2 + altura * 2
    circulo: pi x diametro
"""

# definir la clase Rectangulo aca...

# definir la clase Circulo aca...


"""
Ejercicio 3:

La clase Persona tiene un constructor que toma nombre, apellido y id.
Definir la subclase de Persona llamada PersonaConLicencia que
en el constructor toma nombre, apellido, id e numero_de_licencia.
Los primeros 3 parametros tiene que pasarlos a la clase padre.
"""
class Persona(object):
    def __init__(self, nombre, apellido, id):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido


"""
Ejercicio 4:
Completar el generador multiplos.
multiplos(n) retorna un generador que devuelve
los multiplos del numero n empezando en n mismo.
Ejemplo:
g = multiplos(2)
g.next() == 2
g.next() == 4
...

g = multiplos(4)
g.next() = 4
g.next() = 8
...
"""
def multiplos(n):
    return 0


"""
Ejercicio 5:
Dada la lista parametro, devolver una lista con
todos los strings que tengan una arroba adentro:
"nombre@123.com".
Usar filter y lambda!
"""
def arroba(lista):
    return []


"""
Ejercicio 6:
Dada la lista parametro, devolver una lista con
los largos del string, ejemplo:
["123", "hola", "", "vvvvv"] retorna [3, 4, 0, 5]
Usar map y lambda
"""
def largos(lista):
    return []

"""
Ejercicio 7:
Dada la lista parametro, devolver el mayor de los elementos
[1, 10, 100, 99, 15] retorna 100
Usar reduce y lambda
"""
def mayor(lista):
    return 0


"""
Ejercicios con listas por comprension (sin tests)...
* Crear una lista de los cuadrados de los primeros 100 numeros
[0, 1, 4, 9, 16, ...]

* Crear una lista con tuplas cuadrado y cubo de los primeros 100 numeros:
[(0, 0), (1, 1), (4, 8), (9, 27), ...]

* Dada la siguiente lista de nombres, calcular la lista con
  los nombres en mayusculas:
  ["Jose", "Julian", "Andres", "Raul", "Gerardo"]
  ->
  ["JOSE", "JULIAN", ...]

"""

class Clase4Tests(unittest.TestCase):
    def test_ej1(self):
        self.assertTrue(isinstance(ej01(), ClaseMinima))

    def test_ej2(self):
        c1 = Rectangulo(10.0, 20.0)
        self.assertTrue(isinstance(c1, Figura))
        self.assertEqual(c1.get_area(), 200.0)
        self.assertEqual(c1.get_perimetro(), 60.0)
        c2 = Rectangulo(15.0, 25.0)
        self.assertEqual(c2.get_area(), 15.0 * 25.0)
        self.assertEqual(c2.get_perimetro(), 15.0 + 15.0 + 25.0 + 25.0)
        for r in [1.0, 3.0, 5.0, 10.0]:
            circ = Circulo(r)
            self.assertTrue(isinstance(circ, Figura))
            self.assertAlmostEqual(circ.get_area(), r**2*math.pi, 3)
            self.assertAlmostEqual(circ.get_perimetro(), r*2*math.pi, 3)

    def test_ej3(self):
        pcl = PersonaConLicencia("nom", "app", "12345678", "005-1233")
        self.assertTrue(isinstance(pcl, Persona))
        self.assertEqual(pcl.numero_de_licencia, "005-1233")
        self.assertEqual(pcl.nombre, "nom")
        self.assertEqual(pcl.apellido, "app")
        self.assertEqual(pcl.id, "12345678")

    def test_ej4(self):
        g = multiplos(3)
        self.assertEqual([g.next() for _ in range(5)][-1], 15)
        g = multiplos(7)
        self.assertEqual([g.next() for _ in range(5)][-1], 35)
        g = multiplos(4)
        self.assertEqual([g.next() for _ in range(1800)][-1], 7200)

    def test_ej5(self):
        self.assertEqual(arroba([]), [])
        self.assertEqual(arroba(["123", "123"]), [])
        self.assertEqual(arroba(["@123", "123", "123@"]), ["@123", "123@"])
        self.assertEqual(arroba(["@", "1@3", "123@"]), ["@", "1@3", "123@"])

    def test_ej6(self):
        self.assertEqual(largos(["123", "hola", "", "vvvvv"]), [3, 4, 0, 5])
        self.assertEqual(largos([]), [])
        self.assertEqual(largos(["x"*n for n in range(10)]), range(10))

    def test_ej7(self):
        self.assertEqual(mayor([1, 2, 3]), 3)
        self.assertEqual(mayor([1, 2, 3, 4, 5]), 5)
        self.assertEqual(mayor([1, 2, 100, 99, 44]), 100)


if __name__ == "__main__":
    unittest.main()
