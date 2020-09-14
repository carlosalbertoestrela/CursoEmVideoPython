"""
Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    t = input('Deseja continuar? [S/N]: ').strip().upper()
    if t == 'N':
        break
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print('-='*30)
print(f'A lista completa digitada foi {lista}')
print(f'Com os pares sendo: {par}\nCom os impares sendo: {impar}')