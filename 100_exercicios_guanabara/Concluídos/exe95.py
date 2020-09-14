"""
Exercício Python 095:
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
time = list()
jogador = dict()
gols = list()
while True:     # Loop de limentação do dicionário Jogador
    jogador['nome'] = str(input('Nome: '))
    jogador['jogos'] = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    for i in range(0, jogador['jogos']):
        gols.append(int(input(f'    Quantos Gols na partida {i+1}: ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    continuar = str(input('Novo Jogador? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida!')
        continuar = str(input('Novo Jogador? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=='*30)
print(f'{"INFORMAÇÕES DO TIME":^60}')
print(f"{'cod':<5}{'nome':15}{'gols':18}{'total':>10}")
print('=='*30)
for i, v in enumerate(time):    # Varre o dicionário apresentando os jogadores
    print(f"{i:<5}{time[i]['nome']:15}{str(time[i]['gols']):18}{str(time[i]['total']):>10}")
print('=='*30)
while True:     # Mostra os dados detalhados do jogador escolhido
    dados = int(input('Mostrar Dados de qual Jogador? (999 para sair): '))
    if dados > len(time)-1:
        print('Jogador inválido, tente novamente!')
    elif dados == 999:
        print(f"{'<< VOLTE SEMPRE >>':^60}")
        break
    else:
        print(f'---Levantamento do jogador {time[dados]["nome"].upper()}---')
        print(f'{time[dados]["nome"]} jogou {time[dados]["jogos"]} partidas.')
        for i, v in enumerate(time[dados]['gols']):
            print(f'No jogo {i+1} fez {v} gols')
        print(f'Marcando um total de {time[dados]["total"]} gols!')
