"""
Escreva um program para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar
O VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
Calcule o valor da prestação mensal, saberndo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from time import sleep
print('-=-'*20+'\n    Validação de Emprestimo   \n' + '-=-'*20)

preco = float(input(f'Digite o valor da casa que deseja comprar: R$'))
salario = float(input('Qual seu salário atual? R$'))
anos = int(input('Em quantos anos pretende quitar a casa? '))
prestacao = preco / (anos * 12)
print("<<<PROCESSANDO>>>")
sleep(3)
if prestacao < (salario*.3):
    print(f'Seu emprestimo foi aprovado!! \nSua prestação será de R${prestacao:.2f} dividida em {anos*12}x!')
else:
    print(f'Emprestimo REPROVADO!!!\nA prestação de R${prestacao} excede os 30% do seu salário.')
