#!/usr/bin/python3

from random import randint

def partir(tex, modo):
    r = ['', '']
    s = ''
    agregar = True
    if modo == "una_coma":
        s = ','
    elif modo == "un_puntoycoma":
        s = ';'
    elif modo == "separacion_manual":
        s = '|'
        agregar = False

    r = tex.split(s)
    if agregar:
        r[0] += s
    return r

la = [
    ['una_coma', './bd/con_una_coma.txt'],
    ['un_puntoycoma', './bd/con_un_punto_y_coma.txt'],
    ['separacion_manual', './bd/con_separacion_manual.txt'],
]

mi = randint(0,len(la)-1)
bd = open(la[mi][1], 'r').read().split('\n')

ri1 = ri2 = randint(0, len(bd)-1)

while ri2 == ri1:
    ri2 = randint(0, len(bd)-1)

r1 = bd[ri1]
r2 = bd[ri2]

modo = la[mi][0]

rp1 = partir(r1, modo)[0]
rp2 = partir(r2, modo)[1]

if modo == 'separacion_manual':
    r1 = r1.replace('|', '')
    r2 = r2.replace('|', '')

print(f'\n==  {rp1}{rp2} ==\n')
print(f':1  {r1}')
print(f':2  {r2}')
