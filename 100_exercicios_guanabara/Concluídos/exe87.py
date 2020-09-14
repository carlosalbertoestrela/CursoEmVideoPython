"""
Exercício Python 087:
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
soma = s_terceira = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        matriz[x][y] = int(input(f'Digite o valor para a posição [{x}x{y}]: '))
        if matriz[x][y] % 2 == 0:
            soma += matriz[x][y]
print('-='*20)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^10}]', end='')
    print()
for x in range(len(matriz)):

    s_terceira += matriz[x][2]
print('-='*20)
print(f"""A soma dos valores pares da matiz é: {soma}
A soma da terceira colula é: {s_terceira}
O maior valor na 2ª linha foi: {max(matriz[1])}""")
print('-='*20)
