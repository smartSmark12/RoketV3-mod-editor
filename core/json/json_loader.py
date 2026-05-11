# yoinked from Nebula v0.0.4s

import json
from pathlib import Path

class JsonLoader:
    @staticmethod
    def create_new_file(filepath:str) -> None:
        try:
            Path(filepath.rsplit('/', 1)[0]).mkdir(parents=True, exist_ok=True)

            with open(filepath, "x") as file:
                return True
        except FileExistsError:
            return False

    @staticmethod
    def load_from_file(filepath:str) -> dict:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            print(f"{__name__}:readError: couldn't read data from file {filepath}")
            return None
        
    @staticmethod
    def write_to_file(filepath:str, data:dict) -> None:
        """ try: """
        if JsonLoader.create_new_file(filepath):
            print(f"{__name__}: created new file at {filepath}")
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=4))
        """ except:
            print(f"{__name__}:writeError: couldn't write data:\n{data}\nto file:\n{filepath}") """