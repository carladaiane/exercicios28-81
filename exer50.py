import math as m

""" algoritmo 50 
Entrar com a base e a altura de um retângulo e imprimir a seguinte saída: 
peri metro 
area 
diagonal: 
prog 1ea23 
real perimetro, area, diagonal, base, altura; 
imprima "\ndigite base: 
leia base, 
imprima "\ndigite altura: 
leia altura, 
perimetro < 2*(base + altura); 
area <-base * altura; 
diagonal <- raiz(base**2 + alt u ra**2), 
imprima "\nperimetro = " ,perimetro, 
imprima "\narea = ", area , 45 
imprima "\ndiagonal = ", diagonal 
imprima "\n; 
fi mprog """

base = float(input('Digite base:'))
altura = float(input('Digite altura:'))
perimetro = 2*(base + altura)
area = base * altura
diagonal = m.sqrt(base**2 + altura**2)

print (f"\nPerimetro = {perimetro:.2f}")
print (f"\nArea = {area}")
print (f"\nDiagonal = {diagonal:.2f}")

print (f"\n" )











