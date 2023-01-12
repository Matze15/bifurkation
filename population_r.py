# Import relevanter Module
import pandas as pd
import plotly.express as px

# Einstellungen
settings = {
    "start_x" : None,
    "iterations" : None,
    "r" : None
}

# Input vom Benutzer erhalten, ohne Error-Handling (Fehler können durch falschen User-Input entstehen):
settings['start_x'] = float(input('Populationsstartwert x (0 < x < 1; z.B.: 0.5, .348, 0.96): '))

settings['r'] = float(input('r-Wert (r > 0, z.B.: 1.34, 3, 3.54): '))

settings['iterations'] = int(input('Iterationen (Für wie viele Jahre soll die Population berechnet werden?, z.B.: 5, 22, 1000): '))


# Startwert für x festlegen, x wird im Laufe der Iterationen verändert
x = settings['start_x']

# Liste, in die später die Populationswerte eingetragen werden, erstes x eintragen
x_values = [x]

# Iterationen durchführen
while len(x_values) <= settings['iterations']:

    # Formel anwenden: xn+1 = r * xn (1 - xn)
    x = settings['r'] * x * (1 - x)

    # Neuen x-Wert in die Liste der x-Werte schreiben
    x_values.append(x)

# Liste mit Jahreswerten generieren
years = []
for i in range(settings['iterations'] + 1):
    years.append(i)

# Funktion zum Erstellen eines Diagramms, wobei: x/y_werte: Liste; x/y_achse: Achsenbeschriftung (string)
def graph(x_werte,y_werte,x_achse,y_achse,titel): 

    # Erstellen des Dataframe  
    df = pd.DataFrame(dict(
        x = x_werte,
        y = y_werte,
    ))

    # Erstellen des Diagramms
    figure = px.line(
        df, 
        x = 'x', 
        y = 'y', 
        labels={
            'x' : x_achse,
            'y' : y_achse
        },
        title = titel)

    # Anzeigen des Diagramms im Browser
    figure.show()

if __name__ == '__main__':
    graph(years, x_values, 'Zeit in Jahren', 'Population (Maximalwert 1)', f'Population in Abhängigkeit von der Zeit mit: xn+1 = r * xn * (1 - xn) und r = {settings["r"]}')