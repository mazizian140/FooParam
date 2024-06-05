# foo_param/gui.py

import tkinter as tk
from tkinter import messagebox
#from foo_param.coreFunc import calculate_volume
from foo_param.coreFunc import calculate_volume

class FooParamApp(tk.Tk):
    def __int__(self):
        super().__init__()
        self,title("Foo Param - Sphere Volume Calculator")

        self.label = tk.Label(self, text="Enter the radius of the sphere:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.calculate_button = tk.Button(self, text="Calculate Volume", command=self.calculate_volume)
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

    def calculate_volume(self):
        try:
            radius = float(self.entry.get())
            volume = calculate_volume(radius)
            self.result_label.config(text=f"Volume: {volume:.5f}")
        except ValueError as error:
            messagebox.showerror("Error", str(error))


if __name__ == '__main__':
    app = FooParamApp()
    app.mainloop()