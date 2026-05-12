import customtkinter as tk

from functools import partial

from core.frames.itemFrame import ItemFrame

class FeaturesFrame(tk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=1)

        self.items = {}

        self.mainLabel = tk.CTkLabel(self, text="Features:")
        self.mainLabel.grid(row=0, column=0, padx=10, pady=10)

        for i in range(5):
            item = ItemFrame(self, "core/assets/Roket icon.png", f"Special {i}", i, "idkType")
            #button = tk.CTkButton(self, text=f"feature {i}", command=partial(print, "??"))
            item.grid(row=i+1, column=0, padx=5, pady=5, sticky="nsew")
            self.items[i] = item