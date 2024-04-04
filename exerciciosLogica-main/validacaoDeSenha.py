senha = int(input('Digite sua senha: '))
senhaValida = 1234
confimacao = 'NEGADO'

if senha == senhaValida:
    confimacao = "PERMITIDO"

print(f'ACESSO {confimacao}')
