#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
# Anleitung
print("")
print("Dieses Programm berechnet die Veränderung der Frequenz auf Grund des Dopplereffekts.")
# Schallgeschwindigkeit in m/s
c = 334.0
# Variablen für Plot
x = np.arange(0.0, 0.01, 0.00001)
fig = plt.figure(1)
# Eingabe
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
# Plot berechnen und definieren
ax1 = fig.add_subplot(211)
ax1.plot(x, np.sin(1*20*f/10*np.pi*x))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_title("%f Hz" %f)

ax2 = fig.add_subplot(212)
ax2.plot(x, np.sin(scheinfrequenz/f*20*f/10*np.pi*x))
ax2.grid(True)
ax2.set_ylim((-2, 2))
ax2.set_title("%f HZ" %scheinfrequenz)
# Ausgabe
print("Die registrierte Frequenz beträgt %f Hz." %scheinfrequenz)
print("")
#Plot ausgeben
plt.show()
