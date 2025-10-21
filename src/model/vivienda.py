class Vivienda  :
    def __init__(self,
        ciudad: str,
        barrio: str,
        direccion: str,
        identificacion_propietario: str,
        valor: float):
        self.ciudad: str = ciudad
        self.barrio: str = barrio
        self.direccion: str = direccion
        self.identificacion_propietario: str = identificacion_propietario
        self.valor: float = valor

    def is_equal(self, otra: 'Vivienda') -> bool:
        """Compara si dos instancias de la clase vivienda son iguales."""
        if otra is None:
            return False

        return (
            self.ciudad == otra.ciudad
            and self.barrio == otra.barrio
            and self.direccion == otra.direccion
            and self.identificacion_propietario == otra.identificacion_propietario
            and self.valor == otra.valor
        )