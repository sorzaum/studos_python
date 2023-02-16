g: int
c: str
g = int(input('Digite a medida da Glicose: '))
if g <= 100:
    c = 'Normal'
if g > 100 and g <= 140:
    c = 'Elevado'
if g > 140:
    c = 'Diabético'
print(f'Classificação: {c}')