st = set([8, 15, "x"])
su = set([4, "x", "abc", 15])
print("st:", st)
print("su:", su)

print("Vereinigungsmenge:", st | su)
print("Schnittmenge:", st & su)
print("Differenzmenge st - su:", st - su)
print("Differenzmenge su - st:", su - st)
print("Symmetrische Differenzmenge:", st ^ su)

