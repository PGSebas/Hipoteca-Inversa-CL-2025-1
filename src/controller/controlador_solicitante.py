import sys
sys.path.append("src")
sys.path.append( "." )

from model.solicitante import solicitante
import psycopg2
import secret_config

class controlador_solicitante:

    def crear_tabla():
        cursor = controlador_solicitante.obtener_cursor()
        with open("sql/crear_tabla_solicitantes.sql", "r", encoding="utf-8") as archivo_sql:
            sql = archivo_sql.read()
            cursor.execute(sql)
            cursor.connection.commit()
    
    def borrar_datos_tabla():
        cursor = controlador_solicitante.obtener_cursor()
        sql = "DELETE FROM solicitantes;"
        cursor.execute(sql)
        cursor.connection.commit()

    def insertar(solicitante: solicitante):
        cursor = controlador_solicitante.obtener_cursor()

        sql = """
        INSERT INTO solicitantes (
            nombre, 
            identificacion, 
            fecha_nacimiento, 
            edad
        ) VALUES (%s, %s, %s, %s);
        """

        valores = (
            solicitante.nombre,
            solicitante.identificacion,
            solicitante.fecha_nacimiento,
            solicitante.edad
        )

        cursor.execute(sql, valores)
        cursor.connection.commit()

    def buscar_por_cedula(identificacion_solicitante: str) -> solicitante:
        cursor = controlador_solicitante.obtener_cursor()
        cursor.execute(f"""select nombre, identificacion, fecha_nacimiento, edad
        from solicitantes where identificacion = '{identificacion_solicitante}'""" )
        fila = cursor.fetchone()
        resultado = solicitante(nombre=fila[0], identificacion=fila[1], fecha_nacimiento=fila[2], edad=fila[3])
        return resultado

    def obtener_cursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER, password=secret_config.PGPASSWORD, host=secret_config.PGHOST, port=secret_config.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor