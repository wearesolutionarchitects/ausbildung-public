import fractions

b1 = fractions.Fraction(3, -2)
b2 = fractions.Fraction(1, 4)

b3 = b1 * b2
print(f"{b1} * {b2} = {b3}")
print(f"{b1} / {b2} = {b1 / b2}")
print(f"{b1} + {b2} = {b1 + b2}")
print(f"{b1} - {b2} = {b1 - b2}")
print(f"{b1} + {b2} * {b3}= {b1 + b2 * b3}")
print(f"({b1} + {b2}) * {b3}= {(b1 + b2) * b3}")

b4 = fractions.Fraction(-30, 20)
print(f"{b1} == {b4}: {b1 == b4}")
print(f"{b2} > {b4}: {b2 > b4}")
print(f"{b2} < {b4}: {b2 < b4}")
