def fibonacci(x):
    if x==0 or x==1: # Terminiert / Ende
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2) # Wert, typischerweise rekursiver Aufruf (Fibonacci-Zahlen)
 
 
print(fibonacci(4))

# 0,1,1,3,5,8,...

# Rekursionsbaum