from classes.geladeira import Geladeira

# cria uma nova instancia de Geladeira
eletrolux = Geladeira()

# verifica e imprime se porta está aberta
if (eletrolux.get_porta_aberta() == False):
    print('Porta fechada')
else:
    print('Porta aberta')

# verifica e imprime se lampada está desligada
if (eletrolux.get_lampada_acesa()):
    print('Lampada acesa')
else:
    print('Lampada desligada')

# chama o método abrir porta
eletrolux.abrir_porta()
print('Tentando abrir a porta de novo')
eletrolux.abrir_porta()

# verifica e imprime se porta está aberta
if (eletrolux.get_porta_aberta()):
    print('Porta aberta')
else:
    print('Porta fechada')

# verifica e imprime se lampada está desligada
if (eletrolux.get_lampada_acesa()):
    print('Lampada acesa')
else:
    print('Lampada desligada')

#chamar o método fechar porta
print('Chamando o método fechar porta')
eletrolux.fechar_porta()

# verifica e imprime se porta está aberta
if (eletrolux.get_porta_aberta()):
    print('Porta aberta')
else:
    print('Porta fechada')

# verifica e imprime se lampada está desligada
if (eletrolux.get_lampada_acesa()):
    print('Lampada acesa')
else:
    print('Lampada desligada')

print('Tentando fechar porta de novo')
eletrolux.fechar_porta()