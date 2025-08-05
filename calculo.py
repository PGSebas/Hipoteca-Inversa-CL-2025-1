
def calcular_porcentaje_financiado(edad):
    #Calcula el porcentaje a financiar del total de la vivienda en funcion de la edad del interesado
    if edad >= 65 and edad <70:
        return 30
    if edad >= 70 and edad <80:
        return 40
    if edad >= 80 and edad <85:
        return 55
    if edad >= 85:
        return 70
    return "Edad Incorrecta"


def calcular_plazo_financiacion(edad):
    #Calcula el plazo en el que el banco pagara las cuotas al usuario funcion de la edad del interesado
    if edad >= 65 and edad <70:
        return 20 
    if edad >= 70 and edad <75:
        return 15
    if edad >= 75 and edad <80:
        return 10
    if edad >= 80 and edad <85:
        return 5
    if edad >= 85:
        return 3

def calcular_pago_mensual(porcentaje_financiado, valor_vivienda, plazo):
    pago = (valor_vivienda * porcentaje_financiado / 100) / (plazo * 12)
    return pago

def calcular_valor_financiado(porcentaje_financiado, valor_vivienda):
    return None

def calcular_intereses(tasa_efectiva_anual, pago_mensual):
    return None

