import os, shutil
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

        #self.iconbitmap("./core/assets/icon.png")

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
        try:
            filename = tk.filedialog.askopenfilename(filetypes=[("Nebula compressed archive", ".nca"), ("compressed archive", ".zip")], title="Select mod .nca file", initialdir=os.getcwd() + "/" + OUTPUT_FOLDER_PATH)
            print("picked mod file:", filename)
            self.openNcaProject(filename)
        except:
            print("cancelled picking mod file")

    def addTab(self, tabName:str, frameClass, meta=None):
        #try:
        self.tabs[tabName] = self.mainTabMenu.add_tab(tabName, frameClass(self.mainTabMenu, meta))
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
            sourcePath = TEMP_FOLDER_PATH + modId + "/"
            archivePath = modId + "/"
            zip.write(sourcePath + MOD_INFO_NAMES["modInfo"] + JSON_EXTENSION, archivePath + MOD_INFO_NAMES["modInfo"] + JSON_EXTENSION)


    def openNcaProject(self, fileName:str):
        # clear temp folder
        for filename in os.listdir(TEMP_FOLDER_PATH):
            file_path = os.path.join(TEMP_FOLDER_PATH, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

        # extract the nca
        with zipfile.ZipFile(fileName, "r", zipfile.ZIP_DEFLATED) as zip:
            zip.extractall(TEMP_FOLDER_PATH)

            for file in zip.namelist():
                print(file)

        # load the mod into the editor
        self.loadTempProject()


    def loadTempProject(self):
        tree = [os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(TEMP_FOLDER_PATH) for f in filenames]

        print(tree)

        files = [f.split("\\")[-1].split(".")[-2] for f in tree]

        if MOD_INFO_NAMES['modInfo'] in files[0]:
            modInfoFile = [f for f in tree if MOD_INFO_NAMES['modInfo'] in f][0]
            self.addTab(WINDOW_NAMES['newMod'], NewModTab, meta=JsonLoader.load_from_file(modInfoFile))
            self.selectTab(WINDOW_NAMES['newMod']) # this is borderline stupid


def run():
    print("starting mod editor")
    app = ModEditor()
    app.mainloop()