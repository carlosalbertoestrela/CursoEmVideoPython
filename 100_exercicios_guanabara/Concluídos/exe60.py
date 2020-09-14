"""
Faça um programa que leia um númeor qualquer e mostreo o seu fatorial.

ex:
5! = 5x4x3x2x1 = 120
"""
num = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {num}! = ', end='')
c = num
f = 1
while c > 0:
    print(f'{c} ', end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)

n = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {n}! = ', end='')
fat = 1
for co in range(n, 1, -1):
    print(f'{co} ', end='')
    print('x ' if co > 2 else 'x 1 = ', end='')
    fat *= co
print(fat)
