num = float (input(f'\nentre com um numero com parte fracionaria:'))
num1 = round(num - 0.5)
numfrac = num - num1

numa = round(num + 0.00001)

print (f'\nparte inteira: {num1}')
print(f'\nParte fracionária: {(numfrac + 0.00001):.3f}')
print(f'\nParte arredondado: {numa}')

print(f"\n")