# Import notwendiger Module
import numpy as np
import pandas as pd
import plotly.express as px

# Plan: 
# für jedes 0 > r > 4, Intervall 0.01 (oder später ändern):
# 300 Iterationen "Vorlauf" (sodass sich die Bevölkerung auf Werte eingependelt hat,
# bei denen die Abweichung kleiner ist, als pythons Dezimalstellensupport)
# Dann jedes neue x in Liste eintragen,
# wenn vorhandenes x, Abbrechen
# wenn fertig, Diagramm erstellen (px.scatter)

# Start x festlegen, dieses Programm, nimmt keinen User input
start_x = 0.5

# Liste mit r-werten generieren
r_values = []
for i in np.arange(0, 4, 0.01):
    # Wert anhängen und runden (Python und Addition sind nicht best friends, z.B.: .1 + .2 = 0.30000000000000004)
    r_values.append(round(i, 2))

# In diese Liste kommen später die Listen mit x Werten für die r-Werte:
x_values_list = []

# Für jedes r ausführen:

for r in r_values:

    # Berechnen kann lange dauern:
    print(f'Berechne x-Werte für r = {r}')

    current_x = start_x

    # Leere Liste mit nur den x Werten für das r, wodurch gerade geloopt wird
    x_values = []

    # Iterationen-Counter
    its = 0
    while its <= 300:

        # Formel anwenden (300 mal)
        current_x = r * current_x * (1 - current_x)
        its += 1

    # Iterationen-Counter zurücksetzen, wenn mehr als 300 Werte gefunden werden, keine
    # weiteren Werte berechnen
    its = 0
    while current_x not in x_values and its < 300:

        # neue x werte an die x_values liste hängen
        x_values.append(current_x)

        # das aktuelle x updaten:
        current_x = r * current_x * (1 - current_x)

        its += 1
    
    its = 0
    x_values_list.append(x_values)


def diagramm():
    pass