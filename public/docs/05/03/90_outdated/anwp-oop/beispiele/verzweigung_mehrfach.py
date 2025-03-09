import random
random.seed
x = random.randint(-5, 5)
print("x:", x)

if x > 0:
    print("x ist positiv")
elif x < 0:
    print("x ist negativ")
else:
    print("x ist gleich 0")
