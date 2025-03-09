name = ["Maier", "Schmitz", "Mertens"]
vorname = ["Hans", "Peter", "Julia"]
personalnummer = [6714, 81343, 2297]
gehalt = [3500.0, 3750.0, 3621.5]
geburtstag = ["15.03.1962", "12.04.1958", "30.12.1959"]

kombi = zip(name, vorname, personalnummer, gehalt, geburtstag)
for element in kombi:
    print(element)
print(type(kombi))


