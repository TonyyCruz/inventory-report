from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import DictReader
import xmltodict
import json


class Inventory:
    @classmethod
    def read_file(cls, path):
        file_data = ""
        with open(path, 'r') as file:
            if path.endswith(".csv"):
                file_data = list(DictReader(file))
            elif path.endswith(".xml"):
                dict_file = xmltodict.parse(file.read())
                file_data = dict_file["dataset"]["record"]
            elif path.endswith(".json"):
                file_data = json.load(file)
        return file_data

    @classmethod
    def import_data(cls, path, report_type):
        list_of_products_in_dict = cls.read_file(path)

        if report_type.lower() == "simples":
            return SimpleReport.generate(list_of_products_in_dict)
        elif report_type.lower() == "completo":
            return CompleteReport.generate(list_of_products_in_dict)
        else:
            return "Invalid Report Type"
