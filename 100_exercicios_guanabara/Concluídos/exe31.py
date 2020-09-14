dist = float(input('Qual a distancia da sua viagem? '))
if dist <= 200:
    preco = dist * .5
else:
    preco = dist * .45
print(f'Você está prestes a começar uma viagem de {dist:.2f}km')
print(f'E o preço da sua passagem será de R${preco:.2f}')
