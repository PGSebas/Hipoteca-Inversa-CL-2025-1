import unittest
from calculo import *

class TestFinanciacion(unittest.TestCase):
    def test_porcentaje_financiado(self):
        #Entrada
        edad = 68

        # Calculo 
        resultado = calcular_porcentaje_financiado(edad)

        # Verificación
        self.assertEqual(resultado, 30)

    def test_plazo_financiacion(self):
        #Entrada
        edad = 68
        
        # Calculo
        resultado = calcular_plazo_financiacion(edad)

        # Verificación
        self.assertEqual(resultado, 20)

    def test_pago_mensual(self):
        #Entrada
        porcentaje_financiado = 30
        valor_vivienda = 500000000
        plazo = 20
        
        # Calculo
        resultado = calcular_pago_mensual(porcentaje_financiado, valor_vivienda, plazo)

        # Verificación
        self.assertEqual(resultado, 625000.0)

if __name__ == '__main__':
    unittest.main()