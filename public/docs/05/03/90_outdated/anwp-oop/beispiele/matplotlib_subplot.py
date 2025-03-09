import matplotlib.pyplot as plt
import math

x = []
y1 = []
y2 = []
i = 0
for i in range(0, 361):
    x.append(i)
    bm = math.radians(i)
    y1.append(math.sin(bm))
    y2.append(math.cos(bm))

figur, (py1, py2) = plt.subplots(2, 1)

py1.plot(x, y1)
py1.set_title("Sinus")
py1.set_xlabel("x")
py1.set_ylabel("sin(x)")
py1.axis([0, 360, -1, 1])
py1.grid(axis="both")

py2.plot(x, y2)
py2.set_title("Kosinus")
py2.set_xlabel("x")
py2.set_ylabel("cos(x)")
py2.axis([0, 360, -1, 1])
py2.grid(axis="both")

plt.show()
