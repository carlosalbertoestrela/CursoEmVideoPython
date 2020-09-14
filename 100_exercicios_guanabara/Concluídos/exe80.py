"""
Exercício Python 080:
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
numeros = []
for i in range(0, 5):
    n = int(input("Digite um número: "))
    if i == 0 or n > numeros[-1]:   # testa se é o primeiro valor ou se é maior que o último valor
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):   # testa se é menor que o valor varrendo a lista
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1
print(numeros)

