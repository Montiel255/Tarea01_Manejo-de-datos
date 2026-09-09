# Excepciones personalizadas para controlar los datos ingresados


class EdadInvalidaError(Exception):
    """Se utiliza cuando la edad no está entre 18 y 99 años."""
    pass


class SexoInvalidoError(Exception):
    """Se utiliza cuando el sexo ingresado no es M o F."""
    pass


class FumadorInvalidoError(Exception):
    """Se utiliza cuando se ingresa una opción diferente de Si o No."""
    pass


class ExtraPrimaInvalidaError(Exception):
    """Se utiliza cuando el valor de extra-prima no es válido."""
    pass


class SumaAseguradaInvalidaError(Exception):
    """Se utiliza cuando la suma asegurada está fuera del rango permitido."""
    pass


class TasaCambioInvalidaError(Exception):
    """Se utiliza cuando la tasa de cambio es menor o igual a cero."""
    pass


class Asegurado:
    """
    Representa a una persona que contrata un seguro.

    Guarda los datos proporcionados por el usuario y también
    los resultados obtenidos durante el cálculo de la prima.
    """

    def __init__(
        self,
        nombre,
        edad,
        sexo,
        fumador,
        extra_prima,
        suma_asegurada
    ):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.fumador = fumador
        self.extra_prima = extra_prima
        self.suma_asegurada = suma_asegurada

        # Estos valores se calculan posteriormente
        self.edad_ajustada = 0
        self.factor_edad = 0
        self.prima_mxn = 0
        self.prima_usd = 0


class FactorEdadStrategy:
    """
    Clase base para las estrategias de cálculo del factor de edad.

    Permite utilizar diferentes reglas dependiendo del sexo
    del asegurado.
    """

    def obtener_factor(self, edad):
        return 0


class FactorFemenino(FactorEdadStrategy):
    """Calcula el factor de edad para aseguradas."""

    def obtener_factor(self, edad):
        if 18 <= edad < 25:
            return 1.5
        elif 25 <= edad < 45:
            return 1.7
        elif 45 <= edad < 65:
            return 2.0
        elif 65 <= edad <= 99:
            return 2.2


class FactorMasculino(FactorEdadStrategy):
    """Calcula el factor de edad para asegurados."""

    def obtener_factor(self, edad):
        if 18 <= edad < 25:
            return 2.0
        elif 25 <= edad < 45:
            return 2.3
        elif 45 <= edad < 65:
            return 2.5
        elif 65 <= edad <= 99:
            return 3.0


class FuenteTipoCambio:
    """
    Clase base que representa una fuente de información
    para obtener el tipo de cambio.
    """

    def obtener_tasa(self):
        return 21.13


class ServicioTipoCambio(FuenteTipoCambio):
    """
    Proporciona el tipo de cambio utilizado para convertir
    la prima de pesos mexicanos a dólares.
    """

    def __init__(self, tasa=21.13):
        self.tasa = tasa

    def obtener_tasa(self):
        # La tasa de cambio debe ser positiva
        if self.tasa <= 0:
            raise TasaCambioInvalidaError(
                "La tasa de cambio debe ser mayor que cero."
            )

        return self.tasa


class CalculadoraPrima:
    """
    Realiza los cálculos relacionados con la prima del seguro.

    Utiliza una fuente de tipo de cambio para realizar
    la conversión de MXN a USD.
    """

    def __init__(self, fuente_tipo_cambio):
        self.fuente_tipo_cambio = fuente_tipo_cambio

    def calcular_edad_ajustada(self, asegurado):
        """
        Calcula la edad ajustada del asegurado.

        Reglas:
        - Si no fuma, se restan 5 años.
        - Si es mujer, se restan 10 años.
        - Si tiene extra-prima, se agregan 10 años.
        - La edad final se mantiene entre 18 y 99 años.
        """

        edad = asegurado.edad

        if asegurado.fumador == "No":
            edad = edad - 5

        if asegurado.sexo == "F":
            edad = edad - 10

        if asegurado.extra_prima == "Si":
            edad = edad + 10

        # Se limita la edad al rango permitido
        if edad < 18:
            edad = 18

        if edad > 99:
            edad = 99

        return edad

    def calcular_prima(self, asegurado, estrategia):
        """
        Calcula la prima del seguro en pesos mexicanos y dólares.

        Primero obtiene la edad ajustada y el factor correspondiente.
        Después calcula la prima en MXN y finalmente la convierte a USD.
        """

        asegurado.edad_ajustada = self.calcular_edad_ajustada(asegurado)

        # Se obtiene el factor utilizando la estrategia correspondiente
        asegurado.factor_edad = estrategia.obtener_factor(
            asegurado.edad_ajustada
        )

        # Fórmula para calcular la prima
        asegurado.prima_mxn = (
            asegurado.suma_asegurada * asegurado.factor_edad
        ) / 1000

        # Conversión de MXN a USD
        tasa = self.fuente_tipo_cambio.obtener_tasa()

        asegurado.prima_usd = asegurado.prima_mxn / tasa


