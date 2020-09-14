'''
Crie um program que tenha uma tupla totalmente preenchida por uma
contagem por extenso, de zero a vinte.
seu programa deverá ler um número pelo teclado de 0 a 20 e mostrá-lo
por extenso.
'''

cont = ('zero', 'um', 'dois', 'tês', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'desenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Número inválido, tente novamente...')
    print(f'O número que você digitou foi {str(cont[num]).upper()}')
    while True:
        t = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if t in 'SN':
            break
    if t == 'N':
        break
