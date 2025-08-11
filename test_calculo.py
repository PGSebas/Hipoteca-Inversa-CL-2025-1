import unittest
from calculo import *

class TestHipotecaInversa(unittest.TestCase):
    # =========================
    # CASO 1
    # =========================
    def test_caso_1_porcentaje(self):
        # Entrada
        edad = 68.0
        # Cálculo
        resultado = calcular_porcentaje_financiado(edad)
        # Verificación
        self.assertEqual(resultado, 30)



if __name__ == "__main__":
    unittest.main()
