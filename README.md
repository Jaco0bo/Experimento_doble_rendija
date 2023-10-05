# Experimento Doble Rendija

Este es un proyecto que contiene una serie de funciones y archivos relacionados con la simulación de experimentos cuánticos y clásicos, así como operaciones matriciales y vectoriales complejas en Python. A continuación, se describen los elementos clave de este proyecto y cómo utilizarlos.

## Archivos y Funciones

### `gitignore`

Este archivo contiene patrones que se utilizan para excluir archivos y directorios específicos de un repositorio Git. Esto puede incluir archivos temporales, archivos generados por el sistema y otros archivos que no deben incluirse en el control de versiones.

### `Clasico_a_Cuantico.py`

Este archivo contiene tres funciones relacionadas con la simulación de sistemas cuánticos y clásicos:

1. `simula_canicas(dinamica, inicialstate, clicks)`: Simula el experimento de las canicas. Toma una matriz `dinamica` que representa la dinámica del sistema, un vector `inicialstate` que representa el estado inicial y un número de `clicks` para simular la evolución del sistema. Devuelve el estado final.

2. `probabilistico(dinamica, inicialstate, clicks)`: Simula un sistema de rendijas clásico probabilístico. Requiere que la matriz `dinamica` sea doblemente estocástica. Toma también un vector `inicialstate` y el número de `clicks` para simular. Devuelve el estado final.

3. `cuantico(dinamica, inicialstate, clicks)`: Simula un sistema cuántico. Esta función trabaja con matrices que pueden contener valores complejos. Toma la matriz `dinamica`, el vector `inicialstate` y el número de `clicks` para simular. Devuelve el estado final.

4. `grafica(estado)`: Muestra una gráfica de barras que representa las probabilidades en el estado dado.

### `doble_rendija.py`

Este archivo contiene una función `main()` que utiliza las funciones definidas en `Clasico_a_Cuantico.py` para simular un experimento de doble rendija cuántica. Define una matriz de dinámica, un estado inicial y el número de clics para la simulación. Luego, imprime el resultado.

### `vec_and_mat.py`

Este archivo contiene una serie de funciones para realizar operaciones vectoriales y matriciales complejas, incluyendo suma, resta, multiplicación por escalar, producto interno, norma, distancia, valores y vectores propios, y verificación de propiedades de matrices (unitariedad y hermiticidad).

## Como se usa

1. Tener instalado Python.

2. Clona el repositorio Git o descarga los archivos.

3. Utilizar las funciones definidas en `Clasico_a_Cuantico.py` y `vec_and_mat.py` importándolas como módulos.

4. Para ejecutar el experimento de doble rendija cuántica, ejecuta el archivo `doble_rendija.py`.

5. Tener las bibliotecas `numpy` y `matplotlib` instaladas en tu entorno de Python, ya que estas funciones las utilizan.

6. Personaliza los parámetros y matrices para simular diferentes experimentos cuánticos y clásicos.

