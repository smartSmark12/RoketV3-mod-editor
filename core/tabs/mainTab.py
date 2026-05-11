import customtkinter as tk

from core.tabs.customTabBase import CustomTabBase
from core.settings import *

class MainTab(CustomTabBase):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.buttons = {}

        self.grid_columnconfigure(0, weight=1)

        self.addLabel("welcome", "Welcome to the mod editor!", 0, 0)
        self.addLabel("welcomeInfo", "Select one of the options below\nto start editing", 1, 0)

        self.addButton("newMod", "Create new mod", master.master.callbackCreateNewMod, 2, 0)
        self.addButton("openMod", "Open mod", master.master.callbackOpenMod, 3, 0)