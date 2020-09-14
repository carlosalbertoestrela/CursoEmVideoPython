print('-=-'* 10 + '\nAnalisando Triângulos \n' + '-=-' * 10)
s1 = float(input('Primeiro seguimento = '))
s2 = float(input('Segundo seguimento = '))
s3 = float(input('Terceiro seguimento = '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os seguimentos PODEM FORMAR um triângulo!')
else:
    print('Os seguimentos NÃO PODEM fomrar uma triâgulo')
