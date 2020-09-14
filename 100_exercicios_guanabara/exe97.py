"""
Exercício Python 097:
 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
 mostre uma mensagem com tamanho adaptável.
 Ex:
 escreva(‘Olá, Mundo!’) Saída:
   ~~~~~~~~~~~
   Olá, Mundo!
   ~~~~~~~~~~~
"""


def escreva(texto):
    alinhado = len(texto)+2
    print('-' * alinhado)
    print(f'{texto:^{alinhado}}')
    print('-' * alinhado)

for i in range(1, 4):
    escreva(str(input('Digite algo: ')))
