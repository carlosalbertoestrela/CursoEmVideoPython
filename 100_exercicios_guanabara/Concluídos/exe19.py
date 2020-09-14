import random
n = 1
alunos = []
while n <= 4:
    nome = input(f'digite o nome do {n}º anuno: ')
    alunos.append(nome)
    n += 1
print(f'O escolhido foi {random.choice(alunos)}!')

