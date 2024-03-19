valor1 = int(input('Digite o primeiro valor para se ordenado: '))
valor2 = int(input('Digite o segundo valor para se ordenado: '))
valor3 = int(input('Digite o terceiro valor para se ordenado: '))

aux = ''

if valor1 > valor2 and valor1 > valor3:
    aux = valor1
    valor1 = valor3
    valor3 = aux
elif valor2 > valor3:
    aux = valor2
    valor2 = valor3
    valor3 = aux
if valor1 > valor2:
    aux = valor1
    valor1 = valor2
    valor2 = aux

print(valor1, valor2, valor3)

