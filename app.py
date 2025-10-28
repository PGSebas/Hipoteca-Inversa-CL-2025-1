from flask import Flask, request, render_template
import sys

sys.path.append("src")
from model import excepciones
from model.calculo import (
    calcular_porcentaje_financiado,
    calcular_plazo_financiacion,
    calcular_pago_mensual,
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("formulario.html")

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

   
if __name__ == "__main__":
    app.run(debug=True)
