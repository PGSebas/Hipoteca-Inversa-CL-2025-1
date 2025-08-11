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

    def test_caso_1_plazo(self):
        # Entrada
        edad = 68.0
        # Cálculo
        resultado = calcular_plazo_financiacion(edad)
        # Verificación
        self.assertEqual(resultado, 20)

    def test_caso_1_pago_mensual(self):
        # Entrada
        porcentaje_financiado = 30
        valor_vivienda = 500_000_000.0
        plazo = 20
        # Cálculo
        resultado = calcular_pago_mensual(porcentaje_financiado, valor_vivienda, plazo)
        # Verificación
        self.assertAlmostEqual(resultado, 625000.0, places=6)


if __name__ == "__main__":
    unittest.main()
