def berechne_nettopreis(materialeinsatz, materialgemeinkostenzuschlag, fertigungsstunden, stundensatz, gemeinkostenzuschlag, gewinn):
    ''' Berechnung des Nettoangebotspreises'''
    # Ausgabe Materialeinsatz
    print(f"Materialeinsatz: {materialeinsatz:.2f} €")
    # Berechnung des Materialkostenzuschlagsbetrag
    material_zuschlag = (materialeinsatz * materialgemeinkostenzuschlag) / 100
    print(f"+Gemeinzuschlagsatz (Material): {materialgemeinkostenzuschlag} %, {material_zuschlag:.2f} €")
    # Berechnung der Materialkosten
    materialkosten = materialeinsatz + material_zuschlag
    print(f"=Materialkosten: {materialkosten:.2f} €")
    # Berechnung der Fertigungslöhne
    fertigungsloehne = fertigungsstunden * stundensatz
    print(f"+{fertigungsstunden} Mitarbeiterstunden a {stundensatz} €, {fertigungsloehne:.2f} €")
    # Berechnung der Gemeinkosten
    gemeinkosten = (fertigungsloehne * gemeinkostenzuschlag) / 100
    print(f"+Gemeinkostenzuschlagsatz: {gemeinkostenzuschlag} %, {gemeinkosten:.2f} €")
    # Berechnung der Selbstkosten
    selbstkosten = fertigungsloehne + gemeinkosten + materialkosten
    print(f"=Selbstkosten: {selbstkosten:.2f} €")
    # Berechnung des Gewinns
    gewinn_betrag = (selbstkosten * gewinn) / 100
    print(f"+{gewinn} % Gewinn: {gewinn_betrag:.2f} €")
    # Berechnung des Nettoangebotspreises
    nettoangebotspreis = selbstkosten + gewinn_betrag
    print(f"Nettoangebotspreis: {nettoangebotspreis:.2f} €")

    return nettoangebotspreis


# Eingabe der Parameter
materialeinsatz = float(input("Bitte Materialeinsatz in € eingeben: "))
materialgemeinkostenzuschlag = float(
    input("Bitte den Materialgemeinkostenzuschlagssatz in % eingeben: "))
fertigungsstunden = float(input("Bitte die Fertigungsstunden eingeben: "))
stundensatz = float(
    input("Bitte den durchschnittlichen Stundensatz in € eingeben: "))
gemeinkostenzuschlag = float(
    input("Bitte den Gemeinkostenzuschlagssatz in % eingeben: "))
gewinn = float(input("Bitte den Gewinn in % eingeben: "))

# Aufruf der Berechnungsfunktion mit Wert für 'gewinn'
nettobetrag = berechne_nettopreis(materialeinsatz, materialgemeinkostenzuschlag,
        fertigungsstunden, stundensatz, gemeinkostenzuschlag, gewinn)
