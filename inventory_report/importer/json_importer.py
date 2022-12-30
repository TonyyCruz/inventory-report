from .importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        try:
            with open(path, 'r') as file:
                return json.load(file)

        except FileExistsError:
            print(f'"{path}" não existe')
            raise FileExistsError(f'"{path}" não existe')

        except FileNotFoundError:
            print(f'"{path}" não foi encontrado')
            raise FileNotFoundError(f'"{path}" não foi encontrado')
