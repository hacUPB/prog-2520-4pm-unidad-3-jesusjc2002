# Simulación de consumo de combustible en vuelo usando if y while

# Entrada inicial
combustible_inicial = float(input("Ingrese la cantidad inicial de combustible (litros o galones): "))
consumo_por_hora = float(input("Ingrese el consumo de combustible por hora (litros/hora o gal/h): "))

# Inicialización
combustible_actual = combustible_inicial

# Bucle de simulación
while combustible_actual > 0:
    entrada_horas = input("Ingrese las horas de vuelo a simular (o 'salir' para terminar): ")

    # Condición de salida manual
    if entrada_horas.lower() == "salir":
        print("Simulación finalizada por el usuario.")
        break

    # Conversión a número
    horas_vuelo = float(entrada_horas)

    # Cálculo del consumo
    consumo_total = consumo_por_hora * horas_vuelo
    combustible_actual -= consumo_total

    # Evitar valores negativos
    if combustible_actual < 0:
        combustible_actual = 0

    # Mostrar combustible restante
    print("Combustible restante:", combustible_actual)

    # Fin automático si se agota el combustible
    if combustible_actual == 0:
        print("¡Combustible agotado! Fin de la simulación.")
        break
