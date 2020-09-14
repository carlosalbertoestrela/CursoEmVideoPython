"""
Exercício Python 094:
 Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
pessoa = dict()
grupo = list()
print(f'{"Cadastro de pessoas!":=^60}')
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = str(input('Sexo [M/F] ')).strip().upper()[0]
    grupo.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input('Novo cadastro? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*60)
print(f'Foram cadastradas {len(grupo)} pessoas!')
somaIdade = 0
mulheres = list()
acimaDaMedia = list()
for i, v in enumerate(grupo):
    somaIdade += grupo[i]['idade']
    if grupo[i]['sexo'] == 'F':
        mulheres.append(grupo[i]['nome'])
mediaIdade = somaIdade/len(grupo)
for i, v in enumerate(grupo):
    if grupo[i]['idade'] > mediaIdade:
        acimaDaMedia.append(grupo[i]['nome'])
print(f'A idade média do grupo é {mediaIdade} anos.')
print(f'A lista de mulheres no cadastrasdas foi: {mulheres}.')
print(f'As pessas com idade acima da média foram: {acimaDaMedia}')
