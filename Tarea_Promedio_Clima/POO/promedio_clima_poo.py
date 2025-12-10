"""
TRABAJO PRÁCTICO – PROGRAMACIÓN ORIENTADA A OBJETOS
Autor: [Mayra Moran Medina]
Carrera: [Tecnologias de la Información]
Nivel: [Segundo semestre]
Correo: [mm.moranm@uea.edu.ec]

Objetivo:
Calcular el promedio semanal de temperatura aplicando los principios de la POO.
En este ejemplo se aplican:
- Encapsulamiento: atributos privados.
- Abstracción: métodos que simplifican la interacción.
- Polimorfismo: método calcular_promedio redefinido en una subclase.
- (Opcional) Herencia: Clase base ClimaSemana y subclase ClimaExtendido.
"""

# -------------------------------
# CLASE BASE
# -------------------------------
class ClimaSemana:
    def __init__(self):
        self.__temperaturas = []   # Encapsulamiento

    def ingresar_temperaturas(self):
        """
        Método que solicita las temperaturas de 7 días.
        """
        print("INGRESO DE TEMPERATURAS SEMANALES (POO)")
        print("----------------------------------------")

        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def get_temperaturas(self):
        """
        Retorna la lista de temperaturas (solo lectura).
        """
        return self.__temperaturas

    def calcular_promedio(self):
        """
        Método general para calcular el promedio semanal.
        Puede ser sobrescrito por clases hijas (polimorfismo).
        """
        total = sum(self.__temperaturas)
        return total / len(self.__temperaturas)


# -------------------------------
# SUBCLASE CON POLIMORFISMO
# -------------------------------
class ClimaExtendido(ClimaSemana):
    def calcular_promedio(self):
        """
        Ejemplo de polimorfismo:
        Se redefine el cálculo para aplicar una precisión adicional.
        """
        promedio = super().calcular_promedio()
        return round(promedio, 2)


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------
def main():
    clima = ClimaExtendido()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()

    print("\nRESULTADO (POO):")
    print(f"Temperaturas ingresadas: {clima.get_temperaturas()}")
    print(f"Promedio semanal (POO): {promedio}°C")


# EJECUCIÓN
if __name__ == "__main__":
    main()
