"""
TRABAJO PRÁCTICO – PROGRAMACIÓN TRADICIONAL
Autor: [Mayra Moran Medina]
Carrera: [Tecnologias de la Informaciön]
Nivel: [Segundo semestre]
Correo: [mm.moranm@uea.edu.ec]

Objetivo:
Calcular el promedio semanal de temperatura utilizando programación tradicional
(procedural). El código se basa en funciones, flujo secuencial y modularidad
sin utilizar objetos.
"""

# -------------------------------
# FUNCIÓN PARA INGRESAR TEMPERATURAS
# -------------------------------
def ingresar_temperaturas():
    """
    Solicita al usuario ingresar las temperaturas diarias durante 7 días.
    Retorna una lista con las temperaturas.
    """
    temperaturas = []
    print("INGRESO DE TEMPERATURAS SEMANALES")
    print("---------------------------------")

    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# -------------------------------
# FUNCIÓN PARA CALCULAR PROMEDIO
# -------------------------------
def calcular_promedio(temperaturas):
    """
    Recibe una lista de temperaturas y calcula el promedio semanal.
    """
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio


# -------------------------------
# FUNCIÓN PRINCIPAL
# -------------------------------
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)

    print("\nRESULTADO:")
    print(f"Las temperaturas ingresadas fueron: {temps}")
    print(f"El promedio semanal es: {promedio:.2f}°C")


# EJECUCIÓN
if __name__ == "__main__":
    main()
