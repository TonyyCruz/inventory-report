from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def stock_by_companies(products_data):

        companies_and_stock = CompleteReport.count_and_order_dict_by_key(
            products_data,
            "nome_da_empresa"
        )

        stocked_products_by_company = ""

        for company, stock in companies_and_stock:
            stocked_products_by_company += f"- {company}: {stock}\n"

        return stocked_products_by_company

    def generate(products_data):
        simple_report = CompleteReport.generate_simple_report(products_data)
        companies_and_stock = CompleteReport.stock_by_companies(products_data)
        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{companies_and_stock}"
        )
