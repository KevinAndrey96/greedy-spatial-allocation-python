# Bird Nest Allocation Algorithm in Python 🪺

> **Solución algorítmica al problema de asignación espacial voraz (*Greedy Spatial Allocation*):** Ocupación iterativa del punto medio en el intervalo contiguo desocupado más largo.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-Passing_100%25-brightgreen.svg)](test_nests.py)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Tabla de Contenidos
1. [Descripción del Problema](#-descripción-del-problema)
2. [Evolución de Estados Paso a Paso](#-evolución-de-estados-paso-a-paso)
3. [Estrategia Algorítmica y Complejidad](#-estrategia-algorítmica-y-complejidad)
4. [Aplicaciones en Sistemas Distribuidos e Ingeniería](#-aplicaciones-en-sistemas-distribuidos-e-ingeniería)
5. [Pruebas Automatizadas](#-pruebas-automatizadas)
6. [Instalación y Ejecución](#-instalación-y-ejecución)
7. [Autor](#-autor)

---

## 📖 Descripción del Problema

Se dispone de una hilera de $N$ nidos inicialmente vacíos, representados por un arreglo booleano o caracteres `_`. En cada paso, un ave elige anidar en una posición respetando una regla voraz (*greedy strategy*):

> **Regla de Ocupación:** Cada nueva ave elige ubicarse **en la posición central del intervalo contiguo desocupado más largo**. Si existen múltiples intervalos con la misma longitud máxima, se prioriza el primero de izquierda a derecha.

Este proceso se repite hasta que todos los $N$ nidos quedan completamente ocupados (`X`).

---

## 📊 Evolución de Estados Paso a Paso

Para una hilera de $N = 10$ nidos (índices `0` al `9`):

| Paso | Estado de los Nidos | Intervalo Elegido | Índice Ocupado | Explicación |
| :---: | :--- | :---: | :---: | :--- |
| **0** | `_ _ _ _ _ _ _ _ _ _` | `[0..9]` (Longitud 10) | - | Estado inicial vacío. |
| **1** | `_ _ _ _ _ X _ _ _ _` | `[0..9]` (Longitud 10) | **5** | Punto medio de 10 posiciones: $0 + \lfloor 10 / 2 \rfloor = 5$. |
| **2** | `_ _ X _ _ X _ _ _ _` | `[0..4]` (Longitud 5) | **2** | Intervalos disponibles: `[0..4]` (5) y `[6..9]` (4). Gana `[0..4]`. |
| **3** | `_ _ X _ _ X _ _ X _` | `[6..9]` (Longitud 4) | **8** | Intervalos: `[0..1]` (2), `[3..4]` (2), `[6..9]` (4). Gana `[6..9]`. |
| **4** | `_ X X _ _ X _ _ X _` | `[0..1]` (Longitud 2) | **1** | Intervalos: `[0..1]` (2), `[3..4]` (2), `[6..7]` (2). Empate: gana el primero `[0..1]`. |
| **5** | `_ X X _ X X _ _ X _` | `[3..4]` (Longitud 2) | **4** | Intervalos: `[3..4]` (2), `[6..7]` (2). Gana `[3..4]`. |
| **6** | `_ X X _ X X _ X X _` | `[6..7]` (Longitud 2) | **7** | Intervalo disponible más largo: `[6..7]`. |
| **7** | `X X X _ X X _ X X _` | `[0..0]` (Longitud 1) | **0** | Empate de intervalos unitarios: `0`, `3`, `6`, `9`. Elige `0`. |
| **8** | `X X X X X X _ X X _` | `[3..3]` (Longitud 1) | **3** | Siguiente intervalo unitario. |
| **9** | `X X X X X X X X X _` | `[6..6]` (Longitud 1) | **6** | Siguiente intervalo unitario. |
| **10**| `X X X X X X X X X X` | `[9..9]` (Longitud 1) | **9** | Último nido disponible. |

---

## 🧠 Estrategia Algorítmica y Complejidad

1. **Búsqueda del Intervalo Óptimo (`longest_false_run`):**  
   Recorre el arreglo en tiempo lineal $O(N)$ identificando secuencias contiguas de valores `False`, registrando el inicio y la longitud máxima encontrada.
2. **Asignación del Punto Medio (`occupy_step`):**  
   Calcula la posición objetivo con aritmética de enteros: $\text{mid} = \text{start} + \lfloor \text{length} / 2 \rfloor$.

### Complejidad Computacional:
* **Tiempo:**
  * **Simulación Directa:** $O(N^2)$ al realizar $N$ pasos lineales sobre un arreglo de tamaño $N$.
  * **Optimización con Cola de Prioridad (Max-Heap):** Se puede reducir a $O(N \log N)$ almacenando los intervalos `(longitud, -inicio, fin)` en un heap binario.
* **Espacio Auxiliar:** $O(N)$ para almacenar el estado de los $N$ nidos.

---

## 🌐 Aplicaciones en Sistemas Distribuidos e Ingeniería

El principio subyacente a este problema tiene analogías directas en la ingeniería de software y sistemas distribuidos:

* **Asignación de Carga y Recursos Distribuidos:** Colocación de nuevas instancias de servicios en clústeres para maximizar la distancia y aislar fallos (*Fault Domain Separation*).
* **Gestión de Memoria en Sistemas Operativos:** Variación de algoritmos de asignación dinámica de memoria como *Worst-Fit* o el *Buddy Memory Allocation System*.
* **Planificación Espacial y Logística:** Asignación de puertas de embarque en aeropuertos, bahías de carga o asientos garantizando máxima separación física.

---

## 🧪 Pruebas Automatizadas

El proyecto incluye pruebas unitarias con el módulo nativo `unittest`:

```bash
python3 -m unittest test_nests.py -v
```

Salida esperada:
```text
test_full_simulation (test_nests.TestNests) ... ok
test_longest_false_run (test_nests.TestNests) ... ok
test_occupy_step_sequence (test_nests.TestNests) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

## 💻 Instalación y Ejecución

1. **Clonar repositorio:**
   ```bash
   git clone https://github.com/KevinAndrey96/greedy-spatial-allocation-python.git
   cd greedy-spatial-allocation-python
   ```

2. **Ejecutar simulación:**
   ```bash
   python3 main.py
   ```

3. **Ejecutar tests:**
   ```bash
   python3 -m unittest discover
   ```

---

## 👨‍💻 Autor

**Kevin Andrey Herrera Silva**  
*Senior Backend Engineer & Software Architect*  
* GitHub: [@KevinAndrey96](https://github.com/KevinAndrey96)  
* Email: kahs_kevin@hotmail.com
