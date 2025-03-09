z = [12, 7, 38, -5]
print("Liste:", z)

z[2] = 16
print("Element durch Element ersetzt:", z)

z[1:3] = [43, -8, 72]
print("Slice durch Liste ersetzt:", z)

del z[2]
print("Element entfernt:", z)

del z[2:]
print("Slice entfernt:", z)

z[0] = [-28, 19]
print("Element durch Liste ersetzt:", z)
