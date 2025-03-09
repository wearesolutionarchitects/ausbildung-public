import tkinter as tk
from tkinter import ttk, messagebox
from calendar import monthrange
from datetime import datetime

class Restaurant:
    def __init__(self):
        self.tische = [
            {"name": "Tisch 1", "plätze": 4, "reserviert": {}},
            {"name": "Tisch 2", "plätze": 4, "reserviert": {}},
            {"name": "Tisch 3", "plätze": 4, "reserviert": {}},
            {"name": "Tisch 4", "plätze": 4, "reserviert": {}}
        ]
        self.reservierungen = []

    def reservieren(self, datum, zeit, anzahl_personen, name, email):
        for tisch in self.tische:
            if zeit not in tisch["reserviert"]:
                tisch["reserviert"][zeit] = []
            
            # Überprüfen, ob noch Platz für die Personenanzahl ist
            reservierte_plätze = sum([r[1] for r in tisch["reserviert"][zeit] if r[0] == datum])
            if reservierte_plätze + anzahl_personen <= tisch["plätze"]:
                tisch["reserviert"][zeit].append((datum, anzahl_personen, name, email))
                self.reservierungen.append({"datum": datum, "zeit": zeit, "anzahl_personen": anzahl_personen, "name": name, "email": email})
                return True
        return False

    def stornieren(self, reservierung):
        for tisch in self.tische:
            if reservierung["zeit"] in tisch["reserviert"]:
                tisch["reserviert"][reservierung["zeit"]].remove((reservierung["datum"], reservierung["anzahl_personen"], reservierung["name"], reservierung["email"]))
                self.reservierungen.remove(reservierung)

    def get_reservierungen(self):
        return self.reservierungen

class GUI:
    def __init__(self, root):
        self.restaurant = Restaurant()
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        # Auswahl der Jahr und Monat
        self.year_var = tk.StringVar(value="2024")
        self.month_var = tk.StringVar(value="10")
        self.day_var = tk.StringVar(value="1")

        # Jahr und Monat Auswahl
        self.year_menu = ttk.Combobox(self.frame, textvariable=self.year_var)
        self.year_menu["values"] = [str(year) for year in range(2024, 2026)]
        self.year_menu.bind("<<ComboboxSelected>>", self.update_days)
        self.year_menu.pack(side="left")

        self.month_menu = ttk.Combobox(self.frame, textvariable=self.month_var)
        self.month_menu["values"] = [str(month).zfill(2) for month in range(1, 13)]
        self.month_menu.bind("<<ComboboxSelected>>", self.update_days)
        self.month_menu.pack(side="left")

        # Tagesauswahl
        self.day_menu = ttk.Combobox(self.frame, textvariable=self.day_var)
        self.update_days()  # Initiale Tagesauswahl basierend auf dem aktuellen Monat und Jahr
        self.day_menu.pack(side="left")

        # Auswahl der Uhrzeit
        self.zeit_var = tk.StringVar()
        self.zeit_menu = ttk.Combobox(self.frame, textvariable=self.zeit_var)
        self.zeit_menu["values"] = ["17:00", "19:00", "21:00"]
        self.zeit_menu.pack()

        # Anzahl der Personen
        self.anzahl_personen_var = tk.IntVar()
        self.anzahl_personen_entry = ttk.Entry(self.frame, textvariable=self.anzahl_personen_var)
        self.anzahl_personen_entry.pack()

        # Name und Email
        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.pack()
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.pack()

        self.email_label = tk.Label(self.frame, text="Email:")
        self.email_label.pack()
        self.email_entry = ttk.Entry(self.frame)
        self.email_entry.pack()

        # Senden Button
        self.send_button = ttk.Button(self.frame, text="Reservieren", command=self.reservieren)
        self.send_button.pack()

        # Tabelle der Reservierungen
        self.tabelle_frame = tk.Frame(self.frame)
        self.tabelle_frame.pack(side="bottom", fill="both", expand=True)

        self.tabelle_text = tk.Text(self.tabelle_frame, state="disabled")
        self.tabelle_text.pack(fill="both", expand=True)

        # Aktualisieren der Tabelle bei Start
        self.update_reservierungsliste()

    def update_days(self, *args):
        """Aktualisiert die Tage basierend auf dem ausgewählten Jahr und Monat."""
        year = int(self.year_var.get())
        month = int(self.month_var.get())
        days_in_month = monthrange(year, month)[1]
        self.day_menu["values"] = [str(day).zfill(2) for day in range(1, days_in_month + 1)]
        if int(self.day_var.get()) > days_in_month:
            self.day_var.set(str(days_in_month))  # Setze den Tag auf den maximalen Tag des Monats

    def reservieren(self):
        datum = f"{self.year_var.get()}-{self.month_var.get()}-{self.day_var.get()}"
        zeit = self.zeit_var.get()
        anzahl_personen = self.anzahl_personen_var.get()
        name = self.name_entry.get()
        email = self.email_entry.get()

        # Validierung der Eingaben
        if not name or not email or not zeit or anzahl_personen <= 0:
            messagebox.showerror("Fehler", "Bitte alle Felder korrekt ausfüllen.")
            return

        # Reservierung durchführen
        if self.restaurant.reservieren(datum, zeit, anzahl_personen, name, email):
            messagebox.showinfo("Erfolg", "Reservierung erfolgreich.")
            self.clear_fields()
            self.update_reservierungsliste()
        else:
            messagebox.showerror("Fehler", "Kein Platz mehr verfügbar.")

    def clear_fields(self):
        self.anzahl_personen_var.set(0)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.zeit_var.set("")

    def update_reservierungsliste(self):
        self.tabelle_text.config(state="normal")
        self.tabelle_text.delete(1.0, tk.END)
        for reservierung in self.restaurant.get_reservierungen():
            self.tabelle_text.insert(tk.END, f"{reservierung['datum']} {reservierung['zeit']} - {reservierung['name']} ({reservierung['anzahl_personen']} Personen)\n")
        self.tabelle_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Restaurant Reservierung")
    gui = GUI(root)
    root.mainloop()