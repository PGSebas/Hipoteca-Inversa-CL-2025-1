import sys
sys.path.append("src")
sys.path.append( "." )

from model.solicitante import Solicitante
import psycopg2
import secret_config

class ControladorSolicitante:

    def crear_tabla():
        cursor = ControladorSolicitante.obtener_cursor()
        with open("sql/crear_tabla_solicitantes.sql", "r", encoding="utf-8") as archivo_sql:
            sql = archivo_sql.read()
            cursor.execute(sql)
            cursor.connection.commit()
    
    def eliminar_tabla():
        cursor = ControladorSolicitante.obtener_cursor()
        # Si existe la tabla viviendas, eliminarla primero para evitar dependencias (FK)
        try:
            cursor.execute("DROP TABLE IF EXISTS viviendas;")
        except Exception:
            # Si no existe o falla, continuar
            pass
        sql = "DROP TABLE IF EXISTS solicitantes;"
        cursor.execute(sql)
        cursor.connection.commit()
    
    def borrar_datos_tabla():
        cursor = ControladorSolicitante.obtener_cursor()
        sql = "DELETE FROM solicitantes;"
        cursor.execute(sql)
        cursor.connection.commit()

    def insertar(solicitante: Solicitante):
        """ Recibe un a instancia de la clase Solicitante y la inserta en la tabla respectiva"""
        cursor = ControladorSolicitante.obtener_cursor()
        consulta = "INSERT INTO solicitantes (nombre, identificacion, fecha_nacimiento, edad) VALUES (%s, %s, %s, %s)"
        cursor.execute(consulta, (solicitante.nombre, solicitante.identificacion, solicitante.fecha_nacimiento, solicitante.edad))
        cursor.connection.commit()

    def buscar_por_cedula(identificacion_solicitante: str) -> Solicitante:
        """ Retorna una instancia de la clase Solicitante con los datos obtenidos de la base de datos
            a partir de la cedula suministrada como parametro """
        cursor = ControladorSolicitante.obtener_cursor()
        cursor.execute(f"""select nombre, identificacion, fecha_nacimiento, edad
        from solicitantes where identificacion = '{identificacion_solicitante}'""" )
        fila = cursor.fetchone()
        # Si no se encuentra ninguna fila, retornar None en vez de intentar indexar None
        if fila is None:
            return None

        resultado = Solicitante(nombre=fila[0], identificacion=fila[1], fecha_nacimiento=fila[2], edad=fila[3])
        return resultado

    def modificar_datos(solicitante: Solicitante):
        """Actualiza los datos de un solicitante existente identificado por su cedula."""
        cursor = ControladorSolicitante.obtener_cursor()
        consulta = "UPDATE solicitantes SET nombre = %s, fecha_nacimiento = %s, edad = %s WHERE identificacion = %s"
        cursor.execute(consulta, (solicitante.nombre, solicitante.fecha_nacimiento, solicitante.edad, solicitante.identificacion))
        # Si no se actualizó ninguna fila, indicar que el solicitante no existe
        if cursor.rowcount == 0:
            cursor.connection.rollback()
            raise ValueError(f"No existe solicitante con identificacion {solicitante.identificacion}")
        cursor.connection.commit()

    def obtener_cursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=secret_config.PGDATABASE, 
                                      user=secret_config.PGUSER, 
                                      password=secret_config.PGPASSWORD, 
                                      host=secret_config.PGHOST, 
                                      port=secret_config.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor