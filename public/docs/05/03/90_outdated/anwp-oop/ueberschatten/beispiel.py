class Basis():

    def anzeige(self,parameter):  # Überschatten
        print("Hallo, ein Parameter")

    def anzeige(self):
        print("Hallo, kein Parameter")

b = Basis()
b.anzeige("Tag")