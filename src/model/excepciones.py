class ExcepcionPorEdadIncorrectaNegativa( Exception ):
    """
    Excepción personalizada para indicar que el usuario ingresó una edad negativa 

    """
    def __init__(self, edad_ingresada_por_usuario : int):
        super().__init__( f"Edad ingresada inválida, esta no puede ser negativa y usted ingresó: {edad_ingresada_por_usuario}. Debe ingresar un número entero" )

class ExcepcionPorEdadIncorrectaMenorAMinimina( Exception ):
    """
    Excepción personalizada para indicar que el usuario ingresó una edad menor a la edad minima requerida (65)

    """
    def __init__(self, edad_ingresada_por_usuario : int):
        super().__init__( f"Edad ingresada inválida, esta no puede ser menor a 65 años y usted ingresó: {edad_ingresada_por_usuario}. Su edad debe ser mayor o igual 65 años" )

class ExcepcionPorEdadIncorrectaMayorAMaxima( Exception ):
    """
    Excepción personalizada para indicar que el usuario ingresó una edad mayor a la edad maxima aceptada (115)

    """
    def __init__(self, edad_ingresada_por_usuario : int):
        super().__init__( f"Edad ingresada inválida, esta no puede ser mayor a 115 años y usted ingresó: {edad_ingresada_por_usuario}. Su edad debe ser menor a 115 años" )

class ExcepcionPorEdadIncorrectaDecimal( Exception ):
    """
    Excepción personalizada para indicar que el usuario ingresó una edad decimal y no una entera

    """
    def __init__(self, edad_ingresada_por_usuario : int):
        super().__init__( f"Edad ingresada inválida, esta no puede ser decimal y usted ingresó: {edad_ingresada_por_usuario}. Su edad debe ser un valor entero" )

class ExcepcionPorEdadIncorrectaNoNumerica( Exception ):
    """
    Excepción personalizada para indicar que el usuario ingresó una edad que no es numerica

    """
    def __init__(self, edad_ingresada_por_usuario : int):
        super().__init__( f"Edad ingresada inválida, esta no es numérica y usted ingresó: {edad_ingresada_por_usuario}. Su edad debe ser un valor entero" )
