# Investigación: Principios SOLID

## ¿Qué es SOLID?

SOLID es un conjunto de cinco principios utilizados en el diseño de
programas orientados a objetos. Su propósito es ayudar a construir código
más fácil de entender, mantener, modificar, probar y extender.

El nombre SOLID está formado por las iniciales de cinco principios:

* **S** — Single Responsibility Principle
* **O** — Open/Closed Principle
* **L** — Liskov Substitution Principle
* **I** — Interface Segregation Principle
* **D** — Dependency Inversion Principle

---

# 1. S — Single Responsibility Principle (SRP)

## Nombre completo

**Single Responsibility Principle (SRP) — Principio de Responsabilidad Única.**

## Problema que busca resolver

Evita que una misma clase tenga varias responsabilidades que no están
relacionadas entre sí. Cuando una clase hace demasiadas cosas, un cambio en
una de ellas puede afectar otras partes del programa.

## Explicación

Una clase debería tener una responsabilidad principal y una razón clara para
cambiar. Esto permite organizar mejor el código y facilita modificar o
probar una parte del programa sin afectar las demás.

## Código que viola el principio

```python
class Asegurado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def calcular_prima(self):
        return 1000

    def guardar_archivo(self):
        print("Guardando asegurado...")

    def enviar_correo(self):
        print("Enviando correo...")
```

La clase `Asegurado` tiene varias responsabilidades:

* Representar los datos del asegurado.
* Calcular la prima.
* Guardar información.
* Enviar correos.

Esto hace que la clase tenga demasiadas razones diferentes para cambiar.

## Código aplicando el principio

```python
class Asegurado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class CalculadoraPrima:
    def calcular(self, asegurado):
        return 1000


class GuardadorAsegurados:
    def guardar(self, asegurado):
        print("Guardando asegurado...")


class Notificador:
    def enviar_correo(self, asegurado):
        print("Enviando correo...")
```

Ahora cada clase tiene una responsabilidad específica:

* `Asegurado` representa los datos del asegurado.
* `CalculadoraPrima` calcula la prima.
* `GuardadorAsegurados` se encarga del almacenamiento.
* `Notificador` se encarga de las notificaciones.

De esta manera, cada clase tiene una responsabilidad más clara y es más
sencillo realizar cambios sin afectar otras partes del programa.

---

# 2. O — Open/Closed Principle (OCP)

## Nombre completo

**Open/Closed Principle (OCP) — Principio de Abierto/Cerrado.**

## Problema que busca resolver

Evita que una clase tenga que modificarse continuamente cada vez que se agrega
un nuevo comportamiento. Modificar código que ya funciona puede introducir
errores en funcionalidades existentes.

## Explicación

Una clase debe estar abierta para extender su comportamiento, pero cerrada
para modificar su código existente. En otras palabras, debemos poder agregar
nuevas funcionalidades sin tener que cambiar constantemente las clases que ya
funcionan.

## Código que viola el principio

```python
class CalculadoraDescuento:
    def calcular(self, tipo_cliente, precio):
        if tipo_cliente == "normal":
            return precio

        elif tipo_cliente == "estudiante":
            return precio * 0.9

        elif tipo_cliente == "adulto_mayor":
            return precio * 0.8
```

Cada vez que aparece un nuevo tipo de cliente tenemos que modificar
`CalculadoraDescuento` y agregar otra condición.

Por ejemplo, si queremos agregar un descuento para docentes, tendríamos que
modificar la clase existente.

## Código aplicando el principio

```python
class Descuento:
    def calcular(self, precio):
        return precio


class DescuentoEstudiante(Descuento):
    def calcular(self, precio):
        return precio * 0.9


class DescuentoAdultoMayor(Descuento):
    def calcular(self, precio):
        return precio * 0.8


class CalculadoraDescuento:
    def calcular(self, precio, descuento):
        return descuento.calcular(precio)
```

Ahora podemos agregar otro comportamiento mediante una nueva clase:

