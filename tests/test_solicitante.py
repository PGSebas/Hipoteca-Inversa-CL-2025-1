import unittest
import sys
from datetime import datetime
sys.path.append( "src" )

from model.solicitante import solicitante
from controller.controlador_solicitante import controlador_solicitante

class testDBsolicitante (unittest.TestCase):

    # Test fixtures
    def setUpClass():
        """test fixtures: se ejecuta una vez al inicio de la prueba"""
        controlador_solicitante.eliminar_tabla()
        controlador_solicitante.crear_tabla()
        

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
    
    def test_insertar_y_buscar_3(self):
        """ Prueba que inserta un solicitante en la base de datos y luego lo busca por su cedula """
        solicitante_prueba = solicitante(nombre="Luis Fernando Gómez", 
            identificacion="1032145678",
            fecha_nacimiento= datetime.strptime("1980-05-15", "%Y-%m-%d").date(), 
            edad=43)
        
        controlador_solicitante.insertar(solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('1032145678')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))

    def test_modificar_y_buscar_1(self):
        """ Prueba que modifica los datos de un solicitante en la base de datos y luego lo busca por su cedula """
        solicitante_prueba = solicitante(nombre="Ana María López", 
            identificacion="1034567890",
            fecha_nacimiento= datetime.strptime("1970-11-30", "%Y-%m-%d").date(), 
            edad=70)
        
        controlador_solicitante.insertar(solicitante_prueba)

        # Modificar datos
        solicitante_prueba.nombre = "Ana M. López"
        solicitante_prueba.edad = 71

        controlador_solicitante.modificar_datos(solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('1034567890')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))
    
    def test_modificar_y_buscar_2(self):
        """ Prueba que modifica los datos de un solicitante en la base de datos y luego lo busca por su cedula """
        solicitante_prueba = solicitante(nombre="Jorge Luis Hernández", 
            identificacion="1045678901",
            fecha_nacimiento= datetime.strptime("1960-02-20", "%Y-%m-%d").date(), 
            edad=68)
        
        controlador_solicitante.insertar(solicitante_prueba)

        # Modificar datos
        solicitante_prueba.nombre = "Jorge L. Hernández"
        solicitante_prueba.edad = 69

        controlador_solicitante.modificar_datos(solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('1045678901')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))

    def test_modificar_y_buscar_3(self):
        """ Prueba que modifica los datos de un solicitante en la base de datos y luego lo busca por su cedula """
        solicitante_prueba = solicitante(nombre="María Fernanda Castillo", 
            identificacion="1056789012",
            fecha_nacimiento= datetime.strptime("1975-09-10", "%Y-%m-%d").date(), 
            edad=85)
        
        controlador_solicitante.insertar(solicitante_prueba)

        # Modificar datos
        solicitante_prueba.nombre = "María F. Castillo"
        solicitante_prueba.edad = 86

        controlador_solicitante.modificar_datos(solicitante_prueba)

        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('1056789012')

        self.assertTrue(solicitante_prueba.is_equal(solicitante_encontrado))

    def test_buscar_no_existente(self):
        """ Prueba que busca un solicitante que no existe en la base de datos """
        solicitante_encontrado = controlador_solicitante.buscar_por_cedula('9999999999')
        self.assertIsNone(solicitante_encontrado)

    def test_insertar_duplicado(self):
        """ Prueba que intenta insertar un solicitante con una cedula que ya existe en la base de datos """
        solicitante_prueba = solicitante(nombre="Pedro Pablo Díaz", 
            identificacion="1067890123",
            fecha_nacimiento= datetime.strptime("1985-12-05", "%Y-%m-%d").date(), 
            edad=69)
        
        controlador_solicitante.insertar(solicitante_prueba)

        with self.assertRaises(Exception):
            controlador_solicitante.insertar(solicitante_prueba)

    def test_modificar_no_existente(self):
        """ Prueba que intenta modificar un solicitante que no existe en la base de datos """
        solicitante_prueba = solicitante(nombre="Laura Isabel Moreno", 
            identificacion="1078901234",
            fecha_nacimiento= datetime.strptime("1990-08-22", "%Y-%m-%d").date(), 
            edad=72)
        
        with self.assertRaises(Exception):
            controlador_solicitante.modificar_datos(solicitante_prueba)

if __name__ == '__main__':
    unittest.main()
