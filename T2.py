s: float; h: float; sh: float; m: float; sm: float
s = float(input('HORÁRIO EM SEGUNDOS: '))
h = int(s/3600)
if h < 0:
    h = 0
sh = s-(3600*h)
m = int(sh/60)
if m < 0:
    m = 0
sm = sh-(60*m)
print(f'HORÁRIO MODELO(H:M:S): {h}:{m}:{sm:.0f}')
