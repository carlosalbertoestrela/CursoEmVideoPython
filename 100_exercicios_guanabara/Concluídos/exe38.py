"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
 - O primeiro valeor é maior
 - O segundo valor é maior
 - Não existe valor maior, os dios são iguais
"""
from time import sleep

num1 = int(input('Digite dois números para serem comparados:\nDigite o PRIMEIRO número: '))
num2 = int(input('Digite o SEGUNDO número: '))
print('<<<Comparando>>>')
sleep(.8)
if num1 > num2:
    print(f'{num1} é maior que {num2}!')
elif num1 < num2:
    print(f'{num1} é menor que {num2}')
else:
    print(f'{num1} é igual a {num2}')
