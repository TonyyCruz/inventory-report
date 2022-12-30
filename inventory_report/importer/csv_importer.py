from .importer import Importer
from csv import DictReader


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        try:
            with open(path, 'r') as file:
                return list(DictReader(file))

        except FileExistsError:
            print(f'"{path}" não existe')
            raise FileExistsError(f'"{path}" não existe')

        except FileNotFoundError:
            print(f'"{path}" não foi encontrado')
            raise FileNotFoundError(f'"{path}" não foi encontrado')
