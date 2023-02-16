c: float; f: float
O: str
O = str(input('Qual escala será digitada (C/F)?'))
if O == 'C':
    c = float(input('Digite a temperatura em Celsius: '))
    f = ((9*c)/5)+32
    print(f'Temperatura em Fahrenheit = {f:.2f}')
    exit()
if O == "F":
    f = float(input('Digite a temperatura em Fahrenheit: '))
    c = (5*(f-32))/9
    print(f'Temperatura em Celsius = {c:.2f}')
    exit()