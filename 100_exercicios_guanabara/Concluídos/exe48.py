"""
Faça um programa que calcula a soma entre
todos os números impares que são múltiplos
de três e que se encontram no intervalo de
1 até 500
"""
total = 0
termos = 0
for c in range(1, 501, 2):
    if c % 2 == 1 and c % 3 == 0:
        total += c
        termos += 1
print(f'A soma dos {termos} números impares e multiplos de 3 de 1 a 500 é {total}')
