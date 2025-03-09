import string, secrets

li = []
for i in range(10):
    li.append(secrets.randbelow(6) + 1)
print("Zehnmal würfeln:", li)

tx = ""
for i in range(10):
    tx += secrets.choice(string.ascii_lowercase)
print("Text mit zehn zufälligen kleinen Buchstaben:", tx)
