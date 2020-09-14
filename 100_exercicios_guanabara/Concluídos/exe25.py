# Minha solução
nome = str(input('Digite seu nome complete: ')).strip().upper()
lista = nome.split()
print(f'Seu nome tem Silva? {("SILVA" in lista)}')

# Solução do Guanabara
nome = str(input('Qual seu nome completo: '))
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
# Melhor solução
nome = str(input('Qual seu nome completo: ')).strip().lower().split()
print(f'Seu nome tem Silva? {"silva" in nome}')
