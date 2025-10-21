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
    
    def test_insertar_y_buscar(self):
        solicitante_prueba = solicitante(nombre="Beatriz Elena Montoya", 
            identificacion="1022345678",
            fecha_nacimiento= datetime.strptime("1953-03-12", "%Y-%m-%d").date(), 
            edad=72)
        
        controlador_solicitante.insertar(solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('1022345678')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))

if __name__ == '__main__':
    unittest.main()
