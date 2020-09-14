"""
Escreva um programa que leia um númeor N inteiro e mostre na tela os N primeiros elementos da uma
sequência de Fibonacci.
EX:
0 > 1 > 1 > 2 > 3 > 5 > 8
Fn = F(n-1) + F(n-2)
"""
print("Sequencia de Fibonacci")
print("=-="*10)
num = int(input('Digite quantos termos deseja ver: '))
cont = 2
term = 1
ant = 0
prox = 1
print(f'{ant} > ', end='')
while cont <= num:
    print(f'{term} > ', end='')
    term = ant + prox
    ant = prox
    prox = term
    cont += 1
print('Fim')
