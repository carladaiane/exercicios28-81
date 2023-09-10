tempo = int(input('\ndigite o tempo(numero de meses): '))
valor = float(input('\ndigite o valor da prestação: '))
taxa = float(input('\ndigite a taxa: '))

prest = valor+(valor*(taxa/100)*tempo)


print(f'\no valor da prestacao em atraso é {prest:.2f}')

print(f"\n")