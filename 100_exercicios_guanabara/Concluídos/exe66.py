"""
Crie um programa que leia vário números inteiros pelo teclado. O progrma só vai parar quando o
usuário digitar 999, que é a condição de parada. no final mostre quantos números foram digitados
e qual foi a soma entre eles.
"""
soma = cont = 0
while True:
    num = int(input('Digite um número: (999 para sair) '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'A soma dos {cont} números que você digitou é {soma}!!')
