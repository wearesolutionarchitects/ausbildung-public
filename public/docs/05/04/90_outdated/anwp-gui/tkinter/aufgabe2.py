import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def convert_bytes():
    try:
        # Input in bytes
        byte_value = float(entry.get())
        selected_unit = unit_combobox.get()

        # Conversion to bytes based on the selected unit
        if selected_unit == "GB":
            byte_value *= 10 ** 9  # 1 GB = 10^9 Bytes
        elif selected_unit == "GiB":
            byte_value *= 2 ** 30   # 1 GiB = 2^30 Bytes
        # Further units can be added here

        # Calculation of the values
        gb_value = byte_value / (10 ** 9)  # 1 GB = 10^9 Bytes
        gib_value = byte_value / (2 ** 30)  # 1 GiB = 2^30 Bytes

        # Output of the results
        result_var.set(f"{gb_value:.6f} GB\n{gib_value:.6f} GiB")

    except ValueError:
        messagebox.showerror("Fehler bei der Eingabe", "Bitte eine gültige Zahl eingeben!")

# Main window
root = tk.Tk()
root.title("Datenmengenkonverter")

# Input field
label = tk.Label(root, text="Geben Sie eine Datenmenge ein:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)
# Combobox for the unit
unit_label = tk.Label(root, text="Wählen Sie die Einheit:")
unit_label.pack(pady=5)

unit_combobox = ttk.Combobox(root, values=["GB", "GiB"])
unit_combobox.set("GB")  # Set default value
unit_combobox.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Konvertieren", command=convert_bytes)
convert_button.pack(pady=10)

# Result field
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)

# Main loop
root.mainloop()