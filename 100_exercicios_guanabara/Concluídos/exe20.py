from random import shuffle
r = 1
alunos = []
while r <= 4:
    nome = input(f'Digite o nome do {r}º aluno: ')
    alunos.append(nome)
    r += 1
shuffle(alunos)
print(f'A ordem de apresentação será {alunos}')

