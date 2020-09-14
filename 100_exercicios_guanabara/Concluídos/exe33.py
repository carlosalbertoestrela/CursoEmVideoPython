cont =1
maior = 0
menor = 0
while cont <= 4:
    num = (float(input(f'Digite o {cont}º valor: ')))
    if num > maior:
        maior = num
        cont += 1
    elif num > 0 and num < maior:
        menor = num
        cont += 1
    else:
        cont += 1
print(f'O maior valor digitado foi {maior} \nO menor valor digitado foi {menor}')
