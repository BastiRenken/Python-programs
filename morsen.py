#!/usr/bin/python3
zeichenliste = [('a', '.-'), ('b', '-...'), ('c', '-.-.'), ('d', '-..'),
('e', '.'), ('f', '..-.'), ('g', '--.'), ('h', '....'), ('i', '..'),
('j', '.---'), ('k', '-.-'), ('l', '.-..'), ('m', '--'), ('n', '-.'),
('o', '---'), ('p', '.--.'), ('q', '--.-'), ('r', '.-.'), ('s', '...'),
('t', '-'), ('u', '..-'), ('v', '...-'), ('w', '.--'), ('x', '-..-'),
('y', '-.--'), ('z', '--..'), ('ä', '.-.-'), ('ö', '---.'), ('ü', '..--'),
('ß', '...--..'), ('1', '.----'), ('2', '..---'), ('3', '...--'),
('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'), ('8', '---..'),
('9', '----.'), ('0', '-----'), (' ', '/'), ('.', '.-.-.-'), (',', '--..--'),
(':', '---...'), ('?', '..--..'), ('-', '-....-'), ('/', '-..-.'),
('+', '.-.-.'), ('=', '-...-'), ('(', '-.--.'), (')', '-.--.-'), ('@', '.--.-.')]

status = 1

print("Willst du:")
print("-[T]ext in Morsecode umwandeln?")
print("oder")
print("-[M]orsecode in Text umwandeln?")

while status == 1:
    antwort = input(" ")
    antwort = antwort.lower()

    if antwort == "t":
        text = input("Text eingeben: ")
        text = text.lower()
        text = list(text)
        morsecode = []
        for i in range(len(text)):
            for j in range(len(zeichenliste)):
                if text[i] == zeichenliste[j][0]:
                    morsecode.extend(zeichenliste[j][1])
                    morsecode.extend(" ")
                    break
        ausgabe = ("".join(morsecode))
        print("Morsecode: ", ausgabe)
        status = 0

    elif antwort == "m":
        morsecode = input("Morsecode eingeben: ")
        morsecode = morsecode.split()
        text = []
        for i in range(len(morsecode)):
            for j in range(len(zeichenliste)):
                if morsecode[i] == zeichenliste[j][1]:
                    text.extend(zeichenliste[j][0])
                    break
        ausgabe = ("".join(text))
        print("Text: ", ausgabe)
        status = 0

    else:
        print("Geben sie T oder M ein und bestätigen sie mit Enter.")


print("Willst du das Ergebnis speichern?")
print("[J]a oder [N]ein")

auswahl = input(" ")
auswahl = auswahl.lower()
if auswahl == "j":
    ergebnis = open("/Users/basti/Desktop/morsecode.txt", "a")
    ergebnis.write(ausgabe)
    ergebnis.close()
    print("Ergebnis wurde unter /Users/basti/Desktop/morsecode.txt gespeichert.")
elif auswahl == "n":
    print("Ergebnis wurde nicht gespeichert.")
else:
    print("Geben sie J oder N ein und bestätigen sie mit Enter.")
