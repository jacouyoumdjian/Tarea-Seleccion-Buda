# TAREA DE SELECCIÓN | Buda.com - Metro

### Autor: Joaquín Couyoumdjian | [@jacouyoumdjian](https://www.github.com/jacouyoumdjian)

## Estructura del repositorio

```
project
│__ 📑README.md
│__ 💻classes.py
│__ 💻main.py
|__ ⚙️.gitignore

```

## Lenguaje de programación

Python :snake:.

## Decisiones de Diseño

- Se utilizaron Programación Orienada a Objetos (Clases) para modelar las estaciones y la simulación de la ruta más corta.
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

A continuación, se presente el formato del archivo que recibe el programa como input. Este es un archivo de texto (.txt) y todas las líneas del archivo tienen el mismo formato conteniendo:

`NODO,COLOR_DEL_NODO;VECINO_1,VECINO_2,...,VECINO_N`

A modo de ejemplo, el archivo `input.txt` sería:

```
A,SinColor;B
B,VERDE;A,C
C,ROJO;B
```

## Salida (_output_)

El output de salida del programa se visualiza por consola y corresponde a la menor ruta según los parámetros indicados anteriormente. El output representa todas las estaciones que componen la ruta. Un ejemplo de output es:

```
A -> B -> C -> H -> F
```

## Ejecución de tests automáticos

blabla

## Supuestos

- En términos de los inputs de entrada, en el caso de que se ingrese un color de tren, este no puede ser un color distinto al de la estación inicial y final, para así mantener un coherencia de la simulación.

- Para términos de la simulación de las estaciones, no habrán dos estaciones del mismo color seguidas. Si pueden haber estaciones sin color seguidas.
