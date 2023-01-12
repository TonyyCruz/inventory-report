import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main(path, report):
    print("------------ARGUMENTOS----", path, report)
    if path.endswith(".csv"):
        importer = CsvImporter
    elif path.endswith(".xml"):
        importer = XmlImporter
    elif path.endswith(".json"):
        importer = JsonImporter
    else:
        print('A extensão do arquivo deve ser ".csv", ".json" ou ".xml"')
        raise ValueError("Arquivo inválido")

    inventory_report = InventoryRefactor(importer)
    return inventory_report.import_data(path, report)


if len(sys.argv) < 2:
    sys.stderr.write("Verifique os argumentos")
else:
    file_path = sys.argv[0]
    report_type = sys.argv[1]
    main(file_path, report_type)