def pedir_edad():
    """Solicita y valida la edad del asegurado."""

    while True:
        try:
            edad = int(input("Edad (18-99): "))

            if edad < 18 or edad > 99:
                raise EdadInvalidaError(
                    "La edad debe estar entre 18 y 99."
                )

            return edad

        except ValueError:
            print("Error: la edad debe ser un entero.")

        except EdadInvalidaError as error:
            print("Error:", error)


def pedir_sexo():
    """Solicita y valida el sexo del asegurado."""

    while True:
        try:
            sexo = input("Sexo (M/F): ").upper()

            if sexo != "M" and sexo != "F":
                raise SexoInvalidoError(
                    "El sexo debe ser M o F."
                )

            return sexo

        except SexoInvalidoError as error:
            print("Error:", error)


def pedir_fumador():
    """Solicita y valida si el asegurado es fumador."""

    while True:
        try:
            fumador = input("¿Es fumador? (Si/No): ").capitalize()

            if fumador != "Si" and fumador != "No":
                raise FumadorInvalidoError(
                    "Debe escribir Si o No."
                )

            return fumador

        except FumadorInvalidoError as error:
            print("Error:", error)


def pedir_extra_prima():
    """Solicita y valida si el asegurado tiene extra-prima."""

    while True:
        try:
            extra_prima = input(
                "¿Tiene extra-prima? (Si/No): "
            ).capitalize()

            if extra_prima != "Si" and extra_prima != "No":
                raise ExtraPrimaInvalidaError(
                    "Debe escribir Si o No."
                )

            return extra_prima

        except ExtraPrimaInvalidaError as error:
            print("Error:", error)


def pedir_suma_asegurada():
    """Solicita y valida la suma asegurada."""

    while True:
        try:
            suma = float(
                input(
                    "Suma asegurada ($500,000-$3,000,000): "
                )
            )

            if suma < 500000 or suma > 3000000:
                raise SumaAseguradaInvalidaError(
                    "La suma debe estar entre $500,000 y $3,000,000."
                )

            return suma

        except ValueError:
            print("Error: la suma debe ser un número.")

        except SumaAseguradaInvalidaError as error:
            print("Error:", error)


def capturar_asegurado(numero):
    """
    Solicita todos los datos de un asegurado y crea
    un objeto de tipo Asegurado.
    """

    print()
    print("Asegurado", numero)

    nombre = input("Nombre: ")
    edad = pedir_edad()
    sexo = pedir_sexo()
    fumador = pedir_fumador()
    extra_prima = pedir_extra_prima()
    suma_asegurada = pedir_suma_asegurada()

    asegurado = Asegurado(
        nombre,
        edad,
        sexo,
        fumador,
        extra_prima,
        suma_asegurada
    )

    return asegurado


