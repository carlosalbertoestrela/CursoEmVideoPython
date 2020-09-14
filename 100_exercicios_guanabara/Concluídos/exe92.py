"""
Exercício Python 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
contribuinte = dict()
contribuinte['nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
contribuinte['idade'] = date.today().year - idade
ctps = int(input('CTPS (0 se não tiver): '))
if ctps != 0:
    contribuinte['CTPS'] = ctps
    contribuinte['contratação'] = int(input('Ano de inicio da contribuição: '))
    contribuinte['salário'] = float(input('Salário: R$'))
    contribuinte['aposentadoria'] = (contribuinte['contratação'] - idade) + 35
print('-='*20)
for k, v in contribuinte.items():
    print(f'  - {k} tem o valor {v} ')
