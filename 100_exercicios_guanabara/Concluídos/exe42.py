"""
Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
 - Equilátero: Todos os lados iguais
 - Isósceles: dois lados iguis
 - Escaleno: todos os lados diferentes
"""
n1 = float(input('Digite o primeiro seguimento: '))
n2 = float(input('Digite o segundo seguimento: '))
n3 = float(input('Digite o terceiro seguimento: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2:
    if n1 == n2 == n3:
        print('Os seguimento acima podem formar um triângulo Equilátero!')
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('Os seguimentos acima podem formar um triângulo Isósceles')
    else:
        print('Os seguimentos acima podem formar um triâgulo Escaleno')
else:
    print('Os seguimentos acima não podem formar um triângulo')
