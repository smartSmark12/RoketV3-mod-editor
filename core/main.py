import customtkinter as tk
from functools import partial

from core.settings import *

class ModEditor(tk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # window settings
        self.title(f"RoketV3 mod editor v{EDITOR_VERSION}")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")

        # grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # initial values
        self.newModText = "New mod"
        self.addItemText = "Add item"

        # menu bar
        self.mainTabMenu = tk.CTkTabview(self)
        self.mainTabMenu.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # menu new mod
        self.mainNewMod = self.mainTabMenu.add(self.newModText)

        newModButton = tk.CTkButton(self.mainNewMod, text="Create new mod", command=self.callbackCreateNewMod)
        newModButton.grid(row=0, column=0, padx=10, pady=10)
        newModButton = tk.CTkButton(self.mainNewMod, text="Open mod", command=self.callbackOpenMod)
        newModButton.grid(row=1, column=0, padx=10, pady=10)

        # menu postsetup
        self.mainTabMenu.set(self.newModText)

    def callbackCreateNewMod(self):
        self.tabAddItem()
        print("created new mod")

    def callbackOpenMod(self):
        print("opened mod file picked")

    def tabAddItem(self):

        # menu new item
        try:
            self.mainAddItem = self.mainTabMenu.add(self.addItemText)
        except: print("tab already added")

def run():
    print("starting mod editor")
    app = ModEditor()
    app.mainloop()