```python
class DescuentoDocente(Descuento):
    def calcular(self, precio):
        return precio * 0.85
```

No fue necesario modificar `CalculadoraDescuento`.

De esta forma, el programa puede extenderse agregando nuevas clases sin
modificar el código que ya funciona.

---

# 3. L — Liskov Substitution Principle (LSP)

## Nombre completo

**Liskov Substitution Principle (LSP) — Principio de Sustitución de Liskov.**

## Problema que busca resolver

Evita que una clase hija tenga un comportamiento incompatible con lo que se
espera de su clase padre. Esto puede provocar errores cuando el programa usa
la clase hija pensando que se comportará como la clase padre.

## Explicación

Si una clase hija hereda de otra clase, debería poder utilizarse en los
lugares donde se espera la clase padre sin romper el funcionamiento del
programa.

La herencia debe representar una relación válida: la clase hija debe poder
cumplir con los comportamientos que promete la clase padre.

## Código que viola el principio

```python
class Ave:
    def volar(self):
        print("Estoy volando")


class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pingüinos no vuelan")
```

Después podemos tener una función que espere que cualquier `Ave` pueda volar:

```python
def hacer_volar(ave):
    ave.volar()


pinguino = Pinguino()
hacer_volar(pinguino)
```

El problema es que `Pinguino` hereda de `Ave`, pero no puede cumplir
correctamente con el comportamiento de `volar()` definido por su clase padre.

## Código aplicando el principio

Podemos separar las aves que tienen la capacidad de volar:

```python
class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        print("Estoy volando")


class Aguila(AveVoladora):
    pass


class Pinguino(Ave):
    pass
```

Ahora la función solicita específicamente un objeto que tenga la capacidad de
volar:

```python
def hacer_volar(ave_voladora):
    ave_voladora.volar()


aguila = Aguila()
hacer_volar(aguila)
```

`Aguila` puede sustituir a `AveVoladora` sin romper el programa, mientras que
`Pinguino` no necesita implementar un comportamiento que no puede realizar.

---

# 4. I — Interface Segregation Principle (ISP)

## Nombre completo

**Interface Segregation Principle (ISP) — Principio de Segregación de
Interfaces.**

## Problema que busca resolver

Evita que una clase tenga que implementar métodos que realmente no necesita.
Esto puede suceder cuando se crea una interfaz demasiado grande con
funcionalidades muy diferentes.

## Explicación

Es mejor tener varias interfaces pequeñas y específicas que una sola
interfaz grande. De esta manera, cada clase implementa solamente los
comportamientos que realmente necesita.

En Python podemos representar esta idea utilizando clases abstractas.

## Código que viola el principio

```python
from abc import ABC, abstractmethod


class Dispositivo(ABC):

    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def escanear(self):
        pass

    @abstractmethod
    def enviar_fax(self):
        pass
```

Una impresora sencilla tendría que implementar los tres métodos aunque solo
necesite imprimir:

```python
class Impresora(Dispositivo):

    def imprimir(self):
        print("Imprimiendo")

    def escanear(self):
        raise NotImplementedError

    def enviar_fax(self):
        raise NotImplementedError
```

La clase `Impresora` está obligada a implementar funcionalidades que no
utiliza.

## Código aplicando el principio

Podemos dividir la interfaz grande en interfaces más pequeñas:

```python
from abc import ABC, abstractmethod


class Imprimible(ABC):

    @abstractmethod
    def imprimir(self):
        pass


class Escaneable(ABC):

    @abstractmethod
    def escanear(self):
        pass


class Faxable(ABC):

    @abstractmethod
    def enviar_fax(self):
        pass
```

Ahora la impresora sencilla solo utiliza la interfaz que necesita:

```python
class Impresora(Imprimible):

    def imprimir(self):
        print("Imprimiendo")
```

Una impresora multifuncional puede implementar varias:

