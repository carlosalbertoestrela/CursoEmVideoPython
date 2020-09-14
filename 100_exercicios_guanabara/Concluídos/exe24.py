# Minha solução
cidade = str(input('Qual cidade você nasceu? ')).strip().lower()
resposta = True
if (cidade.split())[0] == 'santo':
    print(resposta)
else:
    resposta = False
    print(resposta)
# Solução do Guanabara
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
