artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:3, 42:5}
epreis = {23:2.95, 8:1.45, 42:3.05}

print(f"{'Nr':>4}{'Name':>12}{'Anz':>4}{'EP':>13}{'GP':>13}")
for x in 23, 8, 42:
    print(f"{x:04d}{artname[x]:>12}{anzahl[x]:4d}"
          f"{epreis[x]:8.2f} Euro{anzahl[x] * epreis[x]:8.2f} Euro")
