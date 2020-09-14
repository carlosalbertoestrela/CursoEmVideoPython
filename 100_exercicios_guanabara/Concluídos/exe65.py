"""
Crie um programa que leia vários números inteiros pelo teclado. no final da execução, mostre a média
ente todos os valores e qual foi o menor e o mior valor lido. O programa deve perguntar ao usuário se ele quer ou não
cointinuar a digitar valores.
"""
soma = 0
cont = 0
maior = 0
menor = maior
while True:
    cont += 1
    num = int(input('Digite um número: '))
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    sai = input('Deseja continuar?[S/N]: ').strip().upper()
    if sai == 'N':
        break

media = soma / cont
print(f'A média dos número digitados é {media:.2f} e o maior deles foi {maior} e o menor valor foi {menor}')
