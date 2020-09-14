import colorsys


velocidade = float(input('Digite a velocidade do atual do carro: KM/h '))
if velocidade > 80:
    vMulta = (velocidade-80.0) * 7.0
    print('Multado!!!')
    print(f'Velocidade acima do permitido, valor da multa R$ {vMulta}')
print('Tenha uma boa viagem!')
