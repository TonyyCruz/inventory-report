import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    if sys.argv[1].endswith(".csv"):
        importer = CsvImporter
    elif sys.argv[1].endswith(".xml"):
        importer = XmlImporter
    elif sys.argv[1].endswith(".json"):
        importer = JsonImporter
    else:
        print('A extensão do arquivo deve ser ".csv", ".json" ou ".xml"')
        raise ValueError("Arquivo inválido")

    inventory_report = InventoryRefactor(importer)
    print(inventory_report.import_data(sys.argv[1], sys.argv[2]), end="")
