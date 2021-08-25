class Geladeira:

    def __init__(self):
        self.__porta_aberta = False
        self.__lampada_acesa = False

    def get_porta_aberta(self):
        return self.__porta_aberta

    def get_lampada_acesa(self):
        return self.__lampada_acesa

    def abrir_porta(self):
        if (self.__porta_aberta == True):
            print('Não pode abrir a porta, ela já está aberta, meu jovem')
            return

        self.__porta_aberta = True
        self.__lampada_acesa = True

    def fechar_porta(self):
        if (self.__porta_aberta == False):
            print('Já tá fechada, não tem como fechar mais')
            return

        self.__porta_aberta = False
        self.__lampada_acesa = False