"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida:
 - Média abaixo de 5.0:
    Reprovado
 - Média entre 5.0 e 6.9:
    Recuperação
 - Média 7.0 ou superior:
    Aprovado
"""
nota1 = float(input("Insira suas notas para calcular sua média!\n"
                    "Nota1: "))
nota2 = float(input("Nota 2: "))
media = (nota1+nota2)/2
if media < 5:
    print(f'sua média foi {media:.1f}: REPROVADO')
elif media >= 5 and media <= 6.9:
    print(f'Sua média foi {media:.1f}: RECUPERAÇÃO')
else:
    print(f'Sua média foi {media:.1f}: APROVADO')
