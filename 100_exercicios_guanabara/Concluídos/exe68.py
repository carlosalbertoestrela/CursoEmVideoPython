"""
Faça um programa que jogur par ou impar com o computador. O jogo será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

"""
from random import randint
vit = play = pc = esc = soma = 0
print('='*20, '\nJOGO DO PAR OU IMPAR\n', '='*20)
while True:
    play = int(input('Escolha seu número! '))
    pc = randint(1, 100)
    while True:
        esc = int(input('''Agora escolha!
        Par  [1]
        Impar[2]
    Sua escolha: '''))
        if esc in (1, 2):
            break
    soma = play + pc

    if soma % 2 == 0:
        print(f'{soma} é PAR!!')
    else:
        print(f'{soma} é IMPAR!!')
    if (soma % 2) != (esc % 2):
        print('Você venceu!!')
        vit += 1
        print('~~'*10)
    else:
        print('A não! você perdeu!!! ')
        print(f'vitórias consecutivas: {vit}')
        break
