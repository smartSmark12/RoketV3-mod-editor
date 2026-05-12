import customtkinter as tk
from functools import partial

from core.settings import *
from core.tabs.customTabBase import CustomTabBase

class NewModTab(CustomTabBase):
    def __init__(self, master, meta=None, **kwargs):
        super().__init__(master, meta, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        print(meta)

        if meta != None:
            self.data = meta
        else:
            self.data = {}

        """ self.nameVar = tk.StringVar(self)
        self.idVar = tk.StringVar(self)
        self.authorVar = tk.StringVar(self) """

        # label
        self.mainLabel = tk.CTkLabel(self, text="New mod parameters")
        self.mainLabel.grid(row=0, column=0, padx=10, pady=10)

        # mod meta settings
        self.metaFrame = tk.CTkFrame(self)
        self.metaFrame.grid(row=1, column=0, padx=10, pady=10)


        self.metaLabel = tk.CTkLabel(self.metaFrame, text="Mod metadata:")
        self.metaLabel.grid(row=0, column=0, padx=10, pady=5)


        self.nameEntryLabel = tk.CTkLabel(self.metaFrame, text="Name:")
        self.nameEntryLabel.grid(row=10, column=0, padx=10, pady=5)

        """ if self.data['mod_name']:
            self.nameEntry.insert """

        self.nameEntry = tk.CTkEntry(self.metaFrame, placeholder_text="Mod name")
        self.nameEntry.insert(0, self.data['mod_name'] if self.data else DEFAULT_SETTINGS['name'])
        self.nameEntry.grid(row=10, column=1, padx=10, pady=5)


        self.idEntryLabel = tk.CTkLabel(self.metaFrame, text="modId:")
        self.idEntryLabel.grid(row=11, column=0, padx=10, pady=5)

        self.idEntry = tk.CTkEntry(self.metaFrame, placeholder_text="Unique mod identifier")
        self.idEntry.insert(0, self.data['mod_id'] if self.data else DEFAULT_SETTINGS['id'])
        self.idEntry.grid(row=11, column=1, padx=10, pady=5)


        self.versionEntryLabel = tk.CTkLabel(self.metaFrame, text="version:")
        self.versionEntryLabel.grid(row=12, column=0, padx=10, pady=5)

        self.versionEntry = tk.CTkEntry(self.metaFrame, placeholder_text="Git-like mod version (e.g. 1.4.7)")
        self.versionEntry.insert(0, self.data['mod_version'] if self.data else DEFAULT_SETTINGS['version'])
        self.versionEntry.grid(row=12, column=1, padx=10, pady=5)


        self.authorEntryLabel = tk.CTkLabel(self.metaFrame, text="Author:")
        self.authorEntryLabel.grid(row=15, column=0, padx=10, pady=5)

        self.authorEntry = tk.CTkEntry(self.metaFrame, placeholder_text="Author")
        if self.data:
            self.authorEntry.insert(0, self.data['mod_author'])

        self.authorEntry.grid(row=15, column=1, padx=10, pady=5)


        self.saveMetaButton = tk.CTkButton(self.metaFrame, text="Save mod info", command=self.saveMeta)
        self.saveMetaButton.grid(row=99, column=1, padx=10, pady=10)


        # mod export
        self.exportButton = tk.CTkButton(self, text="Export mod", command=self.exportMod)
        self.exportButton.grid(row=98, column=0, padx=10, pady=10)


        self.closeButton = tk.CTkButton(self, text="Close", command=self.close)
        self.closeButton.grid(row=99, column=0, padx=10, pady=10)


    def saveMeta(self):
        self.data['mod_id'] = self.idEntry.get()
        self.data['mod_name'] = self.nameEntry.get()
        self.data['mod_author'] = self.authorEntry.get()
        self.data['version'] = GAME_TARGET_VERSION
        self.data['mod_version'] = self.versionEntry.get()

        print(f"{__name__}: saving mod info")
        self.master.master.saveModInfoJson(self.data['mod_id'], self.data)


    def exportMod(self):
        print(f"{__name__}: exporting mod as '{self.data.get('mod_id')}'")
        self.master.master.saveNcaOutput(self.data.get('mod_id'))


    def close(self):
        self.master.delete(WINDOW_NAMES['newMod'])
        self = None