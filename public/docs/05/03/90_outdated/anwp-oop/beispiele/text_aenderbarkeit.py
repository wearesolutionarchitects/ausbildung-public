tx = "Das ist ein Text"
print(tx)

try:
    tx[4:6] = "war"
except:
    print("Fehler")

tx = tx[:4] + "war" + tx[7:]
print(tx)
