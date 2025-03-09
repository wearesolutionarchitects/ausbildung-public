print("Zahl:")
x = 12.5
y = x
print("dasselbe Objekt:", x is y)
y = 15.8
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

print("String:")
x = "Robinson"
y = x
print("dasselbe Objekt:", x is y)
y = "Freitag"
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

print("Liste:")
x = [23,"hallo",-7.5]
y = x
print("dasselbe Objekt:", x is y)
y[1] = "welt"
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)

y = ["abc",12.8,"xyz"]
print("dasselbe Objekt:", x is y)
