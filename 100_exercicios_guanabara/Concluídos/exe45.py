"""
Crie um program que faça o computador jogar Jokenpô com você.
"""
from random import randint

print(f'{"Que comecem os jogos!!!":=^50}')
print('Vamos jogar PEDRA, PAPEL E TESOURA! escolha o seu!!!\n'
      '[ 1 ] Pedra\n'
      '[ 2 ] Papel\n'
      '[ 3 ] Tesoura\n')
escolhapc = randint(1, 3)
escolha = int(input('O que vai escolher? '))
if escolha == 1 and escolhapc == 2:
    print('Você escolheu Pedra e o PC Papel. Você perdeu!!')
elif escolha == 1 and escolhapc == 3:
    print('Você escolheu Pedra e o PC Tesoura. Você ganhou!!')

elif escolha == 2 and escolhapc == 1:
    print('Você escolheu Papel e o PC Pedra. Você ganhou!!')
elif escolha == 2 and escolhapc == 3:
    print('Você escolheu Papel e o PC Tesoura. Você perdeu!!')

elif escolha == 3 and escolhapc == 1:
    print('Você escolheu Tesoura e o PC Pedra. Você perdeu!!')
elif escolha == 3 and escolhapc == 2:
    print('Você escolheu Tesoura e o PC Papel. Você ganhou!!')
else:
    print('Você e o PC escolheram o mesmo!!! deu empate!')



