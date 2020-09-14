"""
Exercício Python 093:
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
 No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
jogador['gols'] = list()
for i in range(1, jogador['partidas']+1):
    gol = int(input(f'Quantos gols na partida {i}: '))
    jogador['gols'].append(gol)
jogador['total'] = sum(jogador['gols'])
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}!')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na {i+1}ª partida fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols!')
