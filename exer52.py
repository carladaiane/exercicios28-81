import math as m

lado = float (input(f'\nDigite o lado do quadrado:'))

perimetro =  4 * lado

area = lado ** 2

diagonal = lado * m.sqrt(2)


print(f"\nperimetro:{perimetro:.2f}" )
print(f"\narea:{area:.2f}" )
print(f"\ndiagonal:{diagonal:.2f}" )
print( f"\n")

