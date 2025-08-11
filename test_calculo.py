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

    def test_caso_1_intereses(self):
        # Entrada
        edad = 68.0
        valor_vivienda = 500_000_000.0
        # Cálculo
        pf = calcular_porcentaje_financiado(edad)
        plazo = calcular_plazo_financiacion(edad)
        pago = calcular_pago_mensual(pf, valor_vivienda, plazo)
        intereses, _ = calcular_intereses(pago, TASA_EFECTIVA_MENSUAL, plazo * 12)
        # Verificación
        self.assertAlmostEqual(intereses, 51708483.423720025, places=2)

    # =========================
    # CASO 2
    # =========================
    def test_caso_2_porcentaje(self):
        # Entrada
        edad = 70.0
        # Cálculo
        resultado = calcular_porcentaje_financiado(edad)
        # Verificación
        self.assertEqual(resultado, 40)

    def test_caso_2_plazo(self):
        # Entrada
        edad = 70.0
        # Cálculo
        resultado = calcular_plazo_financiacion(edad)
        # Verificación
        self.assertEqual(resultado, 15)

    def test_caso_2_pago_mensual(self):
        # Entrada
        porcentaje_financiado = 40
        valor_vivienda = 400_000_000.0
        plazo = 15
        # Cálculo
        resultado = calcular_pago_mensual(porcentaje_financiado, valor_vivienda, plazo)
        # Verificación
        self.assertAlmostEqual(resultado, 888888.8888888889, places=6)

    def test_caso_2_intereses(self):
        # Entrada
        edad = 70.0
        valor_vivienda = 400_000_000.0
        # Cálculo
        pf = calcular_porcentaje_financiado(edad)
        plazo = calcular_plazo_financiacion(edad)
        pago = calcular_pago_mensual(pf, valor_vivienda, plazo)
        intereses, _ = calcular_intereses(pago, TASA_EFECTIVA_MENSUAL, plazo * 12)
        # Verificación
        self.assertAlmostEqual(intereses, 23716044.688623436, places=2)

    # =========================
    # CASO 3
    # =========================
    def test_caso_3_porcentaje(self):
        # Entrada
        edad = 80.0
        # Cálculo
        resultado = calcular_porcentaje_financiado(edad)
        # Verificación
        self.assertEqual(resultado, 55)

    def test_caso_3_plazo(self):
        # Entrada
        edad = 80.0
        # Cálculo
        resultado = calcular_plazo_financiacion(edad)
        # Verificación
        self.assertEqual(resultado, 5)

    def test_caso_3_pago_mensual(self):
        # Entrada
        porcentaje_financiado = 55
        valor_vivienda = 200_000_000.0
        plazo = 5
        # Cálculo
        resultado = calcular_pago_mensual(porcentaje_financiado, valor_vivienda, plazo)
        # Verificación
        self.assertAlmostEqual(resultado, 1833333.3333333333, places=6)

    def test_caso_3_intereses(self):
        # Entrada
        edad = 80.0
        valor_vivienda = 200_000_000.0
        # Cálculo
        pf = calcular_porcentaje_financiado(edad)
        plazo = calcular_plazo_financiacion(edad)
        pago = calcular_pago_mensual(pf, valor_vivienda, plazo)
        intereses, _ = calcular_intereses(pago, TASA_EFECTIVA_MENSUAL, plazo * 12)
        # Verificación
        self.assertAlmostEqual(intereses, 3712493.966080846, places=2)

    # =========================
    # CASO 4
    # =========================
    def test_caso_4_porcentaje(self):
        # Entrada
        edad = 95.0
        # Cálculo
        resultado = calcular_porcentaje_financiado(edad)
        # Verificación
        self.assertEqual(resultado, 70)

    def test_caso_4_plazo(self):
        # Entrada
        edad = 95.0
        # Cálculo
        resultado = calcular_plazo_financiacion(edad)
        # Verificación
        self.assertEqual(resultado, 3)

    def test_caso_4_pago_mensual(self):
        # Entrada
        porcentaje_financiado = 70
        valor_vivienda = 10_000_000.0
        plazo = 3
        # Cálculo
        resultado = calcular_pago_mensual(porcentaje_financiado, valor_vivienda, plazo)
        # Verificación
        self.assertAlmostEqual(resultado, 194444.44444444444, places=6)
        
    def test_caso_4_intereses(self):
        # Entrada
        edad = 95.0
        valor_vivienda = 10_000_000.0
        # Cálculo
        pf = calcular_porcentaje_financiado(edad)
        plazo = calcular_plazo_financiacion(edad)
        pago = calcular_pago_mensual(pf, valor_vivienda, plazo)
        intereses, _ = calcular_intereses(pago, TASA_EFECTIVA_MENSUAL, plazo * 12)
        # Verificación
        self.assertAlmostEqual(intereses, 183328.1798740009, places=2)


if __name__ == "__main__":
    unittest.main()
