print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = float(input())

if gehalt > 4000:
    steuerbetrag = gehalt * 0.26
elif gehalt < 2500:
    steuerbetrag = gehalt * 0.18
else:
    steuerbetrag = gehalt * 0.22

print(f"Es ergibt sich eine Steuer von {steuerbetrag} Euro")
