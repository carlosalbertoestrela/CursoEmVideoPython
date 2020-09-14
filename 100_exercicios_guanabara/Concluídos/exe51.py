"""
Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. no final, mostre
os 10 primeiros termos dessa progressão.
"""
from time import sleep

print(f'{"Calculando uma progreção aritimética":=^52}')
p_termo = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))
lista = [p_termo]
num = p_termo
print('\033[1;35m PROCESSANDO...''\033[m')
sleep(2)
for c in range(1, 10):
    num = num + r
    lista.append(num)
print(f'Os 10 primeiros termos da progressão com ínico em {p_termo} e razão {r} são:\n {lista}')
input('Pressione *ENTER* para sair')

# Soliução do Guanabara
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo+1, razao):
    print(c, end=' > ')
print('fim')



