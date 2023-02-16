x: float; y: float
x = float(input('Digite dois numeros inteiros:'))
y = float(input())
if x/y == x//y or y/x == y//x:
    print('SÃO MÚLTIPLOS')
    exit()
if x/y != x//y and y/x != y//x:
    print('NÃO SÃO MÚLTIPLOS')