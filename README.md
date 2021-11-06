# TAREA DE SELECCIÓN - BUDA

### Autor: Joaquín Couyoumdjian | [@jacouyoumdjian](https://www.github.com/jacouyoumdjian)

## Estructura del repositorio

```
project
│__ 📑README.md
│__ 💻main.py
|__ ⚙️.gitignore

```

## Lenguaje de programación

Python :snake:.

## Decisiones de Diseño

- Se utilizaron clases (Programación Orienada a Objetos) para modelar las estaciones y la simulación de la ruta más corta.
- Para almacenar los datos, se utilizaron diccionarios para que el acceso a la información sea lo más eficiente posible.

## Ejecución del programa

Para ejecutar el programa se debe introducir por consola los siguiente parámetros:

- Una estación inicial de las que se muestra en consola (Ej: A, B, ...).
- Una estación final de las que se muestra en consola (Ej: A, B, ...).
- (Opcional) Un color de tren Rojo o Verde ingresando 0 o 1 respectivamente. Sino no se escoge un color, solamente presione "Enter".

## Formato del archivo de entrada (_input_)

A continuación, se presente el formato del archivo que recibe el programa como input. Todas las líneas del archivo tienen el mismo formato y contiene:

`NODO,COLOR_DEL_NODO;VECINO_1,VECINO_2,...,VECINO_N`

Un ejemplo de archivo sería:

```
A,SinColor;B
B,VERDE;A,C
C,ROJO;B
```

## Salida (_output_)

El output de salida del programa se visualiza por consola y corresponde a la menor ruta según los parámetros, indicando todas las estaciones
que la componen. Un ejemplo de output es:

```
A -> B -> C -> H -> F
```

## Supuestos

- En términos de los inputs de entrada, la estación inicial y final no pueden ser de un color distinto al color del tren que se ingresó como input, para así mantener la coherencia de la simulación.

- Para términos de la simulación de las estaciones, no habrán dos estaciones del mismo color seguidas. Si pueden haber estaciones sin color seguidas.
