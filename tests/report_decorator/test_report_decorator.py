from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

mock_items = [
    {
      "id": 1,
      "nome_do_produto": "Cafe",
      "nome_da_empresa": "Cafe Pele",
      "data_de_fabricacao": "1940-10-23",
      "data_de_validade": "2022-12-29",
      "numero_de_serie": "PLE2022",
      "instrucoes_de_armazenamento": "Na memoria"
    },
    {
      "id": 2,
      "nome_do_produto": "cha",
      "nome_da_empresa": "cha zan",
      "data_de_fabricacao": "2022-10-01",
      "data_de_validade": "2024-10-29",
      "numero_de_serie": "chazan",
      "instrucoes_de_armazenamento": "Armazenar em temperatura ambiente"
    }
]
mock_expect_simple_report = (
    f"\033[32m{'Data de fabricação mais antiga:'}\033[0m"
    + f" \033[36m{'1940-10-23'}\033[0m\n"

    f"\033[32m{'Data de validade mais próxima:'}\033[0m"
    + f" \033[36m{'2024-10-29'}\033[0m\n"

    f"\033[32m{'Empresa com mais produtos:'}\033[0m"
    + f" \033[31m{'Cafe Pele'}\033[0m"
)

mock_expect_complete_report = (
    f"\033[32m{'Data de fabricação mais antiga:'}\033[0m"
    + f" \033[36m{'1940-10-23'}\033[0m\n"

    f"\033[32m{'Data de validade mais próxima:'}\033[0m"
    + f" \033[36m{'2024-10-29'}\033[0m\n"

    f"\033[32m{'Empresa com mais produtos:'}\033[0m"
    + f" \033[31m{'Cafe Pele'}\033[0m\n"

    "Produtos estocados por empresa:\n"
    "- Cafe Pele: 1\n"
    "- cha zan: 1\n"
)


def test_decorar_relatorio():
    simple_colored_stance = ColoredReport(SimpleReport)
    complete_colored_stance = ColoredReport(CompleteReport)
    colored_simple_relator = simple_colored_stance.generate(mock_items)
    colored_complete_relator = complete_colored_stance.generate(mock_items)

    assert colored_simple_relator == mock_expect_simple_report
    assert colored_complete_relator == mock_expect_complete_report
