"""
Exercício Python 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print(f'{n} adicionado com sucesso...')
    else:
        print(f'{n} já existe na lista...')
    while True:
        t = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if t in 'SN':
            break
    if t == 'N':
        break
print(f'A lista digitada foi {sorted(num)}')
