import os
import customtkinter as tk
import zipfile
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

        self.newModTabText = "Mod params"

        self.tabs = {}
        self.buttons = {}
        self.labels = {}

        # menu bar
        self.mainTabMenu = tk.CTkTabview(self)
        self.mainTabMenu.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # menu new mod
        self.addTab(self.newModText)
        self.getTab(self.newModText).grid_columnconfigure(0, weight=1)

        self.addButton(self.newModText, "newMod", "Create new mod", self.callbackCreateNewMod, 0, 0)
        self.addButton(self.newModText, "openMod", "Open mod", self.callbackOpenMod, 1, 0)

        # menu postsetup
        self.mainTabMenu.set(self.newModText)

    def callbackCreateNewMod(self):
        self.addTab(self.newModTabText)
        self.selectTab(self.newModTabText) # this is borderline stupid
        self.getTab(self.newModTabText).grid_columnconfigure(0, weight=1)
        self.addLabel(self.newModTabText, "infoLabel", "New mod parameters", 0, 0)

        self.addButton(self.newModTabText, "saveMod", "Export mod", partial(self.saveNcaOutput, "new_mod", None))
        print("created new mod")

    def callbackOpenMod(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Nebula compressed archive", ".nca")], title="Select mod .nca file", initialdir=os.getcwd() + "/" + OUTPUT_FOLDER_PATH)
        print("picked mod file:", filename)
        self.openNcaProject(filename)

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
    
    def saveNcaOutput(self, fileName:str, files:list[str]):
        with zipfile.ZipFile(OUTPUT_FOLDER_PATH + fileName + ARCHIVE_EXTENSION, "w", zipfile.ZIP_DEFLATED) as zip:
            zip.write(TEMP_FOLDER_PATH + "test.txt")

    def openNcaProject(self, fileName:str):
        with zipfile.ZipFile(fileName, "r", zipfile.ZIP_DEFLATED) as zip:
            zip.extractall(TEMP_FOLDER_PATH)

            for file in zip.namelist():
                print(file)

def run():
    print("starting mod editor")
    app = ModEditor()
    app.mainloop()