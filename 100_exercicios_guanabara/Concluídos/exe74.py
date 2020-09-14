'''
Crie um programa que vai gerar 5 números aleatórios e colocar
em uma tupla.
Depois disso, mostre a listagem de númeors gerados e também indique
o menor valor e o mair valor que estão na tupla.
'''
from random import randint
a = randint(-999, 999)
b = randint(-999, 999)
c = randint(-999, 999)
d = randint(-999, 999)
e = randint(-999, 999)
maior = menor = a
aleatorio = (a, b, c, d, e)
primeiroCiclo = True
for n in aleatorio:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'Geramos esta lista aleatória: {aleatorio}\n'
      f'seu maior número é {maior} e seu menor é {menor}')

# Solução do Guanabara:
lista = (randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999), randint(-999, 999))
print('Os valores sorteados foram: ', end='')
for n in lista:
    print(f'{n} ', end='')
print(f'\nO mairo número da lista foi: {max(lista)}')
print(f'O menor número da lista foi: {min(lista)}')

