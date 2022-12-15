from inventory_report.inventory.product import Product


mock = {
  "id": 10,
  "nome_do_produto": "Nome test",
  "nome_da_empresa": "Empresa teste",
  "data_de_fabricacao": "2022-12-15",
  "data_de_validade": "2025-12-15",
  "numero_de_serie": "999999999999",
  "instrucoes_de_armazenamento": "Local seco"
}


def test_cria_produto():
    product = Product(
      mock["id"],
      mock["nome_do_produto"],
      mock["nome_da_empresa"],
      mock["data_de_fabricacao"],
      mock["data_de_validade"],
      mock["numero_de_serie"],
      mock["instrucoes_de_armazenamento"]
    )

    assert mock["nome_do_produto"] in product.__repr__()
    assert mock["data_de_fabricacao"] in product.__repr__()
    assert mock["nome_da_empresa"] in product.__repr__()
    assert mock["data_de_validade"] in product.__repr__()
    assert mock["instrucoes_de_armazenamento"] in product.__repr__()
