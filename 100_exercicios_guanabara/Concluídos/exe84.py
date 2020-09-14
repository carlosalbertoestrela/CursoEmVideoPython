"""
Exercício Python 084:
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
grupo = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    sair = str(input('Continuar cadastro?: [S/N]')).strip().upper()[0]
    if sair == 'N':
        break

print('-='*30)
print(f'Foram cadastradas {len(grupo)} pessoas!')
print(f'O maior peso foi {maior:.2f}Kg, que foi o peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]}...', end='')
    print()
print(f'O menor peso foi {menor:.2f}Kg, que doi o peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]}...', end='')





