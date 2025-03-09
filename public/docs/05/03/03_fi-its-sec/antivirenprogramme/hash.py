import hashlib
 
# das eingegebene Passwort als Byte-String
password = input("Geben Sie das Passwort ein: ").encode('utf-8')
 
# generiere den SHA-256-Hash des Passworts
hash_object = hashlib.sha256(password)
hex_dig = hash_object.hexdigest()
 
# gib den Hashwert aus
print(hex_dig)
 
# halte das Ausgabefenster offen, bis eine Eingabe erfolgt
input("Drücken Sie eine beliebige Taste zum Beenden...")