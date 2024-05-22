import math


deca_x, deca_y = map(float, input().split())
pola_r, pola_f = map(float, input().split())
pola_x = pola_r * math.cos(pola_f)
pola_y = pola_r * math.sin(pola_f)
print(math.dist((deca_x, deca_y), (pola_x, pola_y)))