def mostrar_reporte(asegurados):
    """
    Muestra la información de todos los asegurados.

    También calcula:
    - Prima promedio.
    - Prima máxima.
    - Prima mínima.
    - Asegurado con extra-prima y mayor prima.
    """

    print()
    print("REPORTE FINAL")

    suma_primas = 0
    prima_maxima = asegurados[0]
    prima_minima = asegurados[0]
    extra_prima_mas_alta = None

    for asegurado in asegurados:
        print()
        print("Nombre:", asegurado.nombre)
        print("Edad:", asegurado.edad)
        print("Edad ajustada:", asegurado.edad_ajustada)
        print("Sexo:", asegurado.sexo)
        print("Fumador:", asegurado.fumador)
        print("Extra-prima:", asegurado.extra_prima)
        print("Suma asegurada:", asegurado.suma_asegurada)
        print("Factor de edad:", asegurado.factor_edad)
        print("Prima MXN:", asegurado.prima_mxn)
        print("Prima USD:", asegurado.prima_usd)

        suma_primas += asegurado.prima_mxn

        # Busca la prima más alta
        if asegurado.prima_mxn > prima_maxima.prima_mxn:
            prima_maxima = asegurado

        # Busca la prima más baja
        if asegurado.prima_mxn < prima_minima.prima_mxn:
            prima_minima = asegurado

        # Busca al asegurado con extra-prima y mayor prima
        if asegurado.extra_prima == "Si":
            if extra_prima_mas_alta is None:
                extra_prima_mas_alta = asegurado
            elif asegurado.prima_mxn > extra_prima_mas_alta.prima_mxn:
                extra_prima_mas_alta = asegurado

    promedio = suma_primas / len(asegurados)

    print()
    print("Prima promedio:", promedio)
    print("Prima máxima:", prima_maxima.prima_mxn)
    print("Prima mínima:", prima_minima.prima_mxn)

    if extra_prima_mas_alta is not None:
        print(
            "Asegurado con extra-prima más alta:",
            extra_prima_mas_alta.nombre
        )
        print(
            "Prima:",
            extra_prima_mas_alta.prima_mxn
        )
    else:
        print("Ningún asegurado tiene extra-prima.")


def guardar_carnets(asegurados):
    """
    Guarda la información de los asegurados en un archivo
    de texto llamado carnets_asegurados.txt.
    """

    try:
        with open(
            "carnets_asegurados.txt",
            "w",
            encoding="utf-8"
        ) as archivo:

            for asegurado in asegurados:
                archivo.write("CARNET DEL ASEGURADO\n")
                archivo.write("Nombre: " + asegurado.nombre + "\n")
                archivo.write("Edad: " + str(asegurado.edad) + "\n")

                archivo.write(
                    "Edad ajustada: "
                    + str(asegurado.edad_ajustada)
                    + "\n"
                )

                archivo.write("Sexo: " + asegurado.sexo + "\n")

                archivo.write(
                    "Fumador: "
                    + asegurado.fumador
                    + "\n"
                )

                archivo.write(
                    "Extra-prima: "
                    + asegurado.extra_prima
                    + "\n"
                )

                archivo.write(
                    "Suma asegurada: "
                    + str(asegurado.suma_asegurada)
                    + "\n"
                )

                archivo.write(
                    "Factor de edad: "
                    + str(asegurado.factor_edad)
                    + "\n"
                )

                archivo.write(
                    "Prima MXN: "
                    + str(asegurado.prima_mxn)
                    + "\n"
                )

                archivo.write(
                    "Prima USD: "
                    + str(asegurado.prima_usd)
                    + "\n"
                )

                archivo.write("\n")

        print()
        print("Carnets guardados correctamente.")

    except OSError as error:
        print("Error al escribir el archivo:", error)


def main():
    """Función principal que ejecuta todo el programa."""

    print("CALCULADORA DE SEGUROS")
    print()

    # Solicita la cantidad de asegurados
    while True:
        try:
            n = int(
                input(
                    "¿Cuántos asegurados desea capturar? "
                )
            )

            if n <= 0:
                print("Debe ingresar al menos un asegurado.")
            else:
                break

        except ValueError:
            print("Error: debe ingresar un número entero.")

    asegurados = []

    # Se crean los objetos necesarios para realizar los cálculos
    fuente_tipo_cambio = ServicioTipoCambio()
    calculadora = CalculadoraPrima(fuente_tipo_cambio)

    # Captura y procesa cada asegurado
    for i in range(n):
        asegurado = capturar_asegurado(i + 1)

        # Selecciona la estrategia según el sexo
        if asegurado.sexo == "F":
            estrategia = FactorFemenino()
        else:
            estrategia = FactorMasculino()

        # Calcula la prima del asegurado
        calculadora.calcular_prima(
            asegurado,
            estrategia
        )

        asegurados.append(asegurado)

    # Genera el reporte y guarda los carnets
    mostrar_reporte(asegurados)
    guardar_carnets(asegurados)


# Ejecuta el programa únicamente cuando este archivo
# se ejecuta directamente.
if __name__ == "__main__":
    main()
