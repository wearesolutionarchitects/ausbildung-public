import tkinter as tk
from tkinter import messagebox

class DataConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Size Converter")

        # Create input field for data size in bytes
        self.size_label = tk.Label(self.root, text="Enter data size (bytes):")
        self.size_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.size_entry = tk.Entry(self.root, width=30)
        self.size_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create buttons to convert and reset
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_size)
        self.convert_button.grid(row=1, column=1, padx=10, pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_form)
        self.reset_button.grid(row=2, column=1, padx=10, pady=10)

        # Create labels to display the results
        self.result_label_gib = tk.Label(self.root, text="")
        self.result_label_gib.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label_gb = tk.Label(self.root, text="")
        self.result_label_gb.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def convert_size(self):
        try:
            size_in_bytes = int(self.size_entry.get())
            
            if size_in_bytes < 0:
                messagebox.showerror("Error", "Data size cannot be negative.")
                return

            gib = size_in_bytes / (1024 ** 3)
            gb = size_in_bytes / (1024 ** 3 * 8)

            self.result_label_gib.config(text=f"GiB: {gib:.2f}")
            self.result_label_gb.config(text=f"GB: {gb:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid data size in bytes.")

    def reset_form(self):
        self.size_entry.delete(0, tk.END)
        self.result_label_gib.config(text="")
        self.result_label_gb.config(text="")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    converter = DataConverter()
    converter.run()
