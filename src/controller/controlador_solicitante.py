import sys
sys.path.append("src")

from model.solicitante import solicitante
import psycopg2


class controlador_solicitante:
    def Insertar(solicitante: solicitante):
        """Inserta una instancia de la clase solicitante en la tabla solicitante"""
        
        conexion = psycopg2.connect(
            database="hipoteca_inversa",
            user="administrador",
            password="cY4Xt4NkCkvTiDmkKirF1BHohFExcqF9",
            host="pg-d3ir973e5dus739bs8ig-a.virginia-postgres.render.com",
            port=5432
        )
        
        cursor = conexion.cursor()

        sql = """
        INSERT INTO solicitante (
            nombre_solicitante, 
            identificacion_solicitante, 
            fecha_nacimiento_solicitante, 
            edad_solicitante
        ) VALUES (%s, %s, %s, %s);
        """

        valores = (
            solicitante.nombre_solicitante,
            1012345678,
            '1980-02-10',
            45
        )

        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()

    def Buscar(nombre_solicitante: str) -> solicitante:
        pass
