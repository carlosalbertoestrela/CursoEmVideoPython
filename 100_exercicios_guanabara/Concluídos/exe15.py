dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input("Quantos Km's rodados?" ))
valor = (dias*60)+(km*.15)
print(f'O valor do aluguel a ser pago é: R${valor:.2f}!')
