def urlaubsanspruch():
    behinderung = int(input("Grad der Behinderung in %: "))
    alter = int(input("Alter: "))
    urlaub = 0 # Initialisierung fehlt im Struktogramm

    if alter > 55:
        urlaub = 32
    else:
        if alter < 18:
            urlaub = 35
        else:
            urlaub = 30

    if behinderung >= 50:
        urlaub += 5 # Alternative urlaub = urlaub + 5

    print(f"Ihr Urlaubsanspruch beträgt {urlaub} Tage.")

urlaubsanspruch()