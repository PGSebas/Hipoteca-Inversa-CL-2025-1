import unittest
import sys
from datetime import datetime
sys.path.append( "src" )

from model.solicitante import solicitante
from controller.controlador_solicitante import controlador_solicitante

class testDBsolicitante (unittest.TestCase):

    def setUpClass():
        """test fixtures: se ejecuta una vez al inicio de la prueba"""
        controlador_solicitante.borrar_datos_tabla()
    
    def test_insertar_y_buscar_1(self):
        """ Prueba que inserta un solicitante en la base de datos y luego lo busca por su cedula """
        solicitante_prueba = solicitante(nombre="Beatriz Elena Montoya", 
            identificacion="1022345678",
            fecha_nacimiento= datetime.strptime("1953-03-12", "%Y-%m-%d").date(), 
            edad=72)
        
        controlador_solicitante.insertar(solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('1022345678')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))

    def test_insertar_y_buscar_2(self):
        """ Prueba que inserta un solicitante en la base de datos y luego lo busca por su cedula """
        solicitante_prueba = solicitante(nombre="Carlos Andrés Ramírez", 
            identificacion="1098765432",
            fecha_nacimiento= datetime.strptime("1965-07-25", "%Y-%m-%d").date(), 
            edad=65)
        
        controlador_solicitante.insertar(solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('1098765432')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))

    def test_modificar_y_buscar(self):
        """ Prueba que inserta un solicitante en la base de datos, lo modifica y luego lo busca por su cedula """
        solicitante_prueba = solicitante(nombre="Ana María López", 
            identificacion="1011121314",
            fecha_nacimiento= datetime.strptime("1958-11-30", "%Y-%m-%d").date(), 
            edad=65)
        
        controlador_solicitante.insertar(solicitante_prueba)

        # Modificar datos del solicitante
        solicitante_prueba.nombre = "Ana M. López"
        solicitante_prueba.edad = 66

        # Actualizar en la base de datos
        controlador_solicitante.borrar_datos_tabla()
        controlador_solicitante.insertar(solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('1011121314')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))

if __name__ == '__main__':
    unittest.main()
