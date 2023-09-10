sm = float(input('\n Entre com o salário mínimo:'))
qtdade = float(input('\n Entre com a quantidade quilowatt:'))
preco = sm/700
vp = preco * qtdade
vd = vp * 0.9

print(f'\n Preço do quilowatt: {preco:.2f}, \n valor a ser pago: {vp:.2f}, \n valor com desconto: {vd:.2f}')

print(f'\n')

