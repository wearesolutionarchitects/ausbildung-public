print("5>3:", 5>3)
print("5<3:", 5<3)
print("Typ von 5>3:", type(5>3))

print("Zahl -0.1:", bool(-0.1))
print("Zahl 0:", bool(0))

print("String 'Hallo':", bool("Hallo"))
print("String '':", bool(""))

print("Liste [2,8]:", bool([2,8]))
print("Liste []:", bool([]))

print("Tupel (2,8):", bool((2,8)))
print("Tupel ():", bool(()))

print("Dictionary {'Julia':28, 'Werner':32}:",
      bool({"Julia":28, "Werner":32}))
print("Dictionary {}:", bool({}))

print("Set (2,8,2):", bool(set([2,8,2])))
print("Set ():", bool(set([])))
