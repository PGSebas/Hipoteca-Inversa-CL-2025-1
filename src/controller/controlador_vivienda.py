import sys
sys.path.append("src")
sys.path.append( "." )

from model.vivienda import Vivienda
import psycopg2
import secret_config

class ControladorVivienda:

    def crear_tabla():
        cursor = ControladorVivienda.obtener_cursor()
        with open("sql/crear_tabla_viviendas.sql", "r", encoding="utf-8") as archivo_sql:
            sql = archivo_sql.read()
            cursor.execute(sql)
            cursor.connection.commit()
    
    def eliminar_tabla():
        cursor = ControladorVivienda.obtener_cursor()
        sql = "DROP TABLE IF EXISTS viviendas;"
        cursor.execute(sql)
        cursor.connection.commit()
    
    def borrar_datos_tabla():
        cursor = ControladorVivienda.obtener_cursor()
        sql = "DELETE FROM viviendas;"
        cursor.execute(sql)
        cursor.connection.commit()

    def insertar(vivienda: Vivienda):
        """ Recibe un a instancia de la clase Vivienda y la inserta en la tabla respectiva"""
        cursor = ControladorVivienda.obtener_cursor()
        consulta = "INSERT INTO viviendas (ciudad, barrio, direccion, identificacion_propietario, valor) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(consulta, (vivienda.ciudad, vivienda.barrio, vivienda.direccion, vivienda.identificacion_propietario, vivienda.valor))
        cursor.connection.commit()

    def buscar_por_direccion(direccion_vivienda: str) -> Vivienda:
        """ Retorna una instancia de la clase Vivienda con los datos obtenidos de la base de datos
            a partir de la direccion suministrada como parametro """
        cursor = ControladorVivienda.obtener_cursor()
        cursor.execute(f"""select ciudad, barrio, direccion, identificacion_propietario, valor
        from viviendas where direccion = '{direccion_vivienda}'""" )
        fila = cursor.fetchone()
        # Si no se encuentra ninguna fila, retornar None en vez de intentar indexar None
        if fila is None:
            return None

        resultado = Vivienda(ciudad=fila[0], barrio=fila[1], direccion=fila[2], identificacion_propietario=fila[3], valor=fila[4])
        return resultado
    
    def buscar_por_propietario(identificacion_propietario: str) -> list[Vivienda]:
        """ Retorna una lista de instancias de la clase Vivienda con los datos obtenidos de la base de datos
            a partir de la identificacion del propietario suministrada como parametro """
        cursor = ControladorVivienda.obtener_cursor()
        cursor.execute(f"""select ciudad, barrio, direccion, identificacion_propietario, valor
        from viviendas where identificacion_propietario = '{identificacion_propietario}'""" )
        filas = cursor.fetchall()
        if filas is None:
            return 
        resultados = []
        for fila in filas:
            vivienda = Vivienda(ciudad=fila[0], barrio=fila[1], direccion=fila[2], identificacion_propietario=fila[3], valor=fila[4])
            resultados.append(vivienda)
        return resultados
    
    def modificar_datos(vivienda: Vivienda):
        """Actualiza los datos de una vivienda existente identificada por su direccion."""
        cursor = ControladorVivienda.obtener_cursor()
        consulta = "UPDATE viviendas SET ciudad = %s, barrio = %s, identificacion_propietario = %s, valor = %s WHERE direccion = %s"
        cursor.execute(consulta, (vivienda.ciudad, vivienda.barrio, vivienda.identificacion_propietario, vivienda.valor, vivienda.direccion))
        # Si no se actualizó ninguna fila, indicar que la vivienda no existe
        if cursor.rowcount == 0:
            cursor.connection.rollback()
            raise ValueError(f"No existe vivienda con direccion {vivienda.direccion}")
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
