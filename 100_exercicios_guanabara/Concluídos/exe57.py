"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ser um valor correto.
"""
while True:
    sexo = str(input("Sexo: [M/F] ")).strip().lower()
    if sexo == 'm' or sexo == 'f':
        break
    else:
        print('Valor de entrada incorreto, tente novamente.\n')
print(f'Sexo {sexo} registrado com sucesso!')


n = str(input('Sexo: [M/F] ')).strip().lower()
while 'f' != n and 'm' != n:
    print('Opção inválida!')
    n = str(input('Sexo: [M/F] '))
print(f'Sexo {n} registrado com sucesso!')

# Solução do guanabara:

sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado incorreto, favor informar seu sexo corretamente: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} gravado com sucesso!')
