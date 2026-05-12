import customtkinter as tk

from core.settings import *

class FeatureAddFrame(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.mainLabel = tk.CTkLabel(self, text="Add feature")
        self.mainLabel.grid(row=0, column=0, padx=10, pady=10)

        self.featureSelect = tk.CTkOptionMenu(self, values=[f"{POSSIBLE_FEATURE_TYPES[i]} [{i}]" for i in POSSIBLE_FEATURE_TYPES])
        self.featureSelect.set(f"{POSSIBLE_FEATURE_TYPES['module_types']} [module_types]")
        self.featureSelect.grid(row=1, column=0, padx=10, pady=10)

        self.featureAdd = tk.CTkButton(self, text="Create", command=None)
        self.featureAdd.grid(row=1, column=1, padx=10, pady=10)