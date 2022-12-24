from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def extract_orderly_dict_key(
        dict_data,
        request_key,
        min_value=False,
        max_value=False
    ):
        if min_value and max_value:
            return sorted([
                product[request_key]
                for product in dict_data
                if product[request_key] >= min_value
                and product[request_key] <= max_value
                ])

        elif min_value:
            return sorted([
                product[request_key]
                for product in dict_data
                if product[request_key] >= min_value
                ])

        elif max_value:
            return sorted([
                product[request_key]
                for product in dict_data
                if product[request_key] <= max_value
                ])

        else:
            return sorted([
                      product[request_key]
                      for product in dict_data
                      ])

    @staticmethod
    def count_and_order_dict_by_key(dict_data, dict_key):
        dict_isolated_key = SimpleReport.extract_orderly_dict_key(
          dict_data,
          dict_key
        )
        return Counter(dict_isolated_key).most_common()

    @staticmethod
    def generate(products_data):
        date_today = str(date.today())

        manufacturing_dates = SimpleReport.extract_orderly_dict_key(
          products_data,
          "data_de_fabricacao"
        )

        validity_dates = SimpleReport.extract_orderly_dict_key(
          products_data,
          "data_de_validade",
          date_today
        )

        most_common_company = SimpleReport.count_and_order_dict_by_key(
          products_data,
          "nome_da_empresa"
        )

        return (
            f"Data de fabricação mais antiga: {manufacturing_dates[0]}\n"
            f"Data de validade mais próxima: {validity_dates[0]}\n"
            f"Empresa com mais produtos: {most_common_company[0][0]}"
            )
