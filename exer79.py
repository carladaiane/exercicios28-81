p = float (input(f'\ndigite o valor da aplicacao: '))
n = int (input(f'\ndigite o valor da meses: '))
i = float (input(f'\ndigite o numero de taxa: '))

va = p*(((1+ i )** n)-1) / i


print (f'\nO valor acumulado: {va:.2f}')

print(f"\n")






