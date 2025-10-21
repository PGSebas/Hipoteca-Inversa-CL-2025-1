# Hipoteca-Inversa-CL-2025-2

## Autores 

- Juan Sebastian Pinilla Giraldo
- Julián David Osorio Londoño
## Interfaz-Grafica-realizada-por
- Tomás Sepúlveda Giraldo.

## ¿Como Funciona? 
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

 ## Verificar requisitos previos
   - Asegurarse de tener Python 3 en adelante instalado
     
## Ejecución del Proyecto

Para ejecutar la interfaz en consola, utilice el siguiente comando desde una terminal en la raíz del proyecto:

```sh
python src/view/Interfaz_Hipoteca_Inversa.py
```

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias, utilice el siguiente comando desde desde una terminal la raíz del proyecto:

```sh
python -m unittest discover -s tests -p "test_*.py"
```

## Configuración de la base de datos (PostgreSQL)

Este proyecto utiliza PostgreSQL para las tablas `solicitantes` y `viviendas`.

1) Instale la dependencia de Python para PostgreSQL si aún no lo ha hecho:

```powershell
pip install psycopg2
```

2) Configure las credenciales de conexión:
Asegurese de tener una base de datos PostgreSQL y sus respectivos datos de acceso

- Copie `secret_config_sample.py` a `secret_config.py`:

```powershell
copy secret_config_sample.py secret_config.py
```

- Abra `secret_config.py` y complete las variables con los datos de su servidor PostgreSQL:

```python
PGHOST = 'mi_host_de_bd'
PGDATABASE = 'mi_base_de_datos'
PGUSER = 'mi_usuario'
PGPASSWORD = 'mi_contraseña_segura'
PGPORT = 5432
```

3) Crear las tablas en la base de datos (opciones):

- Opción rápida (desde la raíz del repo):

```powershell
python sql\create_tables.py
```

- Opción manual: ejecute los scripts SQL en la carpeta `sql/` en su cliente psql o herramienta preferida. Asegúrese de crear `solicitantes` antes que `viviendas` (por la FK).

4) Ejecutar la interfaz en consola:

```powershell
python src\view\gui_sql_consola\interfaz_sql.py
```

Nota de seguridad: No incluya credenciales reales en el repositorio. Use `secret_config.py` en su entorno local y añada este archivo a `.gitignore` si contiene secretos.

## Arquitectura Del Proyecto 

El proyecto esta desarrollado basandose en la arquitectura MVC (Modelo Vista Controlador) permitiendo separar el proyecto en carpetas utiles para su ejecución: 

Carpeta .VSCODE 

- Es una carpeta creada automáticamente por Visual Studio Code dentro del proyecto; Sirve para guardar configuraciones específicas del proyecto y del editor 

Carpeta SRC

Dentro de esta carpeta hay 3 Subcarpetas: 

Controller: 
- Contienen un archivo __init.py que permite que python reconozca la carpeta como un Módulo y pueda hacer import

Model:

- contiene un archivo __init.py que permite que python reconozca la carpeta como un Módulo y pueda hacer import

- Contienen el archivo calculo.py, el cual es el encargado de realizar todos los cálculos y procesos principales, utiliza la libreria SYS que proporciona funciones y variables que interactúan directamente con el intérprete de Python 

- Contiene el archivo excepciones.py, con este se definen excepciones para manejar distintos errores relacionados con la edad que ingresa un usuario. Esto permitirá controlar de manera específica los errores y mostrar mensajes claros.

View:

- Esta carpeta contiene el archivo Interfaz_Hipoteca_Inversa.py, esta genera la interfaz principal  que interactuará con el usuario y mostrará los resultados, utilizando las funciones de cálculo definidas en calculo.py

Carpeta TESTS: 

- Contiene el archivo test_calculo.py, el cual es un conjunto de pruebas automáticas para verificar que todas las funciones de calculo y las excepciones funcionen correctamente.

## Cómo ejecutar la aplicación gui

1. Clona el repositorio
git clone https://github.com/Sepu2412/Hipoteca-Inversa-CL-2025-1


2. Instala las dependencias

Si tienes un archivo requirements.txt, simplemente ejecuta:

pip install -r requirements.txt


Si no tienes el archivo, puedes instalar Kivy manualmente:

pip install kivy

3. Estructura esperada del proyecto

Asegúrate de que el proyecto tenga una estructura como esta:

.
├── main.py
├── src/
│   └── model/
│       ├── calculo.py
│       └── excepciones.py
└── tests/
    └── test_*.py

4. Ejecuta la aplicación

Desde la raíz del proyecto, corre el siguiente comando:

python main.py


Esto abrirá una ventana gráfica con un formulario para ingresar la edad y el valor de la vivienda, y podrás ver los resultados del cálculo al presionar el botón "Calcular".

python main.py


Se abrirá una ventana gráfica con el formulario para ingresar la edad y el valor de la vivienda, y podrás ver los resultados del cálculo al presionar el botón "Calcular".


