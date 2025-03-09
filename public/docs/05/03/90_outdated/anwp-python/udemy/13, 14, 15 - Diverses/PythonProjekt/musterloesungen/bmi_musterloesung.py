# Aufgabe: Schreibe ein Programm, welches die Körpergröße und das Gewicht einer Person abfragt (über input()),
#          und auf Basis dieser Daten dann den BMI ausrechnet und ausgibt.
# Hinweis: Die Formel für den BMI ist wie folgt:
#          BMI = [Gewicht in kg] / [Körpergröße in m]^2

# Schreibe dein Programm hier hinein!

print("BMI - Rechner!")

weight_str = input("Bitte gebe dein Gewicht (in kg) ein: ")
height_str = input("Bitte gebe deine Körpergröße (in m) ein: ")

weight = float(weight_str.replace(",", "."))
height = float(height_str.replace(",", "."))

bmi = weight / height ** 2

print("Der BMI ist: " + str(round(bmi, 1)))