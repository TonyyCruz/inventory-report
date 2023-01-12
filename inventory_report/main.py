import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    file_path = sys.argv[1]
    report_type = sys.argv[2]

    if file_path.endswith(".csv"):
        importer = CsvImporter
    elif file_path.endswith(".xml"):
        importer = XmlImporter
    elif file_path.endswith(".json"):
        importer = JsonImporter
    else:
        print('A extensão do arquivo deve ser ".csv", ".json" ou ".xml"')
        raise ValueError("Arquivo inválido")

    inventory_report = InventoryRefactor(importer)
    print(inventory_report.import_data(file_path, report_type), end="")
