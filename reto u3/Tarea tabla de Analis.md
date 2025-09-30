# Sistema de Cálculo de Altitud y Velocidad Vertical para Aeronave
# Autor: [ Jesus cantillo y Samuel mejia ]
'''
## Se desea desarrollar un sistema de cálculo de altitud y velocidad vertical para una aeronave utilizando como variable de entrada la presión barométrica medida en hPa.

El programa debe:

Solicitar al usuario presiones barométricas sucesivas en hPa (ingresadas con punto decimal).

Convertir cada presión en altitud estimada mediante la fórmula barométrica simplificada
Almacenar las altitudes registradas y calcular, entre cada par de mediciones consecutivas, la velocidad vertical

Mostrar en cada iteración:

La presión ingresada.

La altitud estimada.

El estado de la aeronave: subiendo, descendiendo o nivelado.

Al finalizar, el sistema debe presentar un reporte estadístico del vuelo, incluyendo:

Altitud máxima y mínima.

Velocidad de ascenso máxima.

Velocidad de descenso máxima.

Promedio de velocidad vertical.

El programa debe manejar errores como valores negativos, nulos o entradas no numéricas, mostrando un mensaje adecuado al usuario.

Analisis:

Entradas: Presión barométrica, tiempo del sistema

Proceso principal: Conversión de presión a altitud con la fórmula barométrica simplificada, cálculo de variación de altitud entre dos medidas sucesivas y cálculo de velocidad vertical

Salidas: Altitud estimada (m), velocidad vertical (m/s) y dirección de movimiento (subiendo, bajando, nivelado).

Salidas reporte: Altitud máxima, altitud mínima, velocidad de ascenso máxima, velocidad de descenso máxima y velocidad vertical promedio.

Variables: 
P (Presión)
A_Act (Altitud Actual)
A_Ant (Altitud Anterior)
T (Tiempo)
VV (Velocidad Vertical)
'''

'''
# Consumo de combustible en vuelo

## Enunciado:
Un avión consume combustible a una tasa constante durante el vuelo de crucero. El programa debe pedir al usuario la cantidad inicial de combustible (kg) y el consumo por minuto (kg/min). Luego, en cada iteración, debe mostrar el tiempo transcurrido y la cantidad de combustible restante, hasta que este llegue a cero. Al final, debe indicar el tiempo total de vuelo posible.

Análisis:

CONSUMO DE COMBUSTIBLE

Simulador básico de consumo de combustible
Entradas: 
 - Combustible inicial (kg)
 - Consumo por minuto (kg/min)
Proceso:
 - Repetir resta de combustible en cada minuto usando un bucle
 - Contar minutos hasta que el combustible llegue a 0 o menos
Salidas inmediatas:
 - Combustible restante en cada minuto
 - Tiempo transcurrido
Salida final:
 - Tiempo total de vuelo alcanzado
Variables:
CI (combustible inicial)
CPM (consumo por minuto)
CR (combustible restante)
TT (tiempo transcurrido)
'''

'''
# Distancia recorrida en vuelo

## Enunciado:
Un avión mantiene una velocidad constante durante un trayecto. El programa debe solicitar al usuario la velocidad (km/h) y la duración total del vuelo (h). Con un bucle, debe mostrar la distancia recorrida acumulada cada 30 minutos, hasta completar el tiempo indicado. Finalmente, debe mostrar la distancia total recorrida.

Análisis:

Calculadora de distancia en intervalos
Entradas:
 - Velocidad del avión (km/h)
 - Tiempo total de vuelo (h)
Proceso:
 - Usar un bucle para sumar la distancia recorrida cada 0.5 horas
 - Mostrar la distancia acumulada en cada intervalo
Salidas inmediatas:
 - Distancia acumulada cada 30 minutos
Salida final:
 - Distancia total recorrida
Variables principales:
 V (velocidad)
 TT (tiempo total)
 DA (distancia acumulada)
 INT (intervalo de 0,5 horas)
'''

