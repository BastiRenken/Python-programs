#!/usr/bin/python3

from random import randint

zufallszahl = randint(1, 100)

print("Ich denke an eine Zahl zwischen 1 und 100.")
print("Rate, welche Zahl das ist.")

zahl = int(input("Zahl: "))
counter = 1
while zahl != zufallszahl:
    if zahl < zufallszahl:
        print("Zu klein!")
    else:
        print("Zu groß!")
    zahl = int(input("Zahl: "))
    counter += 1
print("Richtig!")
print("Du hast %d Versuche gebraucht" %counter)
