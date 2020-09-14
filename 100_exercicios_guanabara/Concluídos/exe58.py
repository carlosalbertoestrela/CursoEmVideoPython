"""
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número de 0 a 10. só que agora o jogador
vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
from time import sleep

cont = 1
comp = randint(0, 10)
print(f"{'Jogo da advinhação!!':=^50}")
print('Vou pensar em um número de 0 a 10! Tente advinhar')
sleep(.4)
print('\033[34mPensando.... \033[m')
sleep(1.2)
print('Pronto! pensei, agora tente advinhar!!!')
n = int(input('Que numero você acha que pensei? '))
while n != comp:
    if n < comp:
        print('Um pouquinho mais!')
    else:
        print('Um pouquinho menos!')
    n = int(input('tenta de novo!! '))
    cont += 1

print(f'Isso ai!! foi em {n} que eu pensei!!')
if cont == 1:
    print('E ainda foi de primeira!! Você lê mentes?')
else:
    print(f'Aêê!! acertou!! mas teve de tentar {cont} vezes pra isso, haha!!')
