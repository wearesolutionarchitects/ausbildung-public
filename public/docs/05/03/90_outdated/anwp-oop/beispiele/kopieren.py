import copy

x = [23,"hallo",-7.5]
y = []
for i in x:
    y.append(i)
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

x = [23,["Berlin","Hamburg"],-7.5,12,67]
y = copy.deepcopy(x)
print("dasselbe Objekt:", x is y)
print("gleicher Inhalt:", x == y)
