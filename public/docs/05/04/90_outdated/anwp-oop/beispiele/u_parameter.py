def steuer(gehalt):
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18
    print(f"Gehalt: {gehalt} Euro, Steuer: {steuerbetrag} Euro")
    
# Programm
for i in 1800, 2200, 2500, 2900:
    steuer(i)
