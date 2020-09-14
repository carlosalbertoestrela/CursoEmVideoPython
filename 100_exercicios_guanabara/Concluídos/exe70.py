"""
Crie um programa que leia o nome e o preço de vários produtos. o programa deve perguntar
ao usuário se ele deseja continuar. no final mostre:

A) Qual o total gasto na compra
B) Qantos produtos custam mais de R$1000,00
C) Qual o nome do produto mais caro e do mais barato

"""
prodMais = prodMenos = ''
valmais = plus1k = valmenos = total = 00
p1 = True
print("Carrinho de compras".upper(), '\n', '='*20)
while True:
    prod = str(input('Nome do Produto: '))
    val = float(input('Preço: R$'))
    if p1:
        prodMais = prodMenos = prod
        valmais = valmenos = val
        total += val
        p1 = False
    else:
        if val > valmais:
            valmais = val
            prodMais = prod
        elif val < valmenos:
            valmenos = val
            prodMenos = prod
    total += val
    if val >= 1000:
        plus1k += 1
    while True:
        dec = str(input('Deseja continuar comprando? [S/N] ')).strip().upper()[0]
        if dec in 'SN':
            break
    if dec == 'N':
        break
print(f'O valor total da compra foi: {total}, o mais caro foi o {prodMais}, o mais barato foi o {prodMenos} e'
      f' {plus1k} produtos custaram mais de R$1000,00')
