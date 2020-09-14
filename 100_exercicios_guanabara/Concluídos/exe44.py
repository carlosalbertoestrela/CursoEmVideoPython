"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e a condição de
pagamento:
 - À vista Dinchero/cheque: 10% de desconto.
 - À vista no Cartão: 5% de desconto.
 - Em até 2x no cartão: Preço normal.
 - 3x ou mais no cartão: 20% de juros.
"""
print(f'{" Lojas Beto ":=^40}')
preco = float(input('Digite o preço do produto: R$'))
fpag = int(input('Escolha entre as formas de pagamento abaixo:\n'
                 '[ 1 ] À vista Dinheiro/Cheque(10% de desconto).\n'
                 '[ 2 ] À vista Cartão.(5% de desconto)\n'
                 '[ 3 ] Em até 2x no Cartão.(preço normal)\n'
                 '[ 4 ] 3x ou mais no cartão.(20% de juros)\n'
                 'Sua escolha: '))

print('O valor final será: ')
if fpag == 1:
    print(f'R${preco - (preco*.1):.2f}')
elif fpag == 2:
    print(f'R${preco - preco*.05:.2f}')
elif fpag == 3:
    print(f'R${preco}')
elif fpag == 4:
    parcela = int(input('Quantas parcelas: '))
    print(f'Em {parcela} parcelas de R${(preco*.2)/parcela:.2f} ')
    print(f'o preço final sertá R${preco + (preco*.2)}')
else:
    print('Forma de pagamento inválida')
