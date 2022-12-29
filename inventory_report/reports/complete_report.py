from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def stock_by_companies(cls, products_data):

        companies_and_stock = cls.count_and_order_dict_by_common(
            products_data,
            "nome_da_empresa"
        )
        stocked_products_by_company = ""

        for company, stock in companies_and_stock:
            stocked_products_by_company += f"- {company}: {stock}\n"
        return stocked_products_by_company

    @classmethod
    def generate(cls, products_data):
        simple_report = cls.generate_simple_report(products_data)
        companies_and_stock = cls.stock_by_companies(products_data)

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{companies_and_stock}"
        )
