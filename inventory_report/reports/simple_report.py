from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products_data):
        date_today = str(date.today())

        manufacturing_dates = sorted([
                                product["data_de_fabricacao"]
                                for product in products_data
                              ])

        validity_dates = sorted([
                        product["data_de_validade"]
                        for product in products_data
                        if product["data_de_validade"] >= date_today
                      ])

        companies = [
                        product["nome_da_empresa"]
                        for product in products_data
                      ]

        most_common_company = Counter(companies).most_common(1)

        return (
            f"Data de fabricação mais antiga: {manufacturing_dates[0]}\n"
            f"Data de validade mais próxima: {validity_dates[0]}\n"
            f"Empresa com mais produtos: {most_common_company[0][0]}"
            )
