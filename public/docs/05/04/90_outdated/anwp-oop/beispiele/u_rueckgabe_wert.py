def steuer(gehalt):
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18
    return steuerbetrag
    
# Programm
for i in 1800, 2200, 2500, 2900:
    print(f"Gehalt: {i} Euro, Steuer: {steuer(i)} Euro")
