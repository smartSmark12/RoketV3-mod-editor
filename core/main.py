import os
import customtkinter as tk
import zipfile
from functools import partial

from core.settings import *
from core.json.json_loader import JsonLoader
from core.tabview.mainTabView import MainTabview
from core.tabs.mainTab import MainTab
from core.tabs.newModTab import NewModTab

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
        self.tabs = {}
        self.buttons = {}
        self.labels = {}

        # menu bar
        self.mainTabMenu = MainTabview(master=self)
        self.mainTabMenu.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # menu new mod
        self.addTab(WINDOW_NAMES['main'], MainTab)

        # menu postsetup
        self.selectTab(WINDOW_NAMES['main'])

    def callbackCreateNewMod(self):
        self.addTab(WINDOW_NAMES['newMod'], NewModTab)
        self.selectTab(WINDOW_NAMES['newMod']) # this is borderline stupid

        print("created new mod")

    def callbackOpenMod(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Nebula compressed archive", ".nca")], title="Select mod .nca file", initialdir=os.getcwd() + "/" + OUTPUT_FOLDER_PATH)
        print("picked mod file:", filename)
        self.openNcaProject(filename)

    def addTab(self, tabName:str, frameClass):
        #try:
        self.tabs[tabName] = self.mainTabMenu.add_tab(tabName, frameClass(self.mainTabMenu))
        #except: print("tab already added")

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
    

    ## SAVING

    def saveModInfoJson(self, modId:str, data:dict):
        JsonLoader.write_to_file(TEMP_FOLDER_PATH + data['mod_id'] + "/" + MOD_INFO_NAMES['modInfo'] + JSON_EXTENSION, data)
    

    def saveNcaOutput(self, modId:str):
        with zipfile.ZipFile(OUTPUT_FOLDER_PATH + modId + ARCHIVE_EXTENSION, "w", zipfile.ZIP_DEFLATED) as zip:
            folderPath = TEMP_FOLDER_PATH + modId + "/"
            zip.write(folderPath + MOD_INFO_NAMES["modInfo"] + JSON_EXTENSION)


    def openNcaProject(self, fileName:str):
        with zipfile.ZipFile(fileName, "r", zipfile.ZIP_DEFLATED) as zip:
            zip.extractall(TEMP_FOLDER_PATH)

            for file in zip.namelist():
                print(file)


def run():
    print("starting mod editor")
    app = ModEditor()
    app.mainloop()