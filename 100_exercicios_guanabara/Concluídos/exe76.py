'''
Exercício Python 076:
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
produtos = ('Escova', 2.1, 'Paçoca', 0.3, 'Pasta de Dente', 2.5, 'Caneta', 0.25, 'Casa', 12000.90, 'Chinelo', 12.7,
            'bicicleta', 2300)
print(f'{"Produtos / preços":-^40} ')
cont = 0
while len(produtos) != cont:
    print(f"{produtos[cont]:.<30}", f'R${produtos[cont+1]:>8.2f}')
    cont += 2
print('-'*40)

# Soluçãodo Guanabara:

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print('-'*40)
