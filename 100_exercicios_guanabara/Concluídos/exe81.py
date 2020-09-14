"""
Exercício Python 081:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        continuar = str(input('Deseja continuar? [S/N]').strip().upper()[0])
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
lista.sort(reverse=True)
print('-='*30)
print(f'Foram digitados {len(lista)} números!')
print(f'A lista de números em ordem decrescente é {lista}')
if 5 in lista:
    print(f'o valor 5 está na posição {lista.index(5)} da lista!')
else:
    print('O valor 5 não está na lista!')
