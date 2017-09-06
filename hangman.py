#!/usr/bin/python3
import os

status = 1
wort = []
anzeige = []
speicher = []
stelle = []

print("Wir spielen Galgenmännchen!")
eingabe = input("Zu erratendes Wort eingeben: ")
os.system("clear")
eingabe = eingabe.lower()
wort.extend(eingabe)

for i in range(len(eingabe)):
    anzeige.append("_ ")
ausgabe = ("".join(anzeige))
print(ausgabe)

anzeige = []
print("Buchstabe eingeben")
while status == 1:
    buchstabe = input("")
    buchstabe = buchstabe.lower()
    for j in len(wort):
        if wort[j] == buchstabe:
            anzeige.append(wort[j])
        else:
            anzeige.append("_ ")
        ausgabe = ("".join(anzeige))
        print(ausgabe)
