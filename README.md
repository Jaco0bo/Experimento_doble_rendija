#### Andrés Sepúlveda y Jesus Jauregui

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

## Fotos del experimento
   
![image](https://github.com/Jaco0bo/Experimento_doble_rendija/assets/142515732/105c051e-2565-4cb8-be72-a2ab74e3f1e7)

![WhatsApp Image 2023-10-05 at 8 13 32 AM](https://github.com/Jaco0bo/Experimento_doble_rendija/assets/142515732/d9914cae-e700-4a9a-b871-01f611708119)

![WhatsApp Image 2023-10-05 at 8 50 43 AM](https://github.com/Jaco0bo/Experimento_doble_rendija/assets/142515732/370bf24c-92a3-42fa-b32d-659542b721f7)

## Explicación
### Experimento Clásico de la Doble Rendija:
En el experimento clásico de la doble rendija, se tiene una fuente de partículas (por ejemplo, partículas de luz o canicas) que se disparan hacia una barrera con dos rendijas. Detrás de la barrera, hay una pantalla receptora que registra las partículas que llegan.

- Una Rendija Abierta: En un primer experimento, solo se abre una de las dos rendijas, mientras que la otra permanece cerrada. Las partículas se disparan hacia la barrera y pasan a través de la rendija abierta. En la pantalla receptora, se forma un patrón de impacto que corresponde a la rendija abierta.

- Otra Rendija Abierta: En un segundo experimento, se cierra la rendija que estaba abierta previamente y se abre la otra rendija. Ahora, las partículas pasan a través de la segunda rendija y crean un patrón de impacto en la pantalla receptora que corresponde a la segunda rendija.

- Ambas Rendijas Abiertas: En el tercer experimento, ambas rendijas están abiertas al mismo tiempo. Aquí es donde ocurre algo interesante. En lugar de ver la suma de los patrones de impacto de los dos experimentos anteriores, se observa un patrón de interferencia, similar a las crestas y valles en una onda. Las partículas parecen comportarse como ondas y muestran una interferencia constructiva y destructiva en la pantalla receptora, lo que resulta en un patrón de franjas alternas brillantes y oscuras.

