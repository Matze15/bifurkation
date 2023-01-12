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
# kann zu performance Problemen im Browser kommen, das Ausrechnen an sich geht relativ flott
# Die Grafik wird angezeigt, das Interagieren (zoomen etc) kann aber laggen
start_x = 0.5
intervall = 0.001
max_x_pro_r = 600

# Liste mit r-werten generieren
r_values = []
for i in np.arange(0, 4, intervall):
    # Wert anhängen und runden (Python und Addition sind nicht best friends, z.B.: .1 + .2 = 0.30000000000000004)
    r_values.append(round(i, f'{intervall}'[::-1].find('.')))

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

    # Iterationen-Counter zurücksetzen, wenn mehr als max_x_pro_r Werte gefunden werden, keine
    # weiteren Werte berechnen
    its = 0
    while current_x not in x_values and its < max_x_pro_r:

        # neue x werte an die x_values liste hängen
        x_values.append(current_x)

        # das aktuelle x updaten:
        current_x = r * current_x * (1 - current_x)

        its += 1
    
    its = 0

    # x Werte Liste an die "große" Liste anhängen
    x_values_list.append(x_values)

# Da die plotly Bibliothek so funktioniert, muss für jeden y Wert auch ein x Wert existieren,
# es kann nicht einen x-Wert für mehrere y-Werte geben (wie es hier der Fall wäre).
# Deshalb muss der r-Wert in der Liste so oft multipliziert werden, wie er x Werte hat.
r_values_new = []

for i in range(len(r_values)):
    cur = [r_values[i]] * len(x_values_list[i])
    r_values_new.extend(cur)

# Außerdem muss die zweidimensionale Liste x_values_list zu einer eindimensionalen gemacht werden
x_values_list_new = [item for sublist in x_values_list for item in sublist]



# Funktion zum Erstellen des Diagramms
def diagramm(x_werte,y_werte,x_achse,y_achse,titel):
    
    # Dataframe erstellen
    df = pd.DataFrame(dict(
        x = x_werte,
        y = y_werte
    ))

    # Diagramm erstellen
    figure = px.scatter(
        df,
        x = 'x',
        y = 'y',
        labels={
            'x' : x_achse,
            'y' : y_achse
        },
        title = titel
    )
    figure.update_traces(marker={'size':1})

    # Im Browser anzeigen
    figure.show()


if __name__ == "__main__":
   diagramm(r_values_new, x_values_list_new, 'Reproduktionsfaktor r', 'Population nach 300+ Jahren ("Gleichgewichtspopulation")', 'Bifurkationsdiagramm für xn+1 = r * xn * (1 - xn)')