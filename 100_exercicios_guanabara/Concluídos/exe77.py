"""
Exercício Python 077:
 Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
dic = ('teste', 'carro', 'casa', 'pessoas', 'casamento', 'trabalho', 'gatos', 'amor', 'jogos', 'computador', 'vida')

for palavra in dic:
    a = list(palavra.lower())
    print(f'Na palvre {palavra.upper()} temos ', end='')
    for vogal in a:
        if vogal in 'aeiou':
            print(f'{vogal} ', end='')
    print('')

# Solução so Guanabara:

for p in dic:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra} ', end='')
