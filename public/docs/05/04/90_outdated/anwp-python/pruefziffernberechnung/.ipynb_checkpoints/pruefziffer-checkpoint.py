# Prüfziffernberechnung für Kreditkartennummern am Beispiel 934257186670199
def checkCreditcard(number):
    sum = 0
    parity = len(number) % 2
    for i, digit in enumerate(int(x) for x in number):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum += digit
    return sum % 10 == 0

number = input ('Bitte geben Sie die Kreditkartennummer ein: ')
print (checkCreditcard(number))
