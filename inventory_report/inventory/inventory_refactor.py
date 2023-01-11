from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from .inventory_iterator import InventoryIterator


class InventoryRefactor():
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def add_item_from_file(self, path):
        file_data = self.importer.import_data(path)

        for item in file_data:
            self.data.append(item)

    def import_data(self, path, report_type):
        self.add_item_from_file(path)

        if report_type.lower() == "simples":
            return SimpleReport.generate(self.data)
        elif report_type.lower() == "completo":
            return CompleteReport.generate(self.data)
        else:
            print(f'{report_type} deve ser "simples" ou "completo"')
            raise ValueError("Invalid Report Type")
