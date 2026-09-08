# Aplicación de SOLID en la Aseguradora

En este ejercicio se aplican los cinco principios SOLID para organizar el
programa de la aseguradora y facilitar su mantenimiento, modificación y
extensión.

## S — Single Responsibility Principle

El principio de responsabilidad única busca que cada clase tenga una
responsabilidad principal.

En nuestro programa, la clase `Asegurado` se encarga de representar y
almacenar los datos de cada asegurado. Por otro lado, `CalculadoraPrima` se
encarga de realizar los cálculos relacionados con la edad ajustada, el factor
de edad y la prima.

También se separó el funcionamiento del tipo de cambio en
`ServicioTipoCambio`.

Por ejemplo:

* `Asegurado` → almacena los datos del asegurado.
* `CalculadoraPrima` → calcula la prima.
* `ServicioTipoCambio` → proporciona la tasa de cambio.
* Las funciones `pedir_edad`, `pedir_sexo`, `pedir_fumador`,
  `pedir_extra_prima` y `pedir_suma_asegurada` → validan y capturan datos.

De esta forma, cada parte del programa tiene una responsabilidad definida.

## O — Open/Closed Principle

El principio abierto/cerrado indica que el programa debe poder extenderse sin
tener que modificar constantemente el código que ya funciona.

En nuestro programa se aplica mediante `FactorEdadStrategy` y sus clases
hijas `FactorFemenino` y `FactorMasculino`.

La clase `CalculadoraPrima` recibe una estrategia para obtener el factor:

```python
calculadora.calcular_prima(asegurado, estrategia)
```

Esto permite agregar una nueva categoría de asegurado creando otra clase que
herede de `FactorEdadStrategy`, sin tener que modificar el funcionamiento de
`CalculadoraPrima`.

Por ejemplo, podría agregarse otra estrategia:

```python
class OtroFactor(FactorEdadStrategy):
    def obtener_factor(self, edad):
        return 2.1
```

La calculadora no tendría que modificarse para aceptar esta nueva estrategia.

## L — Liskov Substitution Principle

El principio de sustitución de Liskov indica que las clases hijas deben poder
utilizarse en los lugares donde se espera su clase padre sin romper el
funcionamiento del programa.

En nuestro programa, `FactorFemenino` y `FactorMasculino` heredan de
`FactorEdadStrategy` y ambas implementan el método `obtener_factor`.

Por esta razón, `CalculadoraPrima` puede recibir cualquiera de las dos:

```python
estrategia = FactorFemenino()
```

o:

```python
estrategia = FactorMasculino()
```

y utilizar el mismo método:

```python
estrategia.obtener_factor(edad)
```

Las dos clases cumplen con el comportamiento definido por
`FactorEdadStrategy`.

## I — Interface Segregation Principle

El principio de segregación de interfaces busca evitar interfaces demasiado
grandes que obliguen a una clase a implementar métodos que no necesita.

En nuestro programa utilizamos clases base sencillas y específicas. Por
ejemplo, `FactorEdadStrategy` únicamente define el comportamiento necesario
para obtener un factor de edad:

```python
class FactorEdadStrategy:
    def obtener_factor(self, edad):
        return 0
```

De igual forma, `FuenteTipoCambio` se enfoca únicamente en proporcionar una
tasa de cambio:

```python
class FuenteTipoCambio:
    def obtener_tasa(self):
        return 21.13
```

Cada abstracción tiene una función concreta y no obliga a implementar
funcionalidades innecesarias.

## D — Dependency Inversion Principle

El principio de inversión de dependencias indica que las clases principales
no deberían depender directamente de implementaciones concretas.

En nuestro programa, `CalculadoraPrima` recibe la fuente del tipo de cambio
desde fuera:

```python
class CalculadoraPrima:
    def __init__(self, fuente_tipo_cambio):
        self.fuente_tipo_cambio = fuente_tipo_cambio
```

Después utiliza esa dependencia:

```python
tasa = self.fuente_tipo_cambio.obtener_tasa()
```

Esto permite sustituir la fuente del tipo de cambio sin modificar
`CalculadoraPrima`.

Por ejemplo, podríamos crear otra clase con otro valor o servicio de tipo de
cambio y utilizarla de la misma manera.

## Resumen

| Principio                         | Aplicación en nuestro programa                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------ |
| **S — Responsabilidad Única**     | Las clases y funciones tienen responsabilidades separadas.                                       |
| **O — Abierto/Cerrado**           | `FactorEdadStrategy` permite agregar nuevas estrategias sin modificar `CalculadoraPrima`.        |
| **L — Sustitución de Liskov**     | `FactorFemenino` y `FactorMasculino` pueden utilizarse como estrategias de `FactorEdadStrategy`. |
| **I — Segregación de Interfaces** | Las abstracciones utilizadas contienen solamente los comportamientos necesarios.                 |
| **D — Inversión de Dependencias** | `CalculadoraPrima` recibe `fuente_tipo_cambio` desde fuera en lugar de crearla directamente.     |
