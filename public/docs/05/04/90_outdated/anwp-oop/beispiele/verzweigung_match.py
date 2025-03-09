import random
random.seed()

x = "Paris"
print("Wert =", x)
match x:
    case "Paris":
        print("Frankreich")
    case "Rom":
        print("Italien")
    case "Madrid":
        print("Spanien")
    case _:
        print("Unbekanntes Land")
print()

x = random.randint(1,6)
print("Wert =", x)
match x:
    case 1 | 3 | 5:
        print("ungerade")
    case 2 | 4 | 6:
        print("gerade")
    case _:
        print("Kein Würfelwert")
print()

x = random.randint(1,10)
print("Wert =", x * 1.5)
match x * 1.5:
    case x if x < 5:
        print("kleiner Wert")
    case x if x > 11:
        print("großer Wert")
    case _:
        print("mittlerer Wert")
