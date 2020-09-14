"""
Faça um programa que leia um número inteiro e diga se ele é
ou não um número primo.
"""
print(f'{"Avaliador de números primos":=^40}')
num = int(input('Digire um número: '))
primo = True
if num > 1:
    for c in range(2, (num - 1)):
        if num % c == 0:
            primo = False
else:
    primo = False
print(f'Numéro é primo? {primo}')

# Solução do Guanabara:
numero = int(input('Digite um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {numero} foi divisível {tot} vezes!')
if tot == 2:
    print('E por isso ele é PRIMOO')
else:
    print('E por isso ele NÃO É PRIMO')
