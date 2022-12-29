from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def extract_dict_values_by_key(
        cls,
        dict_data,
        request_key,
        min_value=False,
        max_value=False
    ):
        if min_value and max_value:
            return [
                product[request_key]
                for product in dict_data
                if product[request_key] >= min_value
                and product[request_key] <= max_value
                ]

        elif min_value:
            return [
                product[request_key]
                for product in dict_data
                if product[request_key] >= min_value
                ]

        elif max_value:
            return [
                product[request_key]
                for product in dict_data
                if product[request_key] <= max_value
                ]

        else:
            return [
                      product[request_key]
                      for product in dict_data
                      ]

    @classmethod
    def count_and_order_dict_by_common(cls, dict_data, dict_key):
        dict_isolated_key = cls.extract_dict_values_by_key(
          dict_data,
          dict_key
        )
        return Counter(dict_isolated_key).most_common()

    @classmethod
    def generate_simple_report(cls, products_data):
        date_today = str(date.today())

        manufacturing_dates = cls.extract_dict_values_by_key(
          products_data,
          "data_de_fabricacao"
        )

        validity_dates = cls.extract_dict_values_by_key(
          products_data,
          "data_de_validade",
          date_today
        )

        most_common_company = cls.count_and_order_dict_by_common(
          products_data,
          "nome_da_empresa"
        )

        manufacturing_dates.sort()
        validity_dates.sort()

        return (
            f"Data de fabricação mais antiga: {manufacturing_dates[0]}\n"
            f"Data de validade mais próxima: {validity_dates[0]}\n"
            f"Empresa com mais produtos: {most_common_company[0][0]}"
            )

    @classmethod
    def generate(cls, products_data):
        return cls.generate_simple_report(products_data)
