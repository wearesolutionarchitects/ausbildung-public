class Ueberladen:
    
    def print(self, txt, name=None):
        if name is None:
            print(txt)
        else:
            print(f"{txt} {name}")

if __name__ == "__main__":
    u = Ueberladen()
    u.print("Mahlzeit")
    u.print("Nabend", "Hiba")