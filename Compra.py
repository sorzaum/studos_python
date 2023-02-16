preço: float
quantidade: int
dinheiro: float
valor: float
valorR: float
valorA: float
dinheiroT: float
troco: float

preço = float(input('DIGITE O VALOR DO PRODUTO: R$'))
quantidade = int(input('DIGITE A QUANTIDADE COMPRADA: '))
valor = preço * quantidade
print(f'VALOR TOTAL: R${valor:.2f}')
dinheiro = float(input('DINHEIRO RECEBIDO: R$'))

if dinheiro < valor:
    valorR = valor - dinheiro
    print(f'DINHEIRO INSUFICIENTE, ADICIONE R${valorR:.2f}')
    valorA = float(input('VALOR ADICIONADO: R$'))
    dinheiro = valorA + dinheiro
    if dinheiro < valor:
        print('DINHEIRO INSUFICIENTE, POBRE')
        exit()

troco = dinheiro - valor
print(f'TROCO = R${troco:.2f} OBRIGADO PELA COMPRA!')
