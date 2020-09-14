"""
Refaça o desafio 009, mostrando a tabuada
de um número que o usuário escolher, só que
agora utilizando um laço FOR
"""
num = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuada de {num} é: ')
for c in range(1, 11):
    print(f'{num} x {c:2} = {num*c}')
