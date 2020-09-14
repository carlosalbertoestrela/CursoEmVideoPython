"""
Crie um programa que simule o funcionamento de um caixa eletrônico, no inicío pergunta ao
usuário o valor a ser sacado(números inteiros) e o programa irá informar  quantas cédulas de
cada valor serão enregues. considerando que o caixa terá cédualas de 50$, 20$, 10$ e 1$.
"""
from time import sleep

print('*=*'*20)
print(f'{"Caixa Eletronico":=^60}')
print('*=*'*20)
valorSaque = int(input('Quanto deseja sacar? '))
total = valorSaque
nota = 100
cont = 0
print('Contando notas...')
sleep(1.2)
print(f'Transação encerrada! Você recebera {valorSaque} em:')
while True:
    if total > nota:
        while total >= nota:
            total -= nota
            cont = cont + 1
    elif nota == 100:
        nota = 50
        cont = 0
    elif nota == 50:
        nota = 20
        cont = 0
    elif nota == 20:
        nota = 10
        cont = 0
    elif nota == 10:
        nota = 1
        cont = 0
    else:
        break
    if cont != 0:
        print(f'{cont} notas de {nota}')
print('==*'*20)
