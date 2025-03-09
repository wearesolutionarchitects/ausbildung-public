# mit lambda Funktionen können wir anonyme Funktionen erstellen
# m ist gebunden

m = 2
b = 3
gerade = lambda x: m * x + b

print(gerade(1))     # output: 5

m=3

print(gerade(1))     # output: 6