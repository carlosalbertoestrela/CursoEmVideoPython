"""
Exercício Python 088:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from time import sleep
from random import randint
jogo = []
print("=*"*20)
print(f"{'GERADOR MEGA SENA':^40}")
print("=*"*20)
for i in range(0, int(input('Quantos jogos deseja gerar? '))):
    while len(jogo) < 6:
        aleatorio = randint(1, 60)
        if aleatorio not in jogo:
            jogo.append(aleatorio)
    print(f'Jogo {i+1}: {sorted(jogo)}')
    jogo.clear()
    sleep(.3)
print("=*"*20)
print('Programa finalizado! \nBoa Sorte!!')
