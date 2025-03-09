'''Formel nach § 32a EStG für das Jahr 2024
a) bis 11.604 € (Grundfreibetrag): 0;
b) 11.605 € bis 17.005 €: ESt = (922,98 * y + 1.400) * y;
y = (zvE - 11.604) / 10.000
c) 17.006 € bis 66.760 €: ESt = (181,19 * z + 2.397) * z + 1.025,38;
z = (zvE - 17.005) / 10.000
d) 66.761 € bis 277.825 €: ESt = 0,42 * zvE - 10.602,13;
e) ab 277.826 €: ESt = 0,45 * zvE - 18.936,88.
'''


def einkommensteuer_berechnen():
    valid_input = False
    tries = 3

    while tries > 0 and not valid_input:
        ist_verheiratet = input("Sind Sie verheiratet? (ja/nein):").strip().lower()

        if ist_verheiratet == "ja":
            ehepartner1 = float(input("Bitte geben Sie ihr Jahresbruttoeinkommen ein: "))
            ehepartner2 = float(input("Bitte geben Sie das Jahresbruttoeinkommen ihres Ehepartner ein: "))
#E steht für das Einkommen, bei Ehepaaren werden beide Einkommen addiert und durch 2 geteilt.
#Danach wird die Berechnung ausgeführt nach den Bedingungen die oben stehen
            E = (ehepartner1 + ehepartner2) / 2
            valid_input = True
        elif ist_verheiratet == "nein":
            E = float(input("Bitte geben Sie Ihr Jahresbruttoeinkommen ein: "))
            valid_input = True
        else:
            tries -= 1
            print("Ihre Eingabe ist ungülltig. Bitte antworten Sie mit 'ja' oder 'nein'")

    if not valid_input:
        print("Sie haben zu viele ungültige Eingaben gemacht. Das Programm wird nun beendet.")
        return

    if E <= 11604:
        steuer = 0
    elif 11605 <= E <= 17005:
        y = (E - 11604) / 10000
        steuer = (922.98 * y + 1400) * y
    elif 17006 <= E <= 66760:
        z = (E - 17005) / 10000
        steuer = (181.19 * z + 2397) * z + 1025.38
    elif 66761 <= E <= 277825:
        steuer = 0.42 * E - 10602.13
    else:
        steuer = 0.45 * E - 18936.88
    #Mit round kann man das Ergebnis nach dem Komma festlegen in meinem fall 2 Nachkomma stellen
    print("Das zu versteuernde Einkommen beträgt: **", round(E, 2), "€**")
    print("Die Einkommensteuer beträgt: **", round(steuer, 2), "€**")
    print("Ihr Einkommen abzüglich Steuer beträgt", round(E - steuer,2))

einkommensteuer_berechnen()