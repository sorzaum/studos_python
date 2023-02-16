n1: float; n2: float; nf: float

n1 = float(input("NOTA DO PRIMEIRO SEMESTRE: "))
n2 = float(input("NOTA DO SEGUNDO SEMESTRE: "))
nf = n1+n2
print(f'NOTA FINAL = {nf:.2f}')
if nf < 60.00:
    print('REPROVADO')
    exit()
