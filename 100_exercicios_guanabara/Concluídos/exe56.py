"""
Desenvolva um programa que leia o nome, sexo
e idade de 4 pessoas. no final do programa
mostre:
 - A média de idade do grupo
 - Qual o nome do homem mais velho
 - Quantas mulheres tem menos de 20 anos.
"""
menos20 = 0
idades = 0
idadeh = 0
maisVelho = ''

for c in range(1, 5):
    print(f'====={c}ª Pessoa=====')
    nome = str(input('Digite seu nome: '))
    sexo = str(input('Sexo: [M/F] ')).strip().lower()
    idade = int(input('Digite sua idade: '))
    if sexo == "f":
        if idade < 20:
            menos20 += 1
            idades = idades + idade
    elif sexo == "m":
        if idade > idadeh:
            maisVelho = nome
            idades = idades + idade
print(f'A média de idade desse grupo é {idades/4}.\n'
      f'O homem mais velho é o {maisVelho}.\n'
      f'e existem {menos20} mulheres com menos de 20 anos')
