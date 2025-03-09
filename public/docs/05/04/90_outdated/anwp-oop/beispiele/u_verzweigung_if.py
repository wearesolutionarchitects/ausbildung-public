print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = float(input())

if gehalt > 2500:
    steuerbetrag = gehalt * 0.22
else:
    steuerbetrag = gehalt * 0.18

print(f"Es ergibt sich eine Steuer von {steuerbetrag} Euro")
