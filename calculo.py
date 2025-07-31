
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
    return None

def calcular_pago_mensual(porcentaje_financiado, valor_vivienda, plazo):
    return None

def calcular_valor_financiado(porcentaje_financiado, valor_vivienda):
    return None

def calcular_intereses(tasa_efectiva_anual, pago_mensual):
    return None

def probar_porcentaje_financiado():
    #Entradas
    edad = 68
    
    #Proceso de prueba
    resultado_funcion_porcentaje_financiado = calcular_porcentaje_financiado(edad)
    
    #Verificacion
    resultado_esperado_porcentaje_financiado = 30
    if resultado_funcion_porcentaje_financiado == resultado_esperado_porcentaje_financiado:
        print("resultado correcto")
    else:
        print("Resultado incorrecto")

probar_porcentaje_financiado()
