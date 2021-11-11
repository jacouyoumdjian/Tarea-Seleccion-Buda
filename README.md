# TAREA DE SELECCIÓN | Buda.com - Metro

### Autor: Joaquín Couyoumdjian | [@jacouyoumdjian](https://www.github.com/jacouyoumdjian)

## Estructura del repositorio

```
project
│__ 📂tests
|__ ⚙️.gitignore
│__ 📑README.md
│__ 💻classes.py
│__ 💻main.py
│__ 💻main_test.py

```

## Lenguaje de programación

Python :snake:.

## Decisiones de Diseño

- Se utilizó una Programación Orientada a Objetos (Clases) para modelar las estaciones y la simulación de la ruta más corta.

- Para el almacenamiento de los datos, se utilizaron diccionarios para que el acceso a la información sea más eficiente. En esta línea, la complejidad global del algoritmo es O(n^2).

## Ejecución del programa

Para ejecutar el programa se debe introducir el siguiente comando:

`py main.py <ruta\archivo_input.txt>`

Por ejemplo: `py main.py tests\input.txt`

Luego, en la ejecución misma, se solicitará introducir por consola los siguiente parámetros:

- Una estación inicial de las que se muestra en consola (Ej: A, B, ...).
- Una estación final de las que se muestra en consola (Ej: A, B, ...).
- (Opcional) Un color de tren Rojo o Verde ingresando 0 o 1 respectivamente. Sino no se escoge un color, solamente presione "Enter".

## Formato del archivo de entrada (_input_)

A continuación, se presente el formato del archivo que recibe el programa como input. Este es un archivo de texto (.txt) que representa una red de metro y todas las líneas del archivo tienen el siguiente el formato:

`NODO,COLOR_DEL_NODO;VECINO_1,VECINO_2,...,VECINO_N`

A modo de ejemplo, un posible archivo `input.txt` sería:

```
A,SinColor;B
B,Verde;A,C
C,Rojo;B
```

## Salida (_output_)

El output de salida del programa se visualiza por consola y corresponde a la menor ruta según los parámetros indicados anteriormente. El output representa todas las estaciones que componen la ruta. Un ejemplo de output sería:

```
A -> B -> C -> H -> F
```

## Manejo de Errores

Los principales errores manejados en el código son los casos en que:

- Se ingresan valores para la estación inicial, final o para el color de tren que generan una ruta que no es alcanzable. Por ejemplo, en el caso de que se quiera llegar desde una estación inicial sin color a una estación final color verde con un tren de color rojo. También, el caso de que se ingrese una estación que no pertenezca a la red de metro mostrada en consola. Para estos casos se imprime en pantalla: `Los valores ingresados generan una ruta no alcanzable`.

- Se ingresa un color para el tren que no corresponde a: sin color, rojo o verde. Para este caso se imprime en pantalla: `Se ingresó un valor para el color del tren incorrecto, por favor inténtelo de nuevo`.

## Ejecución de tests automáticos

Para correr los tests automáticos se debe ejecutar el siguiente comando:

`py main_test.py`

Los tests se construyeron con la lógica de calcular la ruta más corta entre dos estaciones fijas para distintas redes de metros, probando con cada uno de los posibles colores de tren (sin color, rojo o verde). Las rutas obtenidas se comparan con las respuestas presentes en el archivo `tests\output.txt` indicando por consola el resultado del test (CORRECTO o INCORRECTO).

Tanto el archivo `output.txt` como los archivos de prueba que representan las distintas redes de metro, se encuentran en la carpeta `tests`. Cada línea del archivo `output.txt` contiene las respuestas correctas para cada red de metro con el siguiente formato:

`RUTA_CORRECTA_TREN_SIN_COLOR;RUTA_CORRECTA_TREN_ROJO;RUTA_CORRECTA_TREN_VERDE`

Los archivos de prueba corresponden a archivos de texto que tienen el formato mencionado en el apartado _input_.

## Supuestos de Modelación

- En términos de la simulación de las estaciones, no habrán dos estaciones del mismo color seguidas. Si pueden haber estaciones sin color seguidas.

## Referencias

- https://newbedev.com/how-to-iterate-over-files-in-a-given-directory
- https://pencilprogrammer.com/algorithms/shortest-path-in-unweighted-graph-using-bfs/
- https://www.tutorialspoint.com/python/python_command_line_arguments.htm
- https://docs.pytest.org/en/6.2.x/
