'''
Crie uma tupla preencida com os 20 primeiros colocados da
tabela do campeonato brasileiro de futebol, na ordem da colocação.
depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os 4 ultimos colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
'''

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiais', 'Bahia', 'Vasco', 'Atletico-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cuzeiro', 'SCA',
         'Chapecoense', 'Avaí')
print('='*40, f'\n{"Tabela do Brasileirão!":^40}\n', '='*40)
cont = 1
cont2 = 17
for n in times:
    print(f'{cont}º = {times[cont-1]}')
    cont += 1
    if cont == 6:
        break
print('='*40, f'\n{"Lanterninhas":^40}\n', '='*40)
for n in times:
    print(f'{cont2}°  = {times[cont2-1]}')
    cont2 += 1
    if cont2 == 21:
        break
print('='*40, f'\n{"Times do Brasileiro":^40}\n', '='*40)
for t in sorted(times):
    print(f'{t}; ')
print('-'*40)
chap = times.index('Chapecoense')
print(f'A Chapecoense está na {chap+1}ª posição')

#solução do Guanabara:
print(f'Lista dos 5 primeros times do Brasileirão: {times[:5]}')
print('-='*20)
print(f'lista dos 4 ultimos times do Brasileirão: {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
print('-='*20)
