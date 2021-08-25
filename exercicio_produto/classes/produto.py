class Produto:

    def __init__(self, descricao = '', quantidade = 0, valor_unitario = 0):
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.__subtotal = 0

    def get_subtotal(self):
        self.__subtotal = (self.quantidade * self.valor_unitario)
        return self.__subtotal