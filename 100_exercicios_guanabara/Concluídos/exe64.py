"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
"""
cont = 0
soma = 0
while True:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        break
print(f'A soma do {cont} números digitados é {soma}!!')
