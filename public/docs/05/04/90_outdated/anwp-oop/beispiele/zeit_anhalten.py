import time
 
startzeit = time.time()
print("Start:", startzeit)
for i in range(5):
    time.sleep(2)
    print(time.time())
endzeit = time.time()
print("Ende:", endzeit)
 
differenz = endzeit - startzeit
print("Differenz:", differenz)
