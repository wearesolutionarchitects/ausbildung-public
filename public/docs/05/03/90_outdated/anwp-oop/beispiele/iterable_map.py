def quad(x):
    return x * x

def summe(a,b,c):
    return a + b + c

z = map(quad, [4, 2.5, -1.5])
print("Quadrat:")
for element in z:
    print(element)
print()

z = map(summe, [3, 1.2, 2], [4.8, 2], [5, 0.1, 9])
print("Summe:")
for element in z:
    print(f"{element:.1f}")
print()

print(type(z))
