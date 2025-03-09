import string, secrets

sonder = "!#$%&()*+-/:;<=>?@[]_{|}"
print("Sonderzeichen:", sonder)
alle = string.ascii_letters + string.digits + sonder

while True:
    tx = ""
    anz = [0,0,0,0]
    for i in range(6):
        zeichen = secrets.choice(alle)
        tx += zeichen
        if zeichen in string.ascii_lowercase:
            anz[0] += 1
        elif zeichen in string.ascii_uppercase:
            anz[1] += 1
        elif zeichen in string.digits:
            anz[2] += 1
        else:
            anz[3] += 1
    print("Anzahl:", anz)
    if 0 not in anz:
        break

print("Passwort: ", tx)

