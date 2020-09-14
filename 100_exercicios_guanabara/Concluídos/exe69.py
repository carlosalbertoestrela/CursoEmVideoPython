"""
Crie um programa que leia o sexo e a idade de várias pessoas, a cada pessoa cadastrada o programa deve
perguntar se o usuário quer continuar ou não. no final mostre:

A) Quantas pessoas tem mais de 18 anos:
B) Quantos homens foram cadastrados:
C) Qauntas mulheres tem menos de 20 anos
"""
p18 = homens = mulheres20 = cont = 0

while True:
    print(f'{cont+1}º Cadastro \n', '-=-' * 20)
    while True:
        sexo = str(input('Qual o sexo: [M/F] ')).strip().upper()[0]
        if sexo in 'MF':
            break
    idade = int(input('Digita a idade: '))
    print('-=-' * 20)
    d = ''
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres20 += 1
    if idade >= 18:
        p18 += 1
    cont += 1
    while True:
        d = str(input('Fazer novo cadastro?: [S/N]')).strip().upper()[0]
        if d in 'SN':
            break
    if d == 'N':
        break
print('~~'*20)
print(f"""Foram cadastradas {cont} pessoas, entre elas:
{homens} Homens, {mulheres20} mulheres com menos de 20 anos e {p18} pessoas com mais de 18 anos.""")