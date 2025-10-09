import unittest
import sys
sys.path.append( "src" )

from model.solicitante import solicitante
from controller.controlador_solicitante import controlador_solicitante

class testDBsolicitante (unittest.TestCase):
    
    def test_insertar_y_buscar(self):
        solicitante_prueba = solicitante(nombre_solicitante="Beatriz Elena Montoya", 
            identificacion_solicitante="1022345678",
            fecha_nacimiento_solicitante="1953-03-12", 
            edad_solicitante=72)
        
        controlador_solicitante.Insertar (solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.Buscar('Beatriz Elena Montoya')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))

if __name__ == '__main__':
    unittest.main()
