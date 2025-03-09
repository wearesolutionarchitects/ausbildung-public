import tkinter as tk
from calendar import monthcalendar

class Calculator:
    def __init__(self, root, **kwargs):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(side="top")

        self.year_var = tk.StringVar()
        self.month_var = tk.StringVar()

        self.year_menu = ttk.Combobox(self.frame, textvariable=self.year_var)
        for year in range(int(kwargs["fromyear"]), int(kwargs["toyear"]) + 1):
            self.year_menu["values"] += [str(year)]
        self.year_menu.set(str(kwargs["year"]))
        self.year_menu.pack(side="left")

        self.month_menu = ttk.Combobox(self.frame, textvariable=self.month_var)
        for month in range(1, 13):
            self.month_menu["values"] += [str(month)]
        self.month_menu.set(str(kwargs["month"]))
        self.month_menu.pack(side="right")

        self.cal_button = ttk.Button(self.frame, text="OK", command=lambda: root.after(100, update_cal))
        self.cal_button.pack(side="bottom")
