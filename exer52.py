import math as m

""" algoritmo 52 
Entrar com o lado de um quadrado e imprimir: 
peri metro: 
area: 
diagonal: 
prog 1ea25 
real lado, perimetro, area, diagonal; 
imprima "\ndigite o lado do quadrado: 
leia lado 
perimetro <_ 4 * lado; 
area<- lado ** 2; 
diagonal <- lado * raiz(2); 
imprima "\nperimetro: ", perimetro; 
imprima "\narea: ", area; 
imprima "\ndiagonal: ", diagonal; 
imprima "\n"; 
fimprog """


lado = float (input('Digite o lado do quadrado:'))

perimetro =  4 * lado

area = lado ** 2

diagonal = lado * m.sqrt(2)


print(f"\nperimetro:{perimetro:.2f}" )
print(f"\narea:{area:.2f}" )
print(f"\ndiagonal:{diagonal:.2f}" )
print( f"\n")

