c: int
preço: float
quantidade: int
valor: float
valorR: float
valorA: float
dinheiroT: float
troco: float

c = int(input('Código do produto comprado: '))
if c == 1:
    preço = 5
if c == 2:
    preço = 3.5
if c == 3:
    preço = 4.8
if c == 4:
    preço = 8.9
if c == 5:
    preço = 7.32

quantidade = int(input('Quantidade Comprada: '))
valor = preço * quantidade
print(f'VALOR TOTAL: R${valor:.2f}')
dinheiro = float(input('DINHEIRO RECEBIDO: R$'))

if dinheiro < valor:
    valorR = valor - dinheiro
    print(f'DINHEIRO INSUFICIENTE, ADICIONE R${valorR:.2f}')
    valorA = float(input('VALOR ADICIONADO: R$'))
    dinheiro = valorA + dinheiro
    if dinheiro < valor:
        print('DINHEIRO INSUFICIENTE')
        exit()

troco = dinheiro - valor
print(f'TROCO = R${troco:.2f} OBRIGADO PELA COMPRA, VOLTE SEMPRE!')
