# TAREA DE SELECCIÓN | Buda.com - Metro

### Autor: Joaquín Couyoumdjian | [@jacouyoumdjian](https://www.github.com/jacouyoumdjian)

## Descripción

El siguiente programa permita calcular la ruta con menor cantidad de estaciones entre dos estaciones de una red de metro, es decir, la ruta más corta entre dos puntos. Cabe destacar que algunas estaciones de la red de metro pueden tener un color asociado (Rojo o Verde) que indica que un tren exprés de color Verde pasará solo por estaciones sin color o Verde, y un tren exprés de color Rojo pasará solo por estaciones sin color o Roja. Para efectos del código, la red de metro será representada por un archivo _input_ y el resultado de la ejecución correponde a la ruta más corta la cual se imprimirá en pantalla.

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

Para ejecutar el programa se debe introducir el siguiente comando por consola:

`py main.py <ruta\archivo_input.txt>`

Tal como se ilustra, es necesario introducir como parámetro la ruta del archivo que representa una red de metro. Por ejemplo, puede correr el comando: `py main.py tests\input.txt`

Luego, en la ejecución misma, se solicitará introducir por consola los siguiente parámetros:

- Una estación inicial de las que se muestra en consola (Ej: A, B, ...).
- Una estación final de las que se muestra en consola (Ej: A, B, ...).
- (Opcional) Un color de tren Rojo o Verde ingresando 0 o 1 respectivamente. Sino no se escoge un color, solamente presione "Enter".

## Formato del archivo de entrada (_input_)

A continuación, se presente el formato del archivo que recibe el programa como input. Este es un archivo de texto (.txt) que representa una red de metro y todas las líneas del archivo tienen el siguiente formato:

`NODO,COLOR_DEL_NODO;VECINO_1,VECINO_2,...,VECINO_N`

A modo de ejemplo, un posible archivo `input.txt` sería:

```
A,SinColor;B
B,Verde;A,C
C,Rojo;B
```

## Salida (_output_)

El _output_ del programa se visualiza por consola y corresponde a la menor ruta según los parámetros indicados anteriormente. El _output_ representa todas las estaciones que componen la ruta. Un ejemplo de output sería:

```
A -> B -> C -> H -> F
```

## Manejo de Errores

Los principales errores manejados en el código son los casos en que:

- Se ingresan valores para la estación inicial, final o para el color de tren, que generan una ruta que no es alcanzable. Por ejemplo, si es que se quiere llegar desde una estación inicial sin color a una estación final color verde, con un tren de color rojo. También, se maneja el caso de que se ingrese una estación que no pertenezca a la red de metro mostrada en consola. Para estos casos se imprime en pantalla: `Los valores ingresados generan una ruta no alcanzable`.

- Se ingresa un color para el tren que no corresponde a: sin color, rojo o verde. Para este caso se imprime en pantalla: `Se ingresó un valor para el color del tren incorrecto, por favor inténtelo de nuevo`.

## Ejecución de tests automáticos

En el programa se implementan tests automáticos para evaluar la correctitud de las partes más importantes del algoritmo en distintas redes de metro. Para correr los tests automáticos se debe ejecutar el siguiente comando:

`py main_test.py`

Los tests se construyeron con la lógica de calcular la ruta más corta entre dos estaciones fijas para distintas redes de metros, probando con cada uno de los posibles colores de tren (sin color, rojo o verde). Las rutas obtenidas se comparan con las respuestas presentes en el archivo `output.txt` indicando por consola el resultado del test (CORRECTO o INCORRECTO). Las dos estaciones fijas siempre serán las estaciones `A` y `B`, las cuáles se encontrarán siempre a distancias distintas una de la otra dada la configuración única de cada red de metro de prueba.

Tanto el archivo `output.txt` como los archivos de prueba que representan las redes de metro, se encuentran en la carpeta `tests`. Cada línea del archivo `output.txt` contiene las respuestas correctas para cada red de metro con el siguiente formato:

```
RUTA_CORRECTA_TREN_SIN_COLOR;RUTA_CORRECTA_TREN_ROJO;RUTA_CORRECTA_TREN_VERDE
```

Cabe destacar que los archivos de prueba corresponden a archivos de texto que tienen el formato mencionado en el apartado _input_.

## Supuestos de Modelación

- En términos de la simulación de las estaciones, no habrán dos estaciones del mismo color seguidas. Sin embargo, si pueden haber estaciones sin color seguidas.

- Para el cálculo de la ruta más corta con un tren de color (Rojo y Verde), si se consideran estaciones sin color, es decir, no se las salta.

## Referencias

- https://newbedev.com/how-to-iterate-over-files-in-a-given-directory
- https://pencilprogrammer.com/algorithms/shortest-path-in-unweighted-graph-using-bfs/
- https://www.tutorialspoint.com/python/python_command_line_arguments.htm
- https://docs.pytest.org/en/6.2.x/
