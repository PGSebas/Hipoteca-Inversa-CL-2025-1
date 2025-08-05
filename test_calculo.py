import unittest
from calculo import *

class TestFinanciacion(unittest.TestCase):
    def test_porcentaje_financiado(self):
        #Entrada
        edad = 68

        # Resultado esperado
        resultado = calcular_porcentaje_financiado(edad)

        # Verificación
        self.assertEqual(resultado, 30)

    def test_plazo_financiacion(self):
        #Entrada
        edad = 68
        
        # Resultado esperado
        resultado = calcular_plazo_financiacion(edad)

        # Verificación
        self.assertEqual(resultado, 20)

if __name__ == '__main__':
    unittest.main()