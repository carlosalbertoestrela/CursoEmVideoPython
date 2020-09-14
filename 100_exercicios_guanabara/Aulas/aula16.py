lanche = ('Hambúrguer', 'Suco', 'pizza', 'Pudim', 'Batata frita')
#for cont in range(0, len(lanche)):
for comida in lanche:
    print(f'eu vou comer {comida}')
print('comi pra caramba!!')

for pos, rango in enumerate(lanche):
    print(f'Eu vou comer {pos} {rango}')
print('Comi pra caramba mesmo!!')

print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c, d)