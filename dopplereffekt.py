#!/usr/bin/python3
# Anleitung
print("")
print("Dieses Programm berechnet die Verändereung der Frequenz auf Grund des Dopplereffekts.")
# Lichtgeschwindigkeit in m/s
c = 334.0
# Eingabe
status = "j"
while status == "j":
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
    if v >= c:
        print("Überschallknall")
    else:
        if richtung == "w":
            scheinfrequenz = f * (c / (c - v))
        elif richtung == "h":
            scheinfrequenz = f * (c / (c + v))
# Ausgabe
        print("Die registrierte Frequenz beträgt %f Hz." % scheinfrequenz)
        print("")
# Wiederholung
    print("Nochmal? [J]a [N]ein")
    status = input("").lower()
    while status != "j" and status != "n":
        print("Geben Sie J oder N ein.")
        status = input("").lower
        print("")
