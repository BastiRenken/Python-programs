#!/usr/bin/python3
# Anleitung
print("")
print("Dieses Programm berechnet die Veränderung der Frequenz auf Grund des Dopplereffekts.")
# Lichtgeschwindigkeit in m/s
c = 334.0
# Eingabe
status = "j"
while status == "j":
    f = input("Frequenz in Hz: ")
    f = float(f)
    v = input("Geschwindigkeit in m/s: ")
    v = float(v)
    print("Bewegen sich Schallquelle und Beobachter voneinander [w]eg oder aufeinander [z]u?")
    richtung = input("").lower()
    while richtung != "w" and richtung != "z":
        print("Geben sie w oder z ein.")
        richtung = input("").lower()
    print("Bewegt sich die [S]challquelle oder der [B]eobachter?")
    bewegung = input("").lower()
    while bewegung != "s" and bewegung != "b":
        print("Geben sie S oder B ein.")
        bewegung = input("").lower()
# Berechnung
    if bewegung == "s":
        if v >= c:
            print("Überschallknall")
        else:
            if richtung == "w":
                scheinfrequenz = f * (c / (c + v))
            elif richtung == "z":
                scheinfrequenz = f * (c / (c - v))
    elif bewegung == "b":
        if richtung == "w":
            scheinfrequenz = f * ((c - v) / c)
        elif richtung == "z":
            scheinfrequenz = f * ((c + v) / c)
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
