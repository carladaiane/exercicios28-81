import math as m


""" algoritmo 59 
Entrar com os valores dos catetos de um triângulo retângulo e imprimira hipotenusa 
prog 1ea32 
real a,b,c; 
imprima "\nEntrar com 1 cateto:, 
leia b, 
imprima "\nEntrar com 2 cateto: 
leia c, 
a <- raiz (b**2 i- c**2), 
imprima "\nA hipotenusa e ", a, 
imprima " \n " , 
fi mprog """


b = float(input('Entrar com 1 cateto:'))
c = float(input('Entrar com 2 cateto:'))
a =  m.sqrt(b**2 + c**2)

print( f"\nA hipotenusa é: {a:.2f}") 
print(f'\n')