```python
class ImpresoraMultifuncional(Imprimible, Escaneable, Faxable):

    def imprimir(self):
        print("Imprimiendo")

    def escanear(self):
        print("Escaneando")

    def enviar_fax(self):
        print("Enviando fax")
```

Así cada clase implementa únicamente los comportamientos que necesita.

---

# 5. D — Dependency Inversion Principle (DIP)

## Nombre completo

**Dependency Inversion Principle (DIP) — Principio de Inversión de
Dependencias.**

## Problema que busca resolver

Evita que las clases principales dependan directamente de implementaciones
concretas. Cuando existe una dependencia directa, cambiar un componente puede
obligarnos a modificar la clase que lo utiliza.

## Explicación

Las clases principales deberían depender de abstracciones y no directamente
de detalles concretos. Esto permite cambiar una implementación por otra sin
modificar la clase principal.

## Código que viola el principio

```python
class ServicioTipoCambio:
    def obtener_tasa(self):
        return 21.13


class CalculadoraPrima:
    def calcular_usd(self, prima_mxn):
        servicio = ServicioTipoCambio()
        tasa = servicio.obtener_tasa()
        return prima_mxn / tasa
```

`CalculadoraPrima` crea directamente un objeto `ServicioTipoCambio`, por lo
que ambas clases quedan fuertemente relacionadas.

Si cambiamos la forma de obtener el tipo de cambio, tendremos que modificar
`CalculadoraPrima`.

## Código aplicando el principio

Primero creamos una abstracción para la fuente del tipo de cambio:

```python
from abc import ABC, abstractmethod


class FuenteTipoCambio(ABC):

    @abstractmethod
    def obtener_tasa(self):
        pass
```

Después podemos crear una implementación concreta:

```python
class ServicioTipoCambio(FuenteTipoCambio):

    def obtener_tasa(self):
        return 21.13
```

La calculadora recibe la dependencia desde afuera:

```python
class CalculadoraPrima:

    def __init__(self, fuente_tipo_cambio):
        self.fuente_tipo_cambio = fuente_tipo_cambio

    def calcular_usd(self, prima_mxn):
        tasa = self.fuente_tipo_cambio.obtener_tasa()
        return prima_mxn / tasa
```

Podemos utilizarla de esta forma:

```python
servicio = ServicioTipoCambio()
calculadora = CalculadoraPrima(servicio)

print(calculadora.calcular_usd(1000))
```

También podemos crear otra implementación:

```python
class BancoTipoCambio(FuenteTipoCambio):

    def obtener_tasa(self):
        return 20.95
```

La clase `CalculadoraPrima` no necesita modificarse para utilizar esta nueva
fuente.

---

# Conclusión

Los principios SOLID ayudan a organizar mejor los programas orientados a
objetos y a reducir problemas relacionados con cambios, mantenimiento y
extensión del código.

Cada principio aborda un problema diferente:

| Principio                         | Idea principal                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| **S — Responsabilidad Única**     | Una clase debe tener una responsabilidad principal.                                        |
| **O — Abierto/Cerrado**           | Se deben poder agregar comportamientos sin modificar el código existente.                  |
| **L — Sustitución de Liskov**     | Una clase hija debe poder sustituir a su clase padre sin romper el programa.               |
| **I — Segregación de Interfaces** | Una clase no debería estar obligada a implementar métodos que no necesita.                 |
| **D — Inversión de Dependencias** | Las clases principales deben depender de abstracciones y no de implementaciones concretas. |

Estos principios serán utilizados posteriormente en los ejercicios de la
aseguradora y del diccionario para justificar las decisiones de diseño.

# Fuentes consultadas

1. Python Software Foundation. **PEP 8 — Style Guide for Python Code**.
   https://peps.python.org/pep-0008/

2. Real Python. **Design and Guidance: Object-Oriented Programming in Python
   — SOLID Principles**.
   https://realpython.com/courses/solid-principles-python/

3. Real Python. **Design and Guidance: OOP in Python (Overview)**.
   https://realpython.com/videos/solid-principles-python-overview/
