"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número digitado for negativo.

"""
while True:
    num = int(input('Digite um número para saber sua taboada! '))
    if num > 0:
        cont = 1
        print('='*50)
        while cont <= 10:
            print(f'{num:} X {cont:2} = {num*cont}')
            cont += 1
        print('=' * 50)
    else:
        print('Taboada finalizada')
        break
