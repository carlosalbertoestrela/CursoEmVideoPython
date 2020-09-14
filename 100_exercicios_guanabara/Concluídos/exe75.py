'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
 mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
valores = [int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: '))]
print(f'Você digitou os númeos {valores}')
if 9 in valores:
    print(f'O número 9 apareceu {valores.count(9)}')
else:
    print('O número 9 não foi digitado!')
if 3 in valores:
    tres = valores.index(3) + 1
    print(f'O número 3 foi digitado na {tres}ª posição')
else:
    print('O três não foi digitado!')
print('Os números pares digitados foram: ', end='')
for i in valores:
    if i % 2 == 0:
        print(f'{i}; ', end='')

# Solução do Guanabara:


