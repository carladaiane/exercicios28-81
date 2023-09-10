deposito = float (input(f'\nentre com depósito: '))
taxa = float (input(f'\nentre coma taxa de juros: '))
valor = deposito*taxa/100
total = deposito + valor

print(f'\nRendimentos: {valor}, \nTotal:{total}')

print(f"\n")