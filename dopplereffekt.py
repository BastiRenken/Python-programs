#!/usr/bin/python3

# Anleitung
print("Dieses Programm berechnet die Verändereung der Frequenz auf Grund des Dopplereffekts.")
print("Angegeben werden müssen:")
print("- Frequenz des ursprünglichen Tons")
print("- Geschwindigkeit der Schallquelle")
print("")

# Lichtgeschwindigkeit in m/s
c = 334

# Eingabe
frequenz = input("Frequenz in Hz: ")
geschwindigkeit = input("Geschwindigkeit in m/s: ")
print("Bewegt sich die Schallquelle vom Beobachter [w]eg oder zu ihm [h]er")
richtung = input("")
richtung = richtung.lower()
while richtung != "w" and richtung != "h":
    print("Geben sie w oder h ein.")
    richtung = input("")
    richtung = richtung.lower()
