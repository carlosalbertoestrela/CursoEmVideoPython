"""
Exercício Python 083:
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
O aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
equacao = list(input('Digite sua equação: '))
print(equacao)
inicio = False
final = False
for i, t in enumerate(equacao):
    if t == '(':
        inicio = True
        for t2 in equacao:
            if t2 == ')':
                final = True
if inicio and final:
    print('Equação válida!')
else:
    print('Equação inválida')

# Solução do guanabara:
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Válida')
else:
    print('Inválida')
    