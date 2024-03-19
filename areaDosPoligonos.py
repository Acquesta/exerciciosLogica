lados = int(input('Digite quantos lados tem seu polígono: '))
medidas = int(input('Digite os centímetros dos lados: '))

menssagem = ''

if lados < 3:
    menssagem = 'NÃO É UM POLÍGONO'
elif lados == 3:
    menssagem = f'Seu polígono é um TRIÂNGULO e a área é: {(medidas * medidas) / 2}'
elif lados == 4:
    menssagem = f'Seu polígono é um QUADRADO e a área é: {medidas * medidas} '
elif lados == 5:
    menssagem = 'A quantidade de lados é igual a um polígono'
else:
    menssagem = 'POLÍGONO NÃO INDENTIFICADO'
print(menssagem)