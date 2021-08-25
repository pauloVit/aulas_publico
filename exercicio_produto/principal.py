from classes.produto import Produto

objeto_produto = Produto("Tomate", 30, 3)
print('Descricao = ' + objeto_produto.descricao)
print('Quantidade = ' + str(objeto_produto.quantidade))
print('Valor unitário = ' + str(objeto_produto.valor_unitario))
print('Subtotal = ' + str(objeto_produto.get_subtotal()))

objeto_produto2 = Produto(
    valor_unitario = 10)
print('Descricao = ' + objeto_produto2.descricao)
print('Quantidade = ' + str(objeto_produto2.quantidade))
print('Valor unitário = ' + str(objeto_produto2.valor_unitario))
print('Subtotal = ' + str(objeto_produto2.get_subtotal()))