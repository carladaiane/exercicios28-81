import math as m

base = float(input(f'\n Digite base:'))
altura = float(input(f'\n Digite altura:'))
perimetro = 2*(base + altura)
area = base * altura
diagonal = m.sqrt(base**2 + altura**2)

print (f"\nPerimetro = {perimetro:.2f}")
print (f"\nArea = {area}")
print (f"\nDiagonal = {diagonal:.2f}")

print (f"\n" )











