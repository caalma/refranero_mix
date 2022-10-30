#!/usr/bin/python3


"""
EJECUTAR CON:
./selector.py crudos/*
"""


from sys import argv

def db_ignorar():
    la = [
        "./bd/con_una_coma.txt",
        "./bd/con_un_punto_y_coma.txt",
    ]
    r = []
    for a in la:
        with open(a, 'r') as f:
            r += f.read().split('\n')
    return r


def selector_de_una_coma():
    sel = []
    for ar in argv[1:]:
        with open(ar, 'r') as f:
            ll = f.read().strip().split('\n')
            for l in ll:
                if not ';' in l:
                    tc = len(l.split(','))
                    if tc == 2:
                        sel.append(l)

    sel = sorted(list(set(sel)))
    with open('./bd/con_una_coma.txt', 'w') as f:
        f.write('\n'.join(sel))

def selector_de_un_punto_y_coma():
    sel = []
    for ar in argv[1:]:
        with open(ar, 'r') as f:
            ll = f.read().strip().split('\n')
            for l in ll:
                tc = len(l.split(';'))
                if tc == 2:
                    sel.append(l)

    sel = sorted(list(set(sel)))
    with open('./bd/con_un_punto_y_coma.txt', 'w') as f:
        f.write('\n'.join(sel))


def selector_con_otro_formato():
    ign = db_ignorar()
    sel = []
    for ar in argv[1:]:
        with open(ar, 'r') as f:
            ll = f.read().strip().split('\n')
            for l in ll:
                if not l in ign:
                    sel.append(l)

    sel = sorted(list(set(sel)))
    with open('./bd/con_separacion_manual__sin_procesar.txt', 'w') as f:
        f.write('\n'.join(sel))

selector_de_una_coma()
selector_de_un_punto_y_coma()
selector_con_otro_formato()
