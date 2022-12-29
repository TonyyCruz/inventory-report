from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import DictReader
import xmltodict
import json


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        list_of_dict = ""

        with open(path, 'r') as file:
            if path.endswith(".csv"):
                list_of_dict = list(DictReader(file))
            elif path.endswith(".xml"):
                dict_file = xmltodict.parse(file.read())
                list_of_dict = dict_file["dataset"]["record"]
            elif path.endswith(".json"):
                list_of_dict = json.load(file)

        if report_type.lower() == "simples":
            return SimpleReport.generate(list_of_dict)
        elif report_type.lower() == "completo":
            return CompleteReport.generate(list_of_dict)
        else:
            return "Invalid Report Type"
