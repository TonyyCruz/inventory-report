from inventory_report.inventory.product import Product

mock_item = {
    "id": 1,
    "nome_do_produto": "Cafe",
    "nome_da_empresa": "Cafe Pele",
    "data_de_fabricacao": "1940-10-23",
    "data_de_validade": "2022-12-29",
    "numero_de_serie": "PLE2022",
    "instrucoes_de_armazenamento": "Na memoria"
  }

mock_expect = (
    f"O produto {mock_item['nome_do_produto']}"
    f" fabricado em {mock_item['data_de_fabricacao']}"
    f" por {mock_item['nome_da_empresa']} com validade"
    f" até {mock_item['data_de_validade']}"
    f" precisa ser armazenado {mock_item['instrucoes_de_armazenamento']}."
)


def test_relatorio_produto():
    product = Product(
        mock_item["id"],
        mock_item["nome_do_produto"],
        mock_item["nome_da_empresa"],
        mock_item["data_de_fabricacao"],
        mock_item["data_de_validade"],
        mock_item["numero_de_serie"],
        mock_item["instrucoes_de_armazenamento"]
        )

    assert repr(product) == mock_expect
