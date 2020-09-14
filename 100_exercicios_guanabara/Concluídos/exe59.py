"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo valor: '))
sair = False
while not sair:
    print('-=-'*8)
    escolha = int(input("""   [1] Somar 
   [2] multiplicar
   [3] maior
   [4] novos números
   [5] sair
>>>> Qual é sua escolha? """))
    if escolha == 1:
        print(f'A soma de {num1} e {num2} é {num1 + num2}!')
    elif escolha == 2:
        print(f'A multiplicação entre {num1} e {num2} é {num1 * num2}')
    elif escolha == 3:
        maior = 0
        if num1 > num2:
            maior = num1
        elif num2 > num1:
            maior = num2
        else:
            maior = '... nehum dos dois, eles são iguais!'
        print(f'O mairo número é {maior}!')
    elif escolha == 4:
        print('Digite os novos números: ')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número '))
    elif escolha == 5:
        sair = True
        print('Até mais!!')
    else:
        print('Escolha inválida, tente novamente!')
    sleep(2)

