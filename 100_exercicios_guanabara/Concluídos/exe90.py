"""
Exercício Python 090:
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
nome = str(input('Nome: '))
media = float(input(f'Qual a média do(a) {nome}? '))
situacao = ''
if media >= 7.0:
    situacao = 'Aprovado'
elif  media >= 5 and media <= 6.9:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'
aluno = {'nome': nome, 'media': media, 'situação': situacao}
print('='*40)

print(f'{aluno["nome"]} teve médias {aluno["media"]} e está {aluno["situação"]}')

# Solução do Guanabara:


alunos = dict()
alunos['nome'] = str(input("Nome: "))
alunos['média'] = float(input(f"Qual a média de {alunos['nome']}? "))
if alunos['média'] >= 7:
    alunos['sutuação'] = 'Aprovado'
elif 5 <= alunos['média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
print('*='*30)
for k, v in alunos.items():
    print(f' - {k} é igual a {v}')

