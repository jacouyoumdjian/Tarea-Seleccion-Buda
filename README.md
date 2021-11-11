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

- Para el almacenamiento de los datos, se utilizaró diccionarios para que el acceso a la información sea más eficiente. En esta línea, la complejidad global del algoritmo es O(n^2).

- En el caso de los tests automáticos se construyeron con la lógica de probar para distintas redes de metros, cuál sería la ruta más corta entre dos estaciones fijas para cada uno de los posibles colores de trenes (sin color, rojo o verde).

## Ejecución del programa

Para ejecutar el programa se debe introducir el siguiente comando:

`py main.py <ruta\archivo_input.txt>`

Por ejemplo: `py main.py tests\input.txt`

Luego, en la ejecución misma, se solicitará introducir por consola los siguiente parámetros:

- Una estación inicial de las que se muestra en consola (Ej: A, B, ...).
- Una estación final de las que se muestra en consola (Ej: A, B, ...).
- (Opcional) Un color de tren Rojo o Verde ingresando 0 o 1 respectivamente. Sino no se escoge un color, solamente presione "Enter".

## Formato del archivo de entrada (_input_)

A continuación, se presente el formato del archivo que recibe el programa como input. Este es un archivo de texto (.txt) que represente una red de metro y todas las líneas del archivo tienen el mismo formato, conteniendo:

`NODO,COLOR_DEL_NODO;VECINO_1,VECINO_2,...,VECINO_N`

A modo de ejemplo, el archivo `input.txt` sería:

```
A,SinColor;B
B,Verde;A,C
C,Rojo;B
```

## Salida (_output_)

El output de salida del programa se visualiza por consola y corresponde a la menor ruta según los parámetros indicados anteriormente. El output representa todas las estaciones que componen la ruta. Un ejemplo de output es:

```
A -> B -> C -> H -> F
```

## Manejo de Errores

Los principales errores manejados en el código son los casos en que:

- Se ingresan valores para la estación inicial, final o para color del tren que generan una ruta que no es alcanzable. Por ejemplo, en el caso de que se quiera llegar desde una estación sin color a una color verde con un tres express de color rojo. También, el caso de que se ingrese una estación que no pertenezca a la red de metro mostrada en consola. Para este caso se imprime en pantalla: `Los valores ingresados generan una ruta no alcanzable`.

- Se ingresa un color para el tren que no corresponde a: Sin color, rojo o verde.

## Ejecución de tests automáticos

Para correr los tests automáticos se debe ejecutar el siguiente comando:

`py main_test.py`

## Supuestos de Modelación

- Para términos de la simulación de las estaciones, no habrán dos estaciones del mismo color seguidas. Si pueden haber estaciones sin color seguidas.
