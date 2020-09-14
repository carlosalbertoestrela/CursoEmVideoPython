"""
Escreva um programa que escregva um número inteiro qualquer e peça para o usuário escolher qual será sia BASE DE
CONVERSÃO:
 - 1 para BINÁRIO
 - 2 para OCTAL
 - 3 par HEXADECIMAL
"""
num = int(input('Digite um número inteiro: '))
print('Escolha uma das basese pare conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
opc = int(input('Sua opção: '))
if opc == 1:
    print(f'{num} convertido para Binário é {bin(num)}')
elif opc == 2:
    print(f'{num} convertido para Octal é {oct(num)} ')
elif opc == 3:
    print(f'{num} convertido para Hexadecimal é {hex(num)}')
else:
    print('Opção inválida')
