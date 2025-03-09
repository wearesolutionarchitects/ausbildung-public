import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []
i = -5
while i < 5.05:
    x.append(i)
    y1.append(i * i)
    y2.append(0.5 * i * i)
    i += 0.1

plt.plot(x, y1, label="y1(x) = x * x")
plt.plot(x, y2, label="y2(x) = 0.5 * x * x")
plt.title("Funktionen")
plt.legend()
plt.xlabel("x")
plt.ylabel("y(x)")
plt.axis([-5, 5, 0, 25])
plt.grid(axis="both")
plt.axhline(9, color="red")
plt.axvline(3, color="green")
plt.show()
