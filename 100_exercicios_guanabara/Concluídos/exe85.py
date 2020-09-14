"""
Exercício Python 085:
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista = [[], []]
for i in range(1,8):
    n = int(input(f'Digite o {i}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-='*30)
print(f'Os números impáres que você digitou foram: {sorted(lista[1])}')
print(f'E os pares foram: {sorted(lista[0])}!')
