def steuer(gehalt):
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18
    return steuerbetrag
