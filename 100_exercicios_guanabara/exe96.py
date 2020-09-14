"""
Exercício Python 096:
 Faça um programa que tenha uma função chamada área(),
 que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def area(a1, b2):
    ar = float(a1) * float(b2)
    print(f'A área do terreno de {a:.1f}x{b:.1f} é de {ar:.1f}m²!')


def titulo(tt):
    print('-'*30)
    print(f'{tt:^30}'.upper())
    print('-'*30)


titulo('controle de terrenos')
a = float(input('ALTURA: m²'))
b = float(input('LARGURA: m²'))
area(a, b)
