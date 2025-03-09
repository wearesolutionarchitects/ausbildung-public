import tkinter as tk
from tkinter import ttk, messagebox

class DataConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Size Converter")

        # Create input field for data size in bytes
        self.size_label = tk.Label(self.root, text="Enter data size (bytes):")
        self.size_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.size_entry = tk.Entry(self.root, width=30)
        self.size_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create combobox to select units
        self.unit_label = tk.Label(self.root, text="Select unit:")
        self.unit_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.units = ["Bytes", "KiB", "MiB", "GiB", "TB"]
        self.unit_var = tk.StringVar()
        self.unit_var.set(self.units[0])
        self.unit_combobox = ttk.Combobox(self.root, textvariable=self.unit_var)
        self.unit_combobox['values'] = self.units
        self.unit_combobox.grid(row=1, column=1, padx=10, pady=10)

        # Create buttons to convert and reset
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_size)
        self.convert_button.grid(row=2, column=1, padx=10, pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_form)
        self.reset_button.grid(row=3, column=1, padx=10, pady=10)

        # Create labels to display the results
        self.result_label_gib = tk.Label(self.root, text="")
        self.result_label_gib.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label_gb = tk.Label(self.root, text="")
        self.result_label_gb.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def convert_size(self):
        try:
            size_in_bytes = int(self.size_entry.get())
            
            if size_in_bytes < 0:
                messagebox.showerror("Error", "Data size cannot be negative.")
                return

            unit = self.unit_var.get()
            conversion_factors = {
                "Bytes": 1,
                "KiB": 1024,
                "MiB": 1024 ** 2,
                "GiB": 1024 ** 3,
                "TB": 1024 ** 4
            }
            factor = conversion_factors[unit]
            
            size_in_unit = size_in_bytes / factor
            
            if unit == "Bytes":
                self.result_label_gib.config(text="")
                self.result_label_gb.config(text="")
                self.result_label_gib.config(text=f"GiB: {size_in_unit:.2f}")
                self.result_label_gb.config(text="")
            elif unit in ["KiB", "MiB"]:
                if size_in_bytes < 1024 ** 3:
                    self.result_label_gib.config(text="")
                    self.result_label_gb.config(text="")
                    self.result_label_gb.config(text=f"GB: {size_in_unit:.2f}")
                    self.result_label_gib.config(text="")
                else:
                    self.result_label_gb.config(text="")
                    self.result_label_gib.config(text="")
                    gib = size_in_bytes / (1024 ** 3)
                    self.result_label_gib.config(text=f"GiB: {gib:.2f}")
            elif unit == "TB":
                if size_in_bytes < 1024 ** 3:
                    self.result_label_gb.config(text="")
                    self.result_label_gib.config(text="")
                    self.result_label_gb.config(text=f"GB: {size_in_unit * 1024:.2f}")
                    self.result_label_gib.config(text="")
                else:
                    gib = size_in_bytes / (1024 ** 3)
                    self.result_label_gb.config(text="")
                    self.result_label_gib.config(text="")
                    self.result_label_gib.config(text=f"GiB: {gib:.2f}")
                    
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid data size in bytes.")

    def reset_form(self):
        self.size_entry.delete(0, tk.END)
        self.unit_var.set(self.units[0])
        self.result_label_gib.config(text="")
        self.result_label_gb.config(text="")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    converter = DataConverter()
    converter.run()
