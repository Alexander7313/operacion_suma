import unittest
from operaciones_aritmeticas import OperacionesAritmeticas

class TestSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15

        resultadoEsperado = 25

        objSuma  = OperacionesAritmeticas(operando1, operando2)

        # Act

        resultadoActual = objSuma.calcularSuma()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, msg="Fallo la suma")

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(1, "a")
        with self.assertRaises(TypeError):
            objSuma.calcularSuma()
    def test_division_dosNumeros_retornarDivision(self):
        # Arrange
        dividendo = 10
        divisor = 15

        resultadoEsperado = 0.666

        objSuma  = OperacionesAritmeticas(dividendo, divisor)

        # Act

        resultadoActual = objSuma.calcularDivision()

        # Assert
        self.assertAlmostEquals(resultadoEsperado, resultadoActual, 2,  msg ="Fallo la división")

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(1, "a")
        with self.assertRaises(TypeError):
            objSuma.calcularSuma()

##https://github.com/jdgamarram/operacion_suma.git


if __name__ == '__main__':
    unittest.main()
