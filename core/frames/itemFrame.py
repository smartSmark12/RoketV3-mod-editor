import customtkinter as tk

from PIL import Image

class ItemFrame(tk.CTkFrame):
    def __init__(self, master, iconPath:str, name:str, id:str, itype:str):
        super().__init__(master)

        self.icon = tk.CTkLabel(self, image=tk.CTkImage(Image.open(iconPath), size=(50,50)), text="")
        self.name = tk.CTkLabel(self, text=name)
        self.id = tk.CTkLabel(self, text=id, text_color="#777777")
        self.type = tk.CTkLabel(self, text=itype)
        self.edit = tk.CTkButton(self, text="Edit", command=None)
        self.delete = tk.CTkButton(self, text="X", fg_color="#C00000", hover_color="#690000", command=None)

        self.icon.grid(row=0, column=0, padx=2, pady=2)
        self.name.grid(row=0, column=1, padx=2, pady=2)
        self.id.grid(row=0, column=2, padx=2, pady=2)
        self.type.grid(row=0, column=3, padx=2, pady=2)
        self.edit.grid(row=0, column=4, padx=2, pady=2)
        self.delete.grid(row=0, column=5, padx=2, pady=2)

