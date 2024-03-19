masculinoFeminino = int(input('Digite 1 para homem, ou 2 para mulher: '))
altura = int(input('Agora digite seu sua altura: '))
pesoIdeal = (72.7 * altura) - 58

if masculinoFeminino == 2:
    pesoIdeal = (62.1 * altura) - 44.7


print(f'O seu peso ideal é: {pesoIdeal}')