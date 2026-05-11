import customtkinter as tk
from functools import partial

from core.settings import *
from core.tabs.customTabBase import CustomTabBase

class NewModTab(CustomTabBase):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.data = {}

        self.nameVar = tk.StringVar(self)
        self.idVar = tk.StringVar(self)
        self.authorVar = tk.StringVar(self)

        # label
        #self.addLabel("infoLabel", "New mod parameters", 0, 0)
        self.mainLabel = tk.CTkLabel(self, text="New mod parameters")
        self.mainLabel.grid(row=0, column=0, padx=10, pady=10)

        # mod meta settings
        self.metaFrame = tk.CTkFrame(self)
        self.metaFrame.grid(row=1, column=0, padx=10, pady=10)


        self.nameEntryLabel = tk.CTkLabel(self.metaFrame, text="Name:")
        self.nameEntryLabel.grid(row=0, column=0, padx=10, pady=10)

        self.nameEntry = tk.CTkEntry(self.metaFrame, placeholder_text="Mod name", textvariable=self.nameVar)
        self.nameEntry.insert(0, "Default")
        self.nameEntry.grid(row=0, column=1, padx=10, pady=10)


        self.idEntryLabel = tk.CTkLabel(self.metaFrame, text="modId:")
        self.idEntryLabel.grid(row=1, column=0, padx=10, pady=10)

        self.idEntry = tk.CTkEntry(self.metaFrame, placeholder_text="Unique mod identifier", textvariable=self.idVar)
        self.idEntry.insert(0, "default")
        self.idEntry.grid(row=1, column=1, padx=10, pady=10)


        self.authorEntryLabel = tk.CTkLabel(self.metaFrame, text="Author:")
        self.authorEntryLabel.grid(row=2, column=0, padx=10, pady=10)

        self.authorEntry = tk.CTkEntry(self.metaFrame, placeholder_text="Author", textvariable=self.authorVar)
        self.authorEntry.insert(0, "Aráček")
        self.authorEntry.grid(row=2, column=1, padx=10, pady=10)


        self.saveMetaButton = tk.CTkButton(self.metaFrame, text="Save mod info", command=self.saveMeta)
        self.saveMetaButton.grid(row=99, column=1, padx=10, pady=10)


        # mod export
        self.exportButton = tk.CTkButton(self, text="Export mod", command=self.exportMod)
        self.exportButton.grid(row=99, column=0, padx=10, pady=10)


    def saveMeta(self):
        self.data['mod_id'] = self.idVar.get()

        print(f"{__name__}: saving mod info")
        self.master.master.saveModInfoJson(self.data['mod_id'], self.data)


    def exportMod(self):
        print(f"{__name__}: exporting mod as '{self.data.get('mod_id')}'")
        self.master.master.saveNcaOutput(self.data.get('mod_id'))