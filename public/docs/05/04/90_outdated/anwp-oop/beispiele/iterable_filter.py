def positiv(a):
    if a>0:
        return True
    else:
        return False

z = filter(positiv, [5, -6, -2, 0, 12, 3, -5])
for element in z:
    print(element)
print(type(z))

