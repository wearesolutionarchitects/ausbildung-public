import random
random.seed
x = random.randint(-3, 3)
print("x:", x)
 
ausgabe = "positiv" if x>0 else "0 oder negativ"
print("Diese Zahl ist", ausgabe)
 
print("Diese Zahl ist", "positiv" if x>0 else "0 oder negativ")
 
print("Diese Zahl ist", "positiv" if x>0 else "negativ" if x<0 else "gleich 0")
