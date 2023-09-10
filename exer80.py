quant = int (input(f'\n Digite a quantidade de fitas: '))
valAluguel = float (input(f'\n Digite o valor do aluguel: '))


fatAnual = quant/3 * valAluguel * 12

print(f'\nFaturamento anual: {fatAnual:.2f}')

multas = valAluguel * 0.1 * (quant/3) / 10

print(f'\nMultas mensais: {multas:.2f}')

quantFinal = (quant - quant * 0.02 + quant/10) #quant * 1.08 ?

print(f'\nQuantidade de fitas no final do ano: {quantFinal:.2f}')

print('\n')
 

