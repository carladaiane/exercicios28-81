sm = float(input('\n Entre com o salário mínimo:'))
qtdade = float(input('\n Entre com a quantidade quilowatt:'))
preco = sm/700
vp = preco * qtdade
vd = vp * 0.9

print(f'\n preço do quilowatt: {preco:.2f}, valor a ser pago: {vp:.2f}, valor com desconto: {vd:.2f}')

print(f'\n')

