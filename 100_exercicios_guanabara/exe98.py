"""
Exercício Python 098:
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
    a) de 1 até 10, de 1 em 1
    b) de 10 até 0, de 2 em 2
    c) uma contagem personalizada
"""
def titile(txt):
    ajuste = len(txt) + 4
    print('=' * ajuste)
    print(f'{txt:^{ajuste}}')
    print('=' * ajuste)


def contador(start, end, step):

    titile(f'A contagem de {start} até {end}, de {step} em {step} é:')
    from time import sleep
    if step == 0:
        step = 1
        end -= 1
    if start > end:
        if step > 0:
            step *= -1
        if end < 1:
            end -= 1
    else:
        end += 1
    for i in range(start, end, step):
        print(f'{i} ', end='')
        sleep(0.25)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a sua contagem! ')
contador(int(input('inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
