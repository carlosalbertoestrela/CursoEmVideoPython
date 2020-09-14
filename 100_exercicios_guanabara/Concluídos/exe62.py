"""
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar masi alguns termos.
O programa encerra qundo ele disser que quer mostar 0 termos.
"""
print('Gerador de PA')
print("=-="*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} > ', end='')
        cont += 1
        termo += razao
    print('Pausa')
    mais = int(input('Quer ver mais termos? digite quantos: '))
print(f'Fim do programa foi finalizado com {total} termos')

print('fim')


