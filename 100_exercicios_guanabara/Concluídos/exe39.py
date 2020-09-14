"""
Faça um programa que leia o ano de nascimento de um jovem e informe, se acordo com sua idade:
  - se ele ainda vai se alistar ao serviço militar.
  - se é a hora de se alistar.
  - se já passou do tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

ano_n = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano_n
if idade < 18 and idade > 0:
    print(f'Ainda faltam {18 - idade} para que você possa se alistar!')
elif idade == 18:
    print('Você completa 18 anos esse ano! Está na hora de se alistar!!')
elif idade > 18:
    print(f'Você deveria se alistar a {idade - 18} anos atrás.')
else:
    print('Você veio do futuro? O.o')
