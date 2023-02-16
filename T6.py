x: float; y: float
x = float(input('Digite os minutos usados: '))
y = 50+((x-100)*2)
if x > 100:
    print(f'Valor a pagar: R${y:.2f}')
    exit()
print('Valor a pagar: R$50.00')