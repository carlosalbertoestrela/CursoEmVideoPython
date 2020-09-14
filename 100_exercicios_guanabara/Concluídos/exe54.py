"""
Crie um programa que leia o ano de nascimento
de sete pessoas, no final, mostre quantas
pessoas não atingiram a maior idade e quantas
já são maiores.
"""
from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input(f'Digite o {c+1}º ano de nascimento:  '))
    if date.today().year - ano < 18:
        menor += 1
    else:
        maior += 1
print(f'{maior} dos digitados são maiores de idade e {menor} são menores de idade')
