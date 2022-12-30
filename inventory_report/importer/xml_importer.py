from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        try:
            with open(path, 'r') as file:
                dict_file = xmltodict.parse(file.read())
                return dict_file["dataset"]["record"]

        except FileExistsError:
            print(f'"{path}" não existe')
            raise FileExistsError(f'"{path}" não existe')

        except FileNotFoundError:
            print(f'"{path}" não foi encontrado')
            raise FileNotFoundError(f'"{path}" não foi encontrado')
