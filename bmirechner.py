# Eingabe
#!/usr/bin/python3

print("Haben sie ihr Idealgewicht?")
masse = float(input("Ihr Gewicht in kg: "))
groesse = float(input("Ihre Größe in m: "))

# Verarbeitung
bmi = masse/groesse**2

# Ausgabe
print("Ihr BMI beträgt:", round(bmi, 2))
if bmi < 18.5:
    print("Sie haben untergewicht.")
if 18.5 <= bmi <= 25:
    print("Sie haben Normalgewicht.")
if 25 < bmi <= 30:
    print("Sie haben Übergewicht.")
if bmi > 30:
    print("Sie leiden unter Adipositas.")
