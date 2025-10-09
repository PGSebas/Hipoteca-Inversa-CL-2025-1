class solicitante  :
    def __init__(self,nombre_solicitante,
        identificacion_solicitante,
        fecha_nacimiento_solicitante,
        edad_solicitante):
        self.nombre_solicitante = nombre_solicitante
        self.identificacion_solicitante = identificacion_solicitante
        self.fecha_nacimiento_solicitante = fecha_nacimiento_solicitante
        self.edad_solicitante = edad_solicitante

    def is_equal (self, otra ) -> bool : 
        "Compara si dos instancias de la clase solicitante son iguales"
        return False