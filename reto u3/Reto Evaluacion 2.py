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

    if entrada_velocidad.lower() != "salir":
        velocidad_IAS = float(entrada_velocidad)

        altitud_pies = float(input("Ingrese la altitud en pies: "))
        altitud_miles_pies = altitud_pies / 1000

        velocidad_TAS = velocidad_IAS * (1 + FACTOR_ALTITUD * altitud_miles_pies)
        print("La velocidad verdadera (TAS) es:", velocidad_TAS, "nudos")
