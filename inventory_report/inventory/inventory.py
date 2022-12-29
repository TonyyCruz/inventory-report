from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from ..importer.csv_importer import CsvImporter
from ..importer.xml_importer import XmlImporter
from ..importer.json_importer import JsonImporter


class Inventory:
    @classmethod
    def read_file(cls, path):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)

    @classmethod
    def import_data(cls, path, report_type):
        list_of_products_in_dict = cls.read_file(path)

        if report_type.lower() == "simples":
            return SimpleReport.generate(list_of_products_in_dict)
        elif report_type.lower() == "completo":
            return CompleteReport.generate(list_of_products_in_dict)
        else:
            return "Invalid Report Type"
