control = True

while True:
    print("Menu principal")
    print("A. Calculadora de presion barometrica")
    print("B. Calculadora de velocidad verdadera (TAS)")
    print("C. Simulacion de consumo de combustible en vuelo")
    print("Q. Salir")
    opcion = input("Seleccione una opcion (A, B, C, Q): ").upper()

    match opcion:
        case "A":
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
                    break

                if entrada.replace("-", "").replace(".", "").isdigit():
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
        case "B":
            # Reto evaluacion 2
             
            FACTOR_ALTITUD = 0.02  # Factor simplificado para ajustar velocidad

            # --- PRIMERA ENTRADA ---
            entrada_velocidad = input("Ingrese la velocidad indicada (IAS) en nudos o escriba 'salir' para terminar: ")

            if entrada_velocidad.lower() != "salir":
                velocidad_IAS = float(entrada_velocidad)

                altitud_pies = float(input("Ingrese la altitud en pies: "))
                altitud_miles_pies = altitud_pies / 1000

                velocidad_TAS = velocidad_IAS * (1 + FACTOR_ALTITUD * altitud_miles_pies)
                print("La velocidad verdadera (TAS) es:", velocidad_TAS, "nudos")

                # --- SEGUNDA ENTRADA ---
                entrada_velocidad = input("Ingrese la velocidad indicada (IAS) en nudos o escriba 'salir' para terminar: ")
        case "C":
            # Simulación de consumo de combustible en vuelo usando if y while

            # Entrada inicial
            combustible_inicial = float(input("Ingrese la cantidad inicial de combustible (litros o galones): "))
            consumo_por_hora = float(input("Ingrese el consumo de combustible por hora (litros/hora o gal/h): "))

            # Inicialización
            combustible_actual = combustible_inicial

            # Bucle de simulación
            while combustible_actual > 0:
                entrada_horas = input("Ingrese las horas de vuelo a simular (o '0' para terminar): ")

                # Condición de salida manual
                if entrada_horas == "0":
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
        case "Q":
            print("Saliendo del programa.")
            raise SystemExit
        case _:
            print("Opción no válida. Intente de nuevo.")
