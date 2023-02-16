x: int; y: int; z: int
x = int(input('Primeiro valor: '))
y = int(input('Segundo valor: '))
z = int(input('Terceiro valor: '))
if x < y and x < z:
    print(f'MENOR: {x}')
    exit()
if y < x and y < z:
    print(f'MENOR: {y}')
    exit()
if z < x and z < y:
    print(f'MENOR: {z}')
    exit()