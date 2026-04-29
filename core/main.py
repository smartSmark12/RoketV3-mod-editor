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

        self.tabs = {}
        self.buttons = {}
        self.labels = {}

        # menu bar
        self.mainTabMenu = tk.CTkTabview(self)
        self.mainTabMenu.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # menu new mod
        self.addTab(self.newModText)
        """ self.tabs["newMod"] = self.mainTabMenu.add(self.newModText) """

        self.addButton(self.newModText, "newMod", "Create new mod", self.callbackCreateNewMod, 0, 0)
        self.addButton(self.newModText, "openMod", "Open mod", self.callbackOpenMod, 1, 0)
        """ newModButton = tk.CTkButton(self.tabs, text="Create new mod", command=self.callbackCreateNewMod)
        newModButton.grid(row=0, column=0, padx=10, pady=10)
        newModButton = tk.CTkButton(self.mainNewMod, text="Open mod", command=self.callbackOpenMod)
        newModButton.grid(row=1, column=0, padx=10, pady=10) """

        # menu postsetup
        self.mainTabMenu.set(self.newModText)

    def callbackCreateNewMod(self):
        self.addTab("New mod params")
        self.selectTab("New mod params") # this is borderline stupid
        self.getTab("New mod params").grid_columnconfigure(0, weight=1)
        self.getTab("New mod params").grid_rowconfigure(0, weight=1)
        self.addLabel("New mod params", "infoLabel", "New mod parameters", 0, 0)
        print("created new mod")

    def callbackOpenMod(self):
        print("opened mod file picked")

    def addTab(self, tabName:str):
        try:
            self.tabs[tabName] = self.mainTabMenu.add(tabName)
        except: print("tab already added")

    def addButton(self, targetTab:str, buttonName:str, text:str, callbackFunction, gridRow:int=0, gridCol:int=0):
        self.buttons[buttonName] = tk.CTkButton(
            master=self.tabs[targetTab],
            text=text,
            command=callbackFunction
        )
        self.buttons[buttonName].grid(row=gridRow, column=gridCol, padx=10, pady=10)

    def addLabel(self, targetTab:str, labelName:str, text:str, gridRow:int=0, gridCol:int=0):
        self.labels[labelName] = tk.CTkLabel(
            master=self.tabs[targetTab],
            text=text
        )
        self.labels[labelName].grid(row=gridRow, column=gridCol, padx=10, pady=10)

    def selectTab(self, tabName:str):
        self.mainTabMenu.set(tabName)

    def getTab(self, tabName:str):
        return self.tabs[tabName]

def run():
    print("starting mod editor")
    app = ModEditor()
    app.mainloop()