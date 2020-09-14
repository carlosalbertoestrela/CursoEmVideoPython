"""
Desolvolva um programa que leia 6 números
inteiros e mostre a soma apenas daqueles
que forem pares. se o valor digitado for impar,
desconsidere-o.
"""
total = 0
cont = 0
print('Digite 6 números inteiros que irei somar os pares digitados!')
for c in range(0, 6):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        cont += 1
        total = total + num
print(f"A somas dos {cont} números pares digitados é! {total}")
