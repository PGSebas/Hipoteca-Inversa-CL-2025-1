# Hipoteca-Inversa-CL-2025-1

## Prerequisitos

- Python 3.12. Puede instalarse desde [python.org](https://www.python.org/) o con `sudo apt install python3.12`.

Este programa permite calcular la cuota mensual que recibirá un adulto mayor (a partir de los 65 años) a través de una hipoteca inversa, de acuerdo con los plazos y porcentajes definidos por la entidad bancaria.
Para realizar el calculo se considerará:
- La edad del solicitante: Este determina el plazo de pago y el porcentaje de la vivienda que se usará como garantía.
- Valor de la vivienda: Este es el respaldo del crédito.
- Plazo definido: Tiempo durante el cual el banco pagará la mensualidad, según el rango de edad del solicitante.
- Tasa de interés: Se utiliza la tasa efectiva anual (TEA) del 24.78% establecida por el Banco de la República para el año 2025, convertida a una tasa equivalente mensual de 1.86%  


### Plazo según rango de edad  

| Edad              | Plazo de pago |
|-------------------|---------------|
| 65 – 70 años      |    20 años    |
| 70 – 75 años      |    25 años    |
| 75 – 80 años      |    10 años    |
| 80 – 85 años      |    5 años     |
| 85 – 95 años      |    3 años     |

### Porcentaje de la vivienda usado como respaldo  

| Edad              | Porcentaje del valor de la vivienda |
|-------------------|-------------------------------------|
| 65 – 70 años      |             30%               |
| 70 – 80 años      |             40%               |
| 80 – 85 años      |             55%               |
| Más de 85 años    |             70%               |

### Formulas Aplicadas 

- Conversión de la tasa efectiva anual (TEA) a tasa mensual equivalente:

$$
i_{mensual} = (1 + i_{anual})^{\tfrac{1}{12}} - 1
$$

- Determinación de la cuota mensual:

$$
\text{Cuota mensual} = \frac{\text{Valor del préstamo}}{\text{Número de meses del plazo}}
$$


## Arquitectura del Proyecto

- `src/model`: lógica de cálculo y excepciones.
- `src/view`: interfaz de consola.
- `src/controller`: coordinación entre modelo y vista.
- `tests`: pruebas unitarias.

## Ejecución de la Interfaz

1. Abrir una consola.
2. Navegar a la carpeta del proyecto (`cd Hipoteca-Inversa-CL-2025-1`).
3. Ejecutar `python3 src/view/Interfaz_Hipoteca_Inversa.py`.

## Ejecución de los Tests

Desde la raíz del proyecto, ejecutar:

```bash
python3 -m unittest discover tests
```

## Autores

- Juan Sebastián Pinilla Giraldo  
- Julián David Osorio Londoño  



