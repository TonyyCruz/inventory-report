from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path, 'r') as file:
            dict_file = xmltodict.parse(file.read())
            return dict_file["dataset"]["record"]
