# Berechnungen zum Populationsmodell nach Verhulst

## Population
Zur Berechnung der Population dient `population_r.py`.
Hierfür wird User-Input in der Konsole/Terminal benötigt.

Außerdem müssen folgende Module installiert sein:

`plotly` : `pip install plotly`

`pandas` : `pip install pandas`

## Bifurkation
`bifurcation.py` ist ein Programm zur Erstellung eines Bifurkationsdiagrammes.
Die Einstellungen müssen direkt in der Datei vorgenommen werden.

Das Programm gibt ein Bifurkationsdiagramm aus. Außerdem wird ein Diagramm generiert, welches die x-Werte pro r-Wert anzeigt. Dieses funktioniert allerdings nicht einwandfrei, da es sich um eine Näherung handelt, und das Unendlichkeitsverhalten nicht untersucht werden kann. Weitere Informationen sind in `bifurcation.py` als Kommentar verfasst.

Folgende Module werden benötigt:

`numpy` : `pip install numpy`

`plotly` : `pip install plotly`

`pandas` : `pip install pandas`

## Feigenbaum
`feigenbaum.py` dient lediglich zur iterativen Berechnung des Feigenbaumpunktes.