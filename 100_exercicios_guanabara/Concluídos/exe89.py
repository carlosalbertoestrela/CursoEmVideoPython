"""
Exercício Python 089:
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.
"""
alunos = []
aluno = ['', [0, 0]]
while True:
    aluno[0] = (str(input('Nome: ')))
    aluno[1][0] = int(input('Nota 1: '))
    aluno[1][1] = int(input('Nota 2: '))
    alunos.append(aluno[:])
    aluno = ['', [0, 0]]
    t = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if t == 'N':
        break
print('-='*30)
for i in range(0, len(alunos)):
    media = (alunos[i][1][0] + alunos[i][1][1]) / 2
    print(f'{i+1} > {alunos[i][0]} = {media:.2f}')
print('-='*30)
while True:
    individual = int(input("Digite o número do aluno para ver suas notas ou 999 para sair: "))
    if individual == 999:
        print('Programa finalizado!')
        break
    elif individual > len(alunos):
        print('Aluno inválido!')
    else:
        print(f'As notas de {alunos[individual-1][0]} foram: {alunos[individual-1][1]}')


