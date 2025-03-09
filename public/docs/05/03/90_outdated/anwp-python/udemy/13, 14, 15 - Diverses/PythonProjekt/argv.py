# Thema in dieser Lektion: Wie du Python - Programmen Parameter übergeben kannst

import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]

    file = open(filename, "r")
    counter = 0

    for line in file:
        counter = counter + 1
    print(counter)

else:
    print("Filename missing")