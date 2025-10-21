import datetime


class Solicitante  :
    def __init__(self,nombre: str,
        identificacion: str,
        fecha_nacimiento: datetime.date,
        edad: int):
        self.nombre: str = nombre
        self.identificacion: str = identificacion
        self.fecha_nacimiento: datetime.date = fecha_nacimiento
        self.edad: int = edad

    def is_equal(self, otra: "Solicitante") -> bool:
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