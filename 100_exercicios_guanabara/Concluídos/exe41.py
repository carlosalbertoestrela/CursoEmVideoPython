"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idede:
 - Até 9 anos: Mirim
 - Até 14 anos: Infantil
 - Até 19 anos: Junior
 - até 20 anos: Sênior
 - Acima: Master
"""
from datetime import date

ano = int(input("Digite o ano de nascimento do atleta: "))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
