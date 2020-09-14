"""
Faça um programa que leia o peso de 5 pessoas.
No final, mostre qual foi o maior e o menor
peso lidos.
"""
pessoas = []
for c in range(0, 5):
    peso = float(input(f"Digite o {c+1}º peso: "))
    pessoas.append(peso)
pessoas.sort()
print(f"O maior peso digitado foi {pessoas[-1]} e o menor peso foi {pessoas[0]}")
#solução do Guanabara
maior = 0
menor = 0
for c in range(1, 8):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            peso = maior
        if peso < menor:
            peso = menor
print(f'O mior peso digitado foi {maior}kg\n'
      f'O menor peso digitado foi {menor}kg')
