#!/usr/bin/python3
status = "j"

# Anleitung
print("Dieses Programm berechnet die Verändereung der Frequenz auf Grund des Dopplereffekts.")
print("Angegeben werden müssen:")
print("- Frequenz des ursprünglichen Tons")
print("- Geschwindigkeit der Schallquelle")
print("")

# Lichtgeschwindigkeit in m/s
c = 334.0

while status == "j":
# Eingabe
    f = input("Frequenz in Hz: ")
    f = float(f)
    v = input("Geschwindigkeit in m/s: ")
    v = float(v)

    print("Bewegt sich die Schallquelle vom Beobachter [w]eg oder zu ihm [h]er")
    richtung = input("").lower()
    while richtung != "w" and richtung != "h":
        print("Geben sie w oder h ein.")
        richtung = input("").lower()

# Berechnung
    if richtung == "w":
        scheinfrequenz = f*(c/(c-v))
    elif richtung == "h":
        scheinfrequenz = f*(c/(c+v))

    print("scheinfrequenz")
    print("Die Scheinfrequenz beträgt %f Hz." %scheinfrequenz)
    print("")

    print("Nochmal? [J]a oder [N]ein")
    status = input("").lower()
    while status != "j" and status != "n":
        print("Geben Sie J oder N ein.")
        status = input("").lower
        print("")
