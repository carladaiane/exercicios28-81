import math as m

num = float(input('\n Entre com o logaritmando:'))

base = float(input('\n Entre com a base:'))

logaritmo = m.log(num) / m.log(base)

print(f'\nO Logaritmo de {num} na base {base} é {logaritmo:.2f}')

print(f'\n')