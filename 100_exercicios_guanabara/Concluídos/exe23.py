# Minha solução
num = str(input('Digite um número: '))
numl = [0, 0, 0, 0]
numl.extend(list(num))
print('Esse número tem: ')
print(f'{numl[-1]} unidades')
print(f'{numl[-2]} dezenas')
print(f'{numl[-3]} centenas')
print(f'{numl[-4]} milhares')

# Solução do Guanabara
num = int(input('Infome um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('unidades: {}'.format(u))
print('dezenas: {}'.format(d))
print('centenas: {}'.format(c))
print('milhares: {}'.format(m))
