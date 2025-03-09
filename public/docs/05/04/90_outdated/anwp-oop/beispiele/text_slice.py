tx = "Hallo Welt"
print("Text:", tx)

print("[2:7]:", tx[2:7])
print("[:7]:", tx[:7])
print("[2:]:", tx[2:])
print("[:]:", tx[:])
print("[1]:", tx[1])
print("[1:-2]:", tx[1:-2])
print()

print("[2:7:2]:", tx[2:7:2])
s = slice(2, 7, 2)
print("[2:7:2]:", tx[s])
a = 2
b = 7
print("[2:7:2]:", tx[a:b:a])
