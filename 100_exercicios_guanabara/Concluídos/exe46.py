"""
Faça um programa que mostre na tela uma contagem
regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entrel
"""
from pygame import mixer
from time import sleep
from emoji import emojize

print("Contagem regressiva!!")
for c in range(10, -1, -1):
    print(f'{c}!!!!')
    sleep(1)
print(emojize('Booom!! :fireworks: Boooom!! :fireworks:\n'*10))
