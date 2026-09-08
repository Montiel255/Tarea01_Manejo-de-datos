# Investigación PEP8

PEP8 es la guía de estilo de Python. Su objetivo es establecer convenciones que permitan escribir código claro, consistente, legible y fácil de mantener.

## 1. Indentación

Se deben utilizar **4 espacios** para cada nivel de indentación. Esto permite identificar fácilmente la estructura del programa.

### Antes

```python
if edad >= 18:
  print("Es mayor de edad")
```

### Después

```python
if edad >= 18:
    print("Es mayor de edad")
```

En el segundo ejemplo se utilizan 4 espacios, siguiendo la recomendación de PEP8.

---

## 2. Longitud máxima de línea

PEP8 recomienda que las líneas de código tengan como máximo **79 caracteres**. Esto facilita la lectura y evita que las líneas sean demasiado largas.

### Antes

```python
resultado = calcular_prima(asegurado, suma_asegurada, factor_edad, tipo_seguro)
```

### Después

```python
resultado = calcular_prima(
    asegurado,
    suma_asegurada,
    factor_edad,
    tipo_seguro
)
```

La instrucción se divide en varias líneas para mejorar la legibilidad.

---

## 3. Espacios alrededor de operadores

Se recomienda colocar **un espacio a cada lado de los operadores** como `=`, `+`, `-`, `*`, `/`, `==`, `<` y `>`.

### Antes

```python
prima=SA*K/1000
```

### Después

```python
prima = SA * K / 1000
```

La operación es la misma, pero la segunda versión es más fácil de leer.

---

## 4. Líneas en blanco

Las líneas en blanco se utilizan para separar diferentes partes lógicas del código, como funciones y clases. Esto ayuda a organizar visualmente el programa.

### Antes

```python
def calcular_prima(sa, factor):
    return sa * factor / 1000
def mostrar_resultado(prima):
    print("Prima:", prima)
```

### Después

```python
def calcular_prima(sa, factor):
    return sa * factor / 1000


def mostrar_resultado(prima):
    print("Prima:", prima)
```

La línea en blanco permite distinguir mejor las dos funciones.

---

## 5. Importaciones

Las instrucciones `import` deben colocarse al inicio del archivo, antes del resto del código. Además, se recomienda escribir las importaciones separadas cuando son módulos diferentes.

### Antes

```python
import math, random

def calcular_area(radio):
    return math.pi * radio ** 2
```

### Después

```python
import math
import random


def calcular_area(radio):
    return math.pi * radio ** 2
```

La segunda versión hace más claras las dependencias utilizadas por el programa.

---

## 6. Nombres de variables y funciones

PEP8 recomienda utilizar **`snake_case`** para los nombres de variables y funciones. Esto significa utilizar letras minúsculas y separar las palabras con guiones bajos.

### Antes

```python
def calcularPrima(sumaAsegurada):
    primaTotal = sumaAsegurada * 2.0 / 1000
    return primaTotal
```

### Después

```python
def calcular_prima(suma_asegurada):
    prima_total = suma_asegurada * 2.0 / 1000
    return prima_total
```

La segunda versión sigue la convención de nombres recomendada para Python.

---

## 7. Constantes en mayúsculas

Las constantes deben escribirse utilizando **letras mayúsculas** y, cuando tienen varias palabras, se deben separar mediante guiones bajos.

### Antes

```python
tipo_cambio = 21.13
```

### Después

```python
TIPO_CAMBIO = 21.13
```

El nombre en mayúsculas permite identificar que se trata de un valor que se espera que permanezca constante.

---

## 8. Comentarios

Los comentarios deben ser **claros y útiles**. Su propósito es proporcionar información que ayude a comprender el código y no simplemente repetir lo que ya es evidente.

### Antes

```python
edad = 20  # asignamos 20 a edad
```

### Después

```python
edad = 20  # Edad mínima permitida para calcular el seguro
```

El segundo comentario aporta información adicional sobre el propósito del valor.

---

## 9. Docstrings

Las funciones, clases y módulos pueden documentarse mediante **docstrings**. Una docstring permite explicar directamente el propósito de un elemento del programa.

### Antes

```python
def calcular_prima(sa, factor):
    return sa * factor / 1000
```

### Después

```python
def calcular_prima(sa, factor):
    """Calcula la prima anual de un seguro."""
    return sa * factor / 1000
```

La docstring permite entender rápidamente qué hace la función.

---

## 10. Una instrucción por línea

Se recomienda escribir **una instrucción por línea** en lugar de colocar varias instrucciones separadas por punto y coma. Esto facilita la lectura y modificación del código.

### Antes

```python
edad = 25; fumador = "No"; sexo = "F"
```

### Después

```python
edad = 25
fumador = "No"
sexo = "F"
```

Cada instrucción queda claramente separada.

---

## Fuente

Python Software Foundation. *PEP 8 – Style Guide for Python Code*.

https://peps.python.org/pep-0008/
