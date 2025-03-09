def steuer(gehalt):
    return gehalt * 0.22 if gehalt > 2500 else gehalt * 0.18
    
# Programm
for i in 1800, 2200, 2500, 2900:
    print(f"Gehalt: {i} Euro, Steuer: {steuer(i)} Euro")
