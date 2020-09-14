"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
 - Abaixo de 18.5: Abaixo do peso
 - Entre 18.5 e 25: Peso ideal
 - 25 até 30: Sobrepeso
 - 30 até 40: Obesidade
 - Acima de 40: Obesidade mórbida
"""
altura = float(input('Digite sua altura em métros: '))
peso = float(input('Digite o seu peso em Kg: '))
imc = peso / (altura**2)
print(f'Seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está no seu PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
