from random import randint
from time import sleep

print("---Jogo da advinhação--- \n --Vou pensar em um número de 1 a 5, tente advinhar!!--")
computador = randint(0, 5)
print("Pendando....")
sleep(3)
num = int(input('Qual nuúmero vc acha que pensei? '))
if num == computador:
    print(f'eu pensei no número {computador}!!')
    print(f'Parabêns voce acertou!!')
else:
    print(f'eu pensei no número {computador}!!')
    print('Que pena, vc errou!')
