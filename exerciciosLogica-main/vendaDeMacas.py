macas = int(input('Digite o número de maçãs que você deseja comprar: '))
precoPorMaca = 0.30

if macas >= 12:
    precoPorMaca = 0.25

total = macas * precoPorMaca
print(f'O preço por maçã foi {precoPorMaca}, e o total da compra foi {total}')