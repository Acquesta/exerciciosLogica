quantidade = int(input('Digite a quantidade de números que você quer ordenar: '))
valores = []

for x in range(quantidade):
    valores.append(int(input(f'Digite o {x + 1}° número: ')))

for x in valores:
    for valor in valores:
        lugar = valores.index(valor)

        if lugar < len(valores) - 1:
            valorProximo = valores[lugar + 1]
            indexProximo = valores.index(valorProximo)

            if valores[lugar] > valorProximo:
                valores.pop(indexProximo)
                valores.insert(lugar, valorProximo)

                print(f"{valor} > {valorProximo}")
                print('')
            else:
                print(f'{valor} < {valorProximo}')
                print('')
        else: 
            print('Lista', valores)
