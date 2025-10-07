# Codigo Reto 1

def presion_a_altitud(presion_hpa):
    # Fórmula barométrica simplificada
    return 44330 * (1 - (presion_hpa / 1013.25) ** (1/5.255))

# Variables iniciales
primera_iteracion = True
altitud_anterior = 0
dt = 1  # intervalo fijo de 1 segundo

while True:
    entrada = input("Ingrese presión barométrica en hPa (o 'salir'): ")

    if entrada.lower() == "salir":
        print("Programa finalizado.")
        break

    # Validar que la entrada sea un número
    if entrada.replace(".", "").isdigit():
        presion = float(entrada)
    else:
        print("⚠️ Entrada inválida. Intente de nuevo.")
        continue

    # Calcular altitud
    altitud = presion_a_altitud(presion)

    if primera_iteracion:
        print(f"Altitud: {altitud:.2f} m")
        altitud_anterior = altitud
        primera_iteracion = False
    else:
        velocidad_vertical = (altitud - altitud_anterior) / dt
        print(f"Altitud: {altitud:.2f} m, Velocidad vertical: {velocidad_vertical:.2f} m/s")

        altitud_anterior = altitud


