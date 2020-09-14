"""
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 peimeiros termos da
progressão usando a estrutura while.
"""
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = 10
a = p
print(f'Os 10 primeiros termos de um PA iniciada em {p} com razão {r} são:')
print(f'{p} >', end='')
while t > 1:
    a += r
    t -= 1
    print(f' {a} > ', end='')
print('FIM')



