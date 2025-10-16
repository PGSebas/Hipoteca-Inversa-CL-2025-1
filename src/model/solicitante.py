class solicitante  :
    def __init__(self,nombre,
        identificacion,
        fecha_nacimiento,
        edad):
        self.nombre = nombre
        self.identificacion = identificacion
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = edad

    def is_equal(self, otra: "solicitante") -> bool:
        """Compara si dos instancias de la clase solicitante son iguales."""
        if otra is None:
            return False

        return (
            self.nombre == otra.nombre
            and self.identificacion
            == otra.identificacion
            and self.fecha_nacimiento
            == otra.fecha_nacimiento
            and self.edad == otra.edad
        )