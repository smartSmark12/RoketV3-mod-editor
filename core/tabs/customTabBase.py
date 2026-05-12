import customtkinter as tk

class CustomTabBase(tk.CTkFrame):

    def __init__(self, master, meta=None, **kwargs):
        super().__init__(master, **kwargs)

        self.buttons = {}
        self.labels = {}

    def addButton(self, buttonName:str, text:str, callbackFunction, gridRow:int=0, gridCol:int=0):
        self.buttons[buttonName] = tk.CTkButton(
            master=self,
            text=text,
            command=callbackFunction
        )
        self.buttons[buttonName].grid(row=gridRow, column=gridCol, padx=10, pady=10)

    def addLabel(self, labelName:str, text:str, gridRow:int=0, gridCol:int=0):
        self.labels[labelName] = tk.CTkLabel(
            master=self,
            text=text
        )
        self.labels[labelName].grid(row=gridRow, column=gridCol, padx=10, pady=10)