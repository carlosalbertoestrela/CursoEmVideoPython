salario = float(input('Digite seu sálario: '))
if salario > 1250.0:
    salario = salario + (salario*.1)
    print(f'Seu novo salário terá um aumento de 10% e será R${salario:.2f}')
else:
    salario = salario + (salario*.15)
    print(f'Seu novo salário terá um aumento de 15% e será R${salario:.2f}')
