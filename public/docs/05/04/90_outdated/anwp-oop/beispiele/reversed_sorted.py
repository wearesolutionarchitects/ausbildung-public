t = 4, 12, 6, -2
print("Tupel:", t)
print("Umgedreht: ", end="")
for i in reversed(t):
    print(i, end=" ")
print()
print("Sortiert:", sorted(t))
print()

dc = {"Peter":31, "Julia":28, "Werner":35}
print("Dictionary:", dc)
va = dc.values()
print("Werte-View:", va)
print("Umgedreht: ", end="")
for i in reversed(va):
    print(i, end=" ")
print()
print("Sortiert:", sorted(va))

