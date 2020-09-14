"""
Exercício Python 091:
 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from time import sleep
from random import randint
from operator import itemgetter
ranking = dict()
jogadores = dict()
cont = 1
while cont <= 4:
    jogadores[f'Jogador {cont}'] = randint(1, 6)
    cont += 1
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(.5)
print("-="*30)
print(f"{'Ranking':=^30}")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i+1}º {v[0]} que tirou {v[1]}')
    cont += 1
    sleep(.5)

