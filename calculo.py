#Constantes
TASA_EFECTIVA_ANUAL = 0.2478 # Esta expresando en decimal (24.78 %)
TASA_EFECTIVA_MENSUAL = ((1+TASA_EFECTIVA_ANUAL)**(1/12))-1 # Resultado expresado en decimmal

def calcular_porcentaje_financiado(edad):
    #Calcula el porcentaje a financiar del total de la vivienda en funcion de la edad del interesado
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 65:
        raise ValueError("La edad debe ser mayor o igual a 65 años")
    if edad >= 65 and edad < 70:
        return 30
    if edad >= 70 and edad < 80:
        return 40
    if edad >= 80 and edad < 85:
        return 55
    if edad >= 85:
        return 70


def calcular_plazo_financiacion(edad):
    #Calcula el plazo en años en el que el banco pagara las cuotas al usuario funcion de la edad del interesado
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
    #Calcula el plazo en el que el banco pagara las cuotas al usuario funcion de la edad del interesado
    if valor_vivienda < 0:
        raise ValueError("El valor de la vivienda no puede ser negativo")
    if valor_vivienda == 0:
        raise ValueError("El valor de la vivienda no puede ser cero")
    if porcentaje_financiado <= 0:
        raise ValueError("El porcentaje financiado debe ser mayor que cero")
    return (valor_vivienda * porcentaje_financiado / 100) / (plazo * 12)

def calcular_valor_financiado(porcentaje_financiado, valor_vivienda):
    #Calcula el valor de la hipoteca respecto al porcentaje fianciado
    valor_financiado = (porcentaje_financiado/100) * valor_vivienda
    return valor_financiado

def calcular_intereses(pago_mensual, tasa_mensual, numero_cuotas, saldo_inicial=0.0):
    #Calcula el interés total y el saldo final con dicho interes
    
    saldo = float(saldo_inicial)
    for _ in range(numero_cuotas):
        interes_mes = saldo * tasa_mensual
        saldo += interes_mes + pago_mensual

    interes_siguiente = saldo * tasa_mensual
    saldo_final = saldo + interes_siguiente
    return interes_siguiente, saldo_final