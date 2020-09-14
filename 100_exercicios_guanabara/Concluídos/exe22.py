nome = str(input("Digite seu nome completo: ")).strip()
nomel = list(nome)
nomes = nome.split()
print(f'Nome em maiusculo {nome.upper()}')
print(f'nome me minusculo {nome.lower()}')
print(f'numero de letras {len(nome) - nome.count(" ")}')
print(f'Seu primeiro nome é {nomes[0]} e ele tem {nome.find(" ")} ')


