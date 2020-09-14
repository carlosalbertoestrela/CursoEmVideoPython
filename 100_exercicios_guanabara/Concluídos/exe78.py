"""
Exercício Python 078:
 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valor = list()
for i in range(0, 5):
    valor.append(input(f'Digite um valor para a posição {i}: '))
print(f'O maior valor digitado foi {max(valor)} e ele foi digitado nas posições ', end='')
for i, n in enumerate(valor):
    if n == max(valor):
        print(f'{i}... ', end='')
print('')
print(f'O menor valor digitado foi {min(valor)} e ele foi digitado nas posições ', end='')
for i, n in enumerate(valor):
    if n == min(valor):
        print(f'{i}... ', end='')
