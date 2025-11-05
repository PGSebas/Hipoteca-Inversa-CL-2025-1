from src.controller.controlador_solicitante import ControladorSolicitante
from flask import Flask, request, render_template
import sys

from model.solicitante import Solicitante

sys.path.append("src")
from model import excepciones
from model.calculo import (
    calcular_porcentaje_financiado,
    calcular_plazo_financiacion,
    calcular_pago_mensual,
)

app = Flask(__name__)

@app.route('/')      
def hello():
    return render_template("index.html")

@app.route('/guardar_solicitante')
def guardar_solicitante():
    
    # Crear un solicitante
    solicitante = Solicitante(nombre="", identificacion="", fecha_nacimiento="", edad=0)
    solicitante.nombre = request.args["nombre"]
    solicitante.identificacion = request.args["identificacion"]
    solicitante.fecha_nacimiento = request.args["fecha_nacimiento"]
    solicitante.edad = request.args["edad"]
    
    # Guardarlo en la BD
    ControladorSolicitante.insertar(solicitante)

    return "Solicitante insertado exitosamente"

@app.route('/crear_tablas')
def crear_tablas():
    ControladorSolicitante.crear_tabla()
    return "Tablas creadas exitosamente"

@app.route("/buscar_solicitante")
def buscar_solicitante():
    solicitante_encontrado = ControladorSolicitante.buscar_por_cedula(request.args["identificacion_buscada"])
    return render_template("solitante_buscado.html", solicitante=solicitante_encontrado)


@app.route("/calcular_hipoteca")
def calcular_hipoteca():
        edad = int(request.args["edad"])
        valor_vivienda = float(request.args["valor_vivienda"])

        porcentaje = calcular_porcentaje_financiado(edad)
        plazo = calcular_plazo_financiacion(edad)
        pago_mensual = calcular_pago_mensual(porcentaje, valor_vivienda, plazo)

        return (
            f"<h2>Resultado del cálculo</h2>"
            f"Edad: {edad} años<br>"
            f"Valor de la vivienda: ${valor_vivienda:,.0f}<br>"
            f"Porcentaje financiado: {porcentaje}%<br>"
            f"Plazo: {plazo} años<br>"
            f"<b>Valor mensual recibido: ${pago_mensual:,.0f}</b>"
        )

@app.route('/crear_solicitante')
def crear_solicitante():
    return render_template("crear_solicitante.html")

@app.route('/calculo')
def calculo():
    return render_template("calculo.html")

   
if __name__ == "__main__":
    app.run(debug=True)
