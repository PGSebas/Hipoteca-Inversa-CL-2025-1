from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

import sys
sys.path.append("src")
from src.model import calculo, excepciones


class CalculadoraHipotecaInversa(App):

    def build(self):
        self.contenedor = BoxLayout(orientation='vertical', padding=10, spacing=10)


        self.contenedor.add_widget(Label(text="Edad:"))
        self.input_edad = TextInput(multiline=False)
        self.input_edad.size_hint = (1, None)
        self.input_edad.height = 40
        self.contenedor.add_widget(self.input_edad)


        self.contenedor.add_widget(Label(text="Valor de la vivienda:"))
        self.input_valor = TextInput(multiline=False)
        self.input_valor.size_hint = (1, None)
        self.input_valor.height = 40
        self.contenedor.add_widget(self.input_valor)


        boton_calcular = Button(text="Calcular")
        boton_calcular.bind(on_press=self.calcular)
        self.contenedor.add_widget(boton_calcular)


        self.resultados = Label(text="")
        self.contenedor.add_widget(self.resultados)


        self.input_edad.focus = True

        return self.contenedor

    def calcular(self, instance):
        try:
            edad = int(self.input_edad.text)
            valor_vivienda = float(self.input_valor.text)

            calculo.verificar_valor_vivienda(valor_vivienda)
            porcentaje_financiado = calculo.calcular_porcentaje_financiado(edad)
            plazo_anios = calculo.calcular_plazo_financiacion(edad)
            pago_mensual = calculo.calcular_pago_mensual(
                porcentaje_financiado,
                valor_vivienda,
                plazo_anios
            )
            intereses_totales, saldo_final = calculo.calcular_intereses(
                pago_mensual,
                calculo.TASA_EFECTIVA_MENSUAL,
                plazo_anios
            )

            self.resultados.text = (
                f"Porcentaje financiado: {porcentaje_financiado}%\n"
                f"Plazo en años: {plazo_anios}\n"
                f"Pago mensual: ${pago_mensual:,.2f}\n"
                f"Intereses Totales: ${intereses_totales:,.2f}\n"
                f"Saldo Final: ${saldo_final:,.2f}"
            )

        except ValueError as e:
            self.mostrar_popup("Error de valor", str(e))

        except excepciones.ExcepcionPorEdadIncorrectaNegativa as e:
            self.mostrar_popup("Error de edad", str(e))
        except excepciones.ExcepcionPorEdadIncorrectaMenorAMinimina as e:
            self.mostrar_popup("Error de edad", str(e))
        except excepciones.ExcepcionPorEdadIncorrectaMayorAMaxima as e:
            self.mostrar_popup("Error de edad", str(e))
        except excepciones.ExcepcionPorEdadIncorrectaDecimal as e:
            self.mostrar_popup("Error de edad", str(e))
        except excepciones.ExcepcionPorEdadIncorrectaNoNumerica as e:
            self.mostrar_popup("Error de edad", str(e))
        except excepciones.ExcepcionPorValorViviendaInvalido as e:
            self.mostrar_popup("Error en valor vivienda", str(e))

    def mostrar_popup(self, titulo, mensaje):
        popup = Popup(
            title=titulo,
            content=Label(text=mensaje),
            size_hint=(0.8, 0.4),
            auto_dismiss=True
        )
        popup.open()


if __name__ == "__main__":
    CalculadoraHipotecaInversa().run()
