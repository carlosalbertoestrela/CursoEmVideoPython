"""
Crie um programa que leia uma fraze qualquer
e diga se ela é um palindromo, desconsiderando
os espaços.
"""
frase = str(input('Digite uma frase: ')).strip()
inverso = []
normal = []
for c in range((len(frase)-1), -1, -1):
    if frase[c] != " ":
        inverso.append(frase[c])
for c in range(0, len(frase)):
    if frase[c] != " ":
        normal.append(frase[c])


if normal == inverso:
    print('É um palindromo')
else:
    print('Não é um palindromo')

# Solução do Guanabara:
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inver = ''
for letra in range(len(junto)-1, -1, -1):
    inver += junto[letra]
print(f"Você digitou {junto} e o seu inverso é {inver}")
if junto == inver:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo')
