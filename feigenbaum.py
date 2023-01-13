# Kurzes Programm zur iterativen Berechnung zur Feigenbaumkonstante
import math

fk = 4.6692
# iterationen = 500000
# letztes_dings = 2
# aktueller_grenzwert = 2

# for i in range(iterationen):
#     letztes_dings = letztes_dings/fk
#     aktueller_grenzwert += letztes_dings

# print(aktueller_grenzwert)

# #3.54507770710658

total = 1

for i in range(100):
    total = total +  (2 / (fk ** i))

print(